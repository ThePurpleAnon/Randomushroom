import os
import shutil
import subprocess
import sys
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

    program.begin_client()
    program.apply_patch() # TODO: only do this if patch is not found
    program.launch_game()

class MainProgram:
    def __init__(self, game_directory):
        self.game_directory = game_directory.parent
        self.game_executable = game_directory

    def begin_client(self):
        self.client = RandoClient(self.game_directory)

        # TODO: set up functions for tcp hooks and AP hooks and stuff
        # client.on_begin_task("level_01_01")
        # client.on_object_collected("level_01_01", 4)
        # client.on_task_complete("level_01_01")

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
    def __init__(self, game_directory):
        self.game_manager = GameManager(game_directory)


    # signals received from game
    def on_begin_task(self, task): # TODO: receive from game
        if self.game_manager.check_if_task_available(task):
            items = self.game_manager.check_task_gates(task)
            self.send_gate(items)
    
    def on_task_complete(self, task): # TODO: receive from game
        if self.game_manager.complete_task(task):
            self.send_check(task)

            if self.game_manager.complete_quest(task):
                quest_item = self.game_manager.get_quest_name(task)
                self.send_item(quest_item)
                self.send_quest_to_tracker(quest_item)

    def on_object_collected(self, task, object_id): # TODO: receive from game
        if self.game_manager.collect_task_item(task, object_id):
            self.send_check(f"{task}_bonus")

    # signals sent to game
    def send_gate(self, items):
        ... # TODO: send text to game about items gating progress

    def send_item(self, item):
        ... # TODO: send text to game about item received


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
