import json
import os
import socket
import shutil
import subprocess
import sys
import threading
from pathlib import Path

from PySide6 import QtWidgets

from randomushroom.classes import GameManager
from randomushroom.constants import *

def main():
    path = None
    # path = Path(path/to/your/game)

    if path is None:
        app = QtWidgets.QApplication(sys.argv)

        QtWidgets.QMessageBox.information(
            None,
            "Find your Mushroom Age Executable",
            "yo this is your reminder to uncomment the 'path' variable in main.py's main() function. ik it kinda sucks but until literally 5 minutes ago i just had my own game path sitting at the top of the file. just make sure not to include that line in your commits lmao. i'll make a proper GUI later i promise. anyway the program is closing now byeeee.",
        )

        sys.exit()

    program = MainProgram(path)

    server_thread = threading.Thread(target = program.begin_tcp_server)
    server_thread.daemon = True
    server_thread.start()

    client_thread = threading.Thread(target = program.begin_client)
    client_thread.daemon = True
    client_thread.start()

    program.apply_patch()
    program.launch_game()

class MainProgram:
    server_host = "127.0.0.1"
    server_port = 55554

    def __init__(self, game_directory):
        self.game_directory = game_directory.parent
        self.game_executable = game_directory
    
    def begin_tcp_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.server_host, self.server_port))

            s.listen(5)

            print(f"tcp server started")
            while True:
                c, addr = s.accept()

                print(f"client {addr} connected!")

    def begin_client(self):
        # TODO: set up functions for tcp hooks and AP hooks and stuff
        # client.on_begin_task("level_01_01")
        # client.on_object_collected("level_01_01", 4)
        # client.on_task_complete("level_01_01")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((self.server_host, self.server_port))
                print(f"rando client successfully connected!")

                self.client = RandoClient(self.game_directory, client_socket)
                command_dict = {
                    # signals sent from the game
                    "game_begin_task": self.client.on_begin_task,
                    "game_task_complete": self.client.on_task_complete,
                    "game_object_collected": self.client.on_object_collected,
                }

                def send_size_prefixed_data_chunk(self, command, args): # TODO: debug later
                    json_payload = json.dumps({"command": command, "args": args})
                    payload = len(json_payload).to_bytes(4, 'big')
                    payload += json_payload
                self.client.send_payload = send_size_prefixed_data_chunk

                def receive_data_chunk(size):
                    chunk = b""
                    while len(chunk) < size:
                        chunk += client_socket.recv(size - len(chunk))
                    return chunk

                while True:
                    data_size = int.from_bytes(receive_data_chunk(4), 'big')
                    payload = receive_data_chunk(data_size)
                    data = json.loads(payload)

                    print(f"rando client received payload {data}")
                    if data.get("command", "") in command_dict:
                        command_dict[data["command"]](self.client, *data.get("args", []))


            except ConnectionRefusedError:
                print("rando client refused to connect")
            except socket.timeout:
                print("rando client timed out")

    def apply_patch(self):
        shutil.copy(
            str(FILES_DIR / "plugin" / "randomushroom.asi"),
            str(self.game_directory),
        )
        pdb_path = FILES_DIR / "plugin" / "randomushroom.pdb"
        if pdb_path.exists():
            shutil.copy(
                str(pdb_path),
                str(self.game_directory),
            )

    def launch_game(self):
        subprocess.run(
            [str(self.game_executable)],
            cwd = str(self.game_directory),
        )

class RandoClient:
    def __init__(self, game_directory, tcp_client_socket):
        self.game_manager = GameManager(game_directory)
        self.tcp_client_socket = tcp_client_socket


    # signals received from game
    def on_begin_task(self, chapter, task_id):
        task = LEVEL_STRING.format(chapter, task_id)

        if self.game_manager.check_if_task_available(task):
            items = self.game_manager.check_task_gates(task)
            self.send_gate(items)
    
    def on_task_complete(self, chapter, task_id):
        task = LEVEL_STRING.format(chapter, task_id)

        if self.game_manager.complete_task(task):
            self.send_check(task)

            if self.game_manager.complete_quest(task):
                quest_item = self.game_manager.get_quest_name(task)
                self.send_item(quest_item)
                self.send_quest_to_tracker(quest_item)

    def on_object_collected(self, chapter, task_id, object_id): 
        task = LEVEL_STRING.format(chapter, task_id)

        if self.game_manager.collect_task_item(task, object_id):
            self.send_check(f"{task}_bonus")

    # signals sent to game
    def send_gate(self, items):
        self.send_payload("rand_main_menu", [])
        self.send_payload("rand_display_text", [f"You cannot play that task right now!\nYou need: {items}"]) # TODO: test and improve

    def send_item(self, item):
        self.send_payload("rand_display_text", [f"You received {item}!"]) # TODO: test and improve


    # signals received from AP
    def on_receive_check(self, check): # TODO: receive from AP
        ... # TODO: convert signal into self.receive_item call

    # signals sent to AP
    def send_check(self, check):
        ... # TODO: send signal to AP

    def send_quest_to_tracker(self, quest):
        ... # TODO: send signal to AP


    # helper functions
    def receive_item(self, item):
        if self.game_manager.receive_item(item):
            self.send_item(item)
