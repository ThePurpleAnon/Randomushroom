TIME_PERIODS = {
    "lab_2008":      {"name": "Einbock's Lab",       "chapters": [ 1,  7,  9, 20]},
    "cemetary_3008": {"name": "Cemetary",            "chapters": [ 2, 13, 17, 19]},
    "nostradamus":   {"name": "Nostradamus",         "chapters": [ 3, 11, 21]},
    "jurassic":      {"name": "The Jurassic Period", "chapters": [ 4, 10]},
    "stone_age":     {"name": "The Stone Age",       "chapters": [ 5, 14]},
    "socrates":      {"name": "Socrates",            "chapters": [ 6, 15]},
    "mushroom_age":  {"name": "The Mushroom Age",    "chapters": [ 8, 16, 22]},
    "omniscient":    {"name": "The Omniscient One",  "chapters": [12, 18]},
    "wedding":       {"name": "Happy Ending",        "chapters": [23]},
}

KEY_ITEMS = {
    "elixir":        {"id": 0, "name": "Progressive Elixir of Understanding", "pool_name": "progressive_elixir", "gates": [( 4,  2), ( 5,  1)]},
    "total_elixir":  {"id": 1, "name": "Progressive Elixir of Understanding", "pool_name": "progressive_elixir", "gates": [(22,  3)]},
    "painting":      {"id": 2, "name": "Professor's Painting",                "gates": [( 7,  2)]},
    "timequake":     {"id": 3, "name": "Timequake",                           "gates": [( 9,  1), (10,  1), (11,  1), (13,  1), (14,  1), (15,  1), (16,  1)]},
    "toilet":        {"id": 4, "name": "Toilet Time Machine", "useful": True, "gates": [(12,  1)]},
    "mushroom_soup": {"id": 5, "name": "Mushroom Soup",                       "gates": [(23,  1)]},
}

KEY_QUESTS = {
    "professor_hope": {"id": 10, "name": "Gave Professor Einbock Hope That His Wife May Return", "task": ( 7,  4), "gates": [(23,  1)]},
    "tom_return":     {"id": 11, "name": "Returned Tom Safely to 2008",                          "task": (13,  5), "gates": [(23,  1)]},
    "uber_mushroom":  {"id": 12, "name": "Appeased the Über-Mushroom",                           "task": (22,  3), "gates": [(23,  1)]},
    "victory":        {"id": 13, "name": "Got Married to Tom Scout",                             "task": (23,  2), "gates": []},
}

KEY_PHONE_NUMBERS = {
    "nostradamus_number":  {"id": 20, "name": "Nostradamus' Phone Number", "gates": [( 3,  1)]},
    "socrates_number":     {"id": 21, "name": "Socrates' Phone Number",    "gates": [( 6,  1)]},
    "mushroom_age_number": {"id": 22, "name": "Mushroom Age Phone Number", "gates": [( 8,  1)]},
}

PROGRESSION_ITEMS = {
    "progressive_elixir": ["elixir", "total_elixir"],
}

TRAP_ITEMS = {
    "main_menu": {"id": 30, "name": "Main Menu Trap"},
}

FILLER_ITEMS = ["Hourglass", "Mushroom Spores", "Photo of Professor Einbock's Wife"]

LEVEL_STRING = "level_{0:02}_{1:02}.lvl"