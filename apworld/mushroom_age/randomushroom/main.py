import json
import os
import shutil
import socket
import subprocess
import threading
from pathlib import Path

from .client import RandoClient
from .classes import GameManager, FilePatcher

def main(path, ap_url):
    program = MainProgram(path)
    program.start_randomized_game()

class MainProgram:
    server_host = "127.0.0.1"
    server_port = 55554

    def __init__(self, game_directory):
        super().__init__()

        self.game_directory = game_directory.parent
        self.game_executable = game_directory
        self.game_running = False
        self.server_running = False

        self.files_dir = Path(__file__).parent / 'files'
        self.file_patcher = FilePatcher()
        self.game_manager = GameManager()

    def _throw_error(self, title, blurb):
        print(f"{title}\n{blurb}")

    def start_randomized_game(self):
        if self.game_running:
            return

        self.file_patcher.set_root(self.game_directory)

        self.game_manager.build_tracker(self.game_directory)

        try_patch = self.apply_patch()
        error_title = "Error Running Game!"
        match try_patch:
            case "not an exe":
                self._throw_error(error_title, "The chosen game file is not an EXE! Please make sure your Mushroom Age executable file is the target game file before launching.")
            case "invalid architecture":
                self._throw_error(error_title, "The chosen game file has an invalid architecture! Please make sure you have chosen a valid Mushroom Age executable file before launching.")
            case _:
                if not self.server_running:
                    self.server_running = True
                    server_thread = threading.Thread(target = self.begin_tcp_server)
                    server_thread.daemon = True
                    server_thread.start()

                    client_thread = threading.Thread(target = self.begin_client)
                    client_thread.daemon = True
                    client_thread.start()

                game_thread = threading.Thread(target = self.launch_game)
                game_thread.daemon = True
                game_thread.start()

    def clean_directory(self):
        if self.game_running:
            return

        files_to_remove = [
            self.game_directory / "randomushroom.asi",
            self.game_directory / "randomushroom.pdb",
        ]

        for file_path in files_to_remove:
            if file_path.exists(): file_path.unlink()

        folders_to_remove = [
            self.game_directory / "randomushroom",
        ]

        for dir_path in folders_to_remove:
            if dir_path.exists(): shutil.rmtree(dir_path)

    
    def begin_tcp_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.server_host, self.server_port))

            s.listen(5)

            print(f"tcp server started")
            while True:
                c, addr = s.accept()

                print(f"client connected at {addr}")

    def begin_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((self.server_host, self.server_port))
                print(f"rando client successfully connected!")

                self.client = RandoClient(self.game_manager, client_socket)
                command_dict = {
                    # signals sent from the game
                    "game_begin_task": self.client.on_begin_task,
                    "game_task_complete": self.client.on_task_complete,
                    "game_object_collected": self.client.on_object_collected,
                }

                def send_size_prefixed_data_chunk(self, command, args): # TODO: debug later
                    json_payload = json.dumps({"command": command, "args": args})
                    payload = bytearray(len(json_payload).to_bytes(4, 'big'))
                    payload.extend(json_payload.encode("utf-8"))
                    client_socket.sendall(payload)

                self.client.send_payload = send_size_prefixed_data_chunk

                def receive_data_chunk(size):
                    chunk = bytearray()
                    while len(chunk) < size:
                        chunk.extend(client_socket.recv(size - len(chunk)))
                    return chunk

                while True:
                    data_size = int.from_bytes(receive_data_chunk(4), 'big')
                    payload = receive_data_chunk(data_size)
                    data = json.loads(payload)

                    print(f"rando client received payload {data}")
                    if data.get("command") in command_dict:
                        command_dict[data["command"]](self.client, *data.get("args", []))

            except ConnectionRefusedError:
                print("rando client refused to connect")
            except socket.timeout:
                print("rando client timed out")

    def apply_patch(self):
        with open(self.game_executable, "rb") as game_exe:
            header = game_exe.read(2)
            if header != b"MZ":
                return "not an exe"
            else:
                game_exe.seek(60)
                header_offset = int.from_bytes(game_exe.read(4), 'little')

                game_exe.seek(header_offset + 4)
                machine = int.from_bytes(game_exe.read(2), 'little')

                match machine:
                    case 0x014c: arch = "i686"
                    case 0x8664: arch = "x86_64"
                    case _: return "invalid architecture"

                game_exe.seek(header_offset + 22)
                characteristics = int.from_bytes(game_exe.read(2), 'little')

                if characteristics & 0x2000: # dll flag
                    return "not an exe"

                # TODO: should probably also make the dll do a handshake with the program so it can verify it didn't just run an unrelated or unmodded game file

        print(f"{arch} EXE detected")

        self.clean_directory()

        shutil.copy(
            str(self.files_dir / "plugin" / arch / "randomushroom.asi"),
            str(self.game_directory),
        )
        pdb_path = self.files_dir / "plugin" / arch / "randomushroom.pdb"
        if pdb_path.exists():
            shutil.copy(
                str(pdb_path),
                str(self.game_directory),
            )

        self.file_patcher.move_images(
            images_to_move = [
                self.files_dir / "img_ap.tga",
            ],
        )

    def launch_game(self):
        self.game_running = True
        subprocess.run(
            [str(self.game_executable)],
            cwd = str(self.game_directory),
        )
        self.game_running = False