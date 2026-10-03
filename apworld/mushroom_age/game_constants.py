LOCATION_NAME_STRING = "Task {0}-{1}"
LOCATION_NAME_STRING_BONUS = "Task {0}-{1} Bonus Item"
LOCATION_NAME_STRING_QUEST = "Task {0}-{1} Quest"

REGIONS = {
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

GAME_ITEMS = {
     1: {"type": "progression", "name": "Progressive Elixir of Understanding"},
     2: {"type": "progression", "name": "Professor's Painting"},
     3: {"type": "progression", "name": "Timequake"},
     4: {"type": "progression", "name": "Toilet Time Machine"},
     5: {"type": "progression", "name": "Mushroom Soup"},
     6: {"type": "progression", "name": "Dinosaur Egg"},
     7: {"type": "progression", "name": "Nostradamus' Phone Number"},
     8: {"type": "progression", "name": "Socrates' Phone Number"},
     9: {"type": "progression", "name": "Mushroom Age Phone Number"},
    10: {"type": "progression", "name": "Give Professor Einbock Hope"},
    11: {"type": "progression", "name": "Return Tom Safely to 2008"},
    12: {"type": "progression", "name": "Appease the Über-Mushroom"},
    13: {"type": "progression", "name": "Find the Wedding Rings"},
    14: {"type": "progression", "name": "Get Married to Tom Scout"},
    15: {"type": "trap",        "name": "Main Menu Trap"},
}

GAME_GATES = [ # (item_id, item_amt): [(chapter_id, task_id), ...]
    # key item gates
    [( 1,  1), [( 4,  1), ( 5,  1)]],
    [( 1,  2), [(22,  1)]],
    [( 2,  1), [( 7,  1)]],
    [( 3,  1), [( 9,  1), (10,  1), (11,  1), (13,  1), (14,  1), (15,  1), (16,  1)]],
    [( 4,  1), [(12,  1)]],
    [( 5,  1), [(23,  1)]],
    # phone number gates
    [( 7,  1), [( 3,  1)]],
    [( 8,  1), [( 6,  1)]],
    [( 9,  1), [( 8,  1)]],
    # quest gates
    [(10,  1), [(23,  1)]],
    [(11,  1), [(23,  1)]],
    [(12,  1), [(23,  1)]],
    [(13,  1), [(23,  2)]],
]

KEY_QUESTS = {
    10: ( 7,  4),
    11: (13,  5),
    12: (22,  3),
    13: (23,  1),
    14: (23,  2),
}

MAIN_MENU_TRAP = 15
KEY_ITEMS = [1, 1, 2, 3, 4, 5]
KEY_REGION_ITEMS = [7, 8, 9]
VICTORY_CONDITIONS = {
    "get_married":           {"items": [(14, 1)], "use_quests": True},
    "collect_dinosaur_eggs": {"macguffins": 6,    "use_quests": False},
}

FILLER_ITEMS_ID = 16
FILLER_SUFFIX = " (Junk)"
FILLER_ITEMS = [
    # chapter 1 references
    "Handkerchief Soaked With Ammonium Chloride", "Picture of a Man Who Does Not Look Like the Professor's Wife",
    "Picture of the Professor's Wife", "Hourglass", "Stopwatch", "Rubber Plant",
    # chapter 2 references
    "Sledgehammer", "Cybernetics", "Tombstone Name Plate", "Hologram Box",
    # chapter 3 references (fun fact, all the zodiac images in the game's files are numbered, i.e. zodiak_9.tga etc, but they're still ordered according to alphabetical order rather than chronology)
    "Aquarius Zodiac", "Aries Zodiac", "Cancer Zodiac", "Capricorn Zodiac", "Gemini Zodiac", "Leo Zodiac",
    "Libra Zodiac", "Pisces Zodiac", "Sagittarius Zodiac", "Scorpius Zodiac", "Taurus Zodiac", "Virgo Zodiac",
    # chapter 4 references
    "String", "Toothbrush", "Rotten Tooth", "Birthday Cake", "Picture of Tom Scout",
    # chapter 5 references
    "Box of Matches", "Firewood", "Stone Ax", "Piece of Flint", "Piece of Dry Bark",
    # chapter 6 references
    "Large Letter Sigma", "Letter Omega", "Letter Kappa", "Letter Rho", "Letter Alpha", "Letter Tau", "Letter Eta", "Letter Sigma",
    # chapter 7 references
    "Piece of Cheese", "Professor's Pill", "Globe", "Starfish", "Vodka?", # unused 7-4 string
    # chapter 8 references
    "Pair of NevoShoes Sneakers", "Mushroom Spores", "Warning Note From Tom",
    # chapter 9 references
    "Fuse", "Rubber Gloves", "Regular Mobile Phone", "Satellite Dish", "Omelet From the Jurassic Period",
    # chapter 10 references
    "At Sign Zodiac", "Dollar Sign Zodiac", "Taijitu Zodiac", "NevoSoft Zodiac", "Mars Zodiac", "Venus Zodiac",
    # chapter 11 references
    "Picture of Napoleon Bonaparte", "Picture of Albert Einstein", "Picture of Abaraham Lincoln", "Picture of George Washington",
    "Picture of Dmitri Mendeleyev", "Picture of Karl Marx", "Picture of Genghis Khan", "Picture of the Dalai Lama",
    # chapter 12 references
    "System Error Log of the Universe", "Yellow Ball", "Red Ball", "God's Phone Number",
    # chapter 13 references
    "Number 7", "Drum", "Drumstick", "Saxophone", "Number 2", "Number 5", "Lowercase Letter T", "Piece of Ugu's Sacred Fang Necklace",
    # chapter 14 references
    "Cockroach", "Centipede", "Frog", "Bug", "Monkey", "Lizard", "Parrot", "Butterfly", "Spider", "Mouse", "Bat",
    # chapter 15 references
    "Loaned Money", "Clothes", "Money From the Palace", "Barrel of Wine",
    # chapter 16 references
    "Robo-checkers Ball", "Pair of Headphones", "Fax Machine", "Book", "Seashell", "Tiny Toadstool",
    # chapter 17 references
    "Toolbox", "Screwdriver", "Wirecutters", "Hammer",
    # chapter 18 references
    "Mirror", "Leonardo da Vinci's Mona Lisa Outfit",
    # chapter 19 references
    "Defective Duck-Shaped Annihilator", "Scotch Tape", "Piece of Hose", "Faucet Handle", "Piece of UM-21's Broken Motherboard",
    # chapter 20 references
    "Computer Game Disc", "Crudely Drawn Picture of a Car", "Crudely Drawn Picture of a Happy Face", "Crudely Drawn Picture of a House",
    # chapter 21 references
    "Picture of Alexander the Great", "Picture of Wolfgang Amadeus Mozart", "Picture of Arnold Schwarzenegger", "Picture of Talking Flower",
    "Ten of Hearts Card", "King of Spades Card", "King of Hearts Card", "Queen of Clubs Card",
    "Queen of Diamonds Card", "Jack of Spades Card", "Jack of Diamonds Card", "Joker Card",
    # chapter 22 references
    "Empty Bottle", "Edible Mushroom", "Poisonous Mushroom", "Sentient Mushroom",
    # chapter 23 references
    "Professor's Suit", "Shovel", "Manhole Cover", "Crowbar", "Kiwi", "Grapes", "Pear", "Watermelon", "Apple", "Banana", "Rose", "Advertisement",
]

CH_MULT = 6
TK_MULT = 2

TASK_IDS = [
    ( 1, 1), ( 1, 2), ( 1, 3),
    ( 2, 1), ( 2, 2), ( 2, 3), ( 2, 4),
    ( 3, 1), ( 3, 2), ( 3, 3), ( 3, 4),
    ( 4, 1), ( 4, 2), ( 4, 3), ( 4, 4), ( 4, 5), ( 4, 6),
    ( 5, 1), ( 5, 2), ( 5, 3), ( 5, 4),
    ( 6, 1), ( 6, 2), ( 6, 3), ( 6, 4),
    ( 7, 1), ( 7, 2), ( 7, 3), ( 7, 4),
    ( 8, 1), ( 8, 2), ( 8, 3),
    ( 9, 1), ( 9, 2), ( 9, 3), ( 9, 4), ( 9, 5),
    (10, 1), (10, 2), (10, 3), (10, 4),
    (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6),
    (12, 1), (12, 2), (12, 3),
    (13, 1), (13, 2), (13, 3), (13, 4), (13, 5),
    (14, 1), (14, 2), (14, 3), (14, 4),
    (15, 1), (15, 2), (15, 3),
    (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6),
    (17, 1),
    (18, 1), (18, 2), (18, 3),
    (19, 1), (19, 2), (19, 3),
    (20, 1), (20, 2), (20, 3), (20, 4),
    (21, 1), (21, 2), (21, 3),
    (22, 1), (22, 2), (22, 3),
    (23, 1), (23, 2),
]

BONUS_ITEM_TASKS = [
    ( 1, 3),
    ( 3, 4),
    ( 7, 3),
    ( 7, 4),
    ( 9, 3),
    (11, 1),
    (13, 2),
    (13, 4),
    (15, 1),
    (16, 4),
    (21, 3),
    (22, 3),
]