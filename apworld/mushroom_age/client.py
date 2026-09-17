from . import MushroomAgeWorld
from .randomushroom.main import main as randomushroom_main
import subprocess
from pathlib import Path

class MushroomAgeClientRunner():
    async def initialize(self):
        settings = MushroomAgeWorld.settings

        self.game_exe = settings.game_exe
    
    async def start(self, ap_url):
        randomushroom_main(Path(self.game_exe), ap_url)