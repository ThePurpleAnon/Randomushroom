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
    "elixir":        {"name": "Progressive Elixir of Understanding", "pool_name": "progressive_elixir", "gates": [( 4,  2), ( 5,  1)]},
    "total_elixir":  {"name": "Progressive Elixir of Understanding", "pool_name": "progressive_elixir", "gates": [(22,  3)]},
    "painting":      {"name": "Professor's Painting",                "gates": [( 7,  2)]},
    "timequake":     {"name": "Timequake",                           "gates": [( 9,  1), (10,  1), (11,  1), (13,  1), (14,  1), (15,  1), (16,  1)]},
    "toilet":        {"name": "Toilet Time Machine",                 "gates": [(12,  1)]},
    "mushroom_soup": {"name": "Mushroom Soup",                       "gates": [(23,  1)]},
}

KEY_QUESTS = {
    "professor_hope": {"name": "Gave Professor Einbock Hope That His Wife May Return", "task": ( 7,  4), "gates": [(23,  1)]},
    "tom_return":     {"name": "Returned Tom Safely to 2008",                          "task": (13,  5), "gates": [(23,  1)]},
    "uber_mushroom":  {"name": "Appeased the Über-Mushroom",                           "task": (22,  3), "gates": [(23,  1)]},
    "victory":        {"name": "Got Married to Tom Scout",                             "task": (23,  2), "gates": []},
}

KEY_PHONE_NUMBERS = {
    "nostradamus_number":  {"name": "Nostradamus' Phone Number", "gates": [( 3,  1)]},
    "socrates_number":     {"name": "Socrates' Phone Number",    "gates": [( 6,  1)]},
    "mushroom_age_number": {"name": "Mushroom Age Phone Number", "gates": [( 8,  1)]},
}

PROGRESSION_ITEMS = {
    "progressive_elixir": ["elixir", "total_elixir"],
}

LEVEL_STRING = "level_{0:02}_{1:02}"