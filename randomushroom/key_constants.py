TIME_PERIODS = {
    "lab_2008":      {"chapters": [ 1,  7,  9, 20]},
    "cemetary_3008": {"chapters": [ 2, 13, 17, 19]},
    "nostradamus":   {"chapters": [ 3, 11, 21]},
    "jurassic":      {"chapters": [ 4, 10]},
    "stone_age":     {"chapters": [ 5, 14]},
    "socrates":      {"chapters": [ 6, 15]},
    "mushroom_age":  {"chapters": [ 8, 16, 22]},
    "omniscient":    {"chapters": [12, 18]},
    "wedding":       {"chapters": [23]},
}

KEY_ITEMS = {
    "elixir":        {"pool_name": "progressive_elixir", "gates": [( 4,  2), ( 5,  1)]},
    "total_elixir":  {"pool_name": "progressive_elixir", "gates": [(22,  3)]},
    "painting":      {"gates": [( 7,  2)]},
    "timequake":     {"gates": [( 9,  1), (10,  1), (11,  1), (13,  1), (14,  1), (15,  1), (16,  1)]},
    "toilet":        {"gates": [(12,  1)]},
    "mushroom_soup": {"gates": [(23,  1)]},
}

KEY_QUESTS = {
    "professor_hope": {"task": ( 7,  4), "gates": [(23,  1)]},
    "tom_return":     {"task": (13,  5), "gates": [(23,  1)]},
    "uber_mushroom":  {"task": (22,  3), "gates": [(23,  1)]},
}

KEY_PHONE_NUMBERS = {
    "nostradamus_number":  {"gates": [( 3,  1)]},
    "socrates_number":     {"gates": [( 6,  1)]},
    "mushroom_age_number": {"gates": [( 8,  1)]},
}

PROGRESSION_ITEMS = {
    "progressive_elixir": ["elixir", "total_elixir"],
}