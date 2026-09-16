from . import MushroomAgeWorld
import subprocess
from pathlib import Path

class MushroomAgeClientRunner():
    async def initialize(self):
        settings = MushroomAgeWorld.settings

        self.game_exe = settings.game_exe
        self.rand_exe = settings.rand_exe
    
    async def start(self, ap_url):
        rand_path = Path(self.rand_exe)
        game_path = Path(self.game_exe)
        args = ["--game_exe", self.game_exe]
        if ap_url:
            args.extend("--ap_url", ap_url)

        if not rand_path.exists():
            print("Client exe not found!")
        elif not game_path.exists():
            print("Game exe not found!")
        else:
            subprocess.Popen([rand_path] + args, cwd = rand_path.parent)