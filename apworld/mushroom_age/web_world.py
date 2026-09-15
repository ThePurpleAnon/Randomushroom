from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class MushroomAgeWebWorld(WebWorld):
    game = "Mushroom Age"
    theme = "jungle"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Mushroom Age for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ThePurpleAnon"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets