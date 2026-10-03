from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items
from .game_constants import *

if TYPE_CHECKING:
    from .world import MushroomAgeWorld


class MushroomAgeLocation(Location):
    game = "Mushroom Age"

def location_names_to_ids() -> dict[str, int | None]:
    locations = get_location_names_with_ids([{"task_id": task_id, "offset": 0, "string": LOCATION_NAME_STRING} for task_id in TASK_IDS])
    locations |= get_location_names_with_ids([{"task_id": task_id, "offset": 1, "string": LOCATION_NAME_STRING_BONUS} for task_id in BONUS_ITEM_TASKS])
    locations |= get_location_names_with_ids([{"task_id": task_id, "offset": None, "string": LOCATION_NAME_STRING_QUEST} for task_id in KEY_QUESTS.values()])

    return locations


def get_location_names_with_ids(location_dicts: list[dict]) -> dict[str, int | None]:
    return_dict = {}

    for location in location_dicts:
        location_id = (location["task_id"][0] * CH_MULT + location["task_id"][1]) * TK_MULT
        return_dict[location["string"].format(*location["task_id"])] = None if location["offset"] is None else location_id + location["offset"]

    return return_dict


def create_all_locations(world: MushroomAgeWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: MushroomAgeWorld) -> None:
    chapter_regions = {}
    for time_period in REGIONS.values():
        region = world.get_region(time_period["name"])
        for chapter in time_period["chapters"]:
            chapter_regions[chapter] = region

    all_locations = location_names_to_ids()

    for task in TASK_IDS:
        region = chapter_regions[task[0]]
        locations = {}

        location_strings = [LOCATION_NAME_STRING, LOCATION_NAME_STRING_BONUS]

        victory_cond = world.options.victory_condition.current_key
        use_quests = VICTORY_CONDITIONS[victory_cond]["use_quests"]
        if use_quests:
            location_strings.append(LOCATION_NAME_STRING_QUEST)

        for name_string in location_strings:
            location_name = name_string.format(*task)
            if location_name in all_locations:
                locations[location_name] = all_locations[location_name]

        use_location = False
        if str(task[0]) not in world.options.blocked_chapters:
            use_location = True
        elif use_quests and LOCATION_NAME_STRING_QUEST.format(*task) in all_locations:
            use_location = True
        
        if use_location:
            region.add_locations(locations, MushroomAgeLocation)

def create_events(world: MushroomAgeWorld) -> None:
    event_dict = create_event_dict(world)

    for task_key, quest_items in event_dict.items():
        for item in quest_items:
            item_name = GAME_ITEMS[item]["name"]
            quest_item = items.MushroomAgeItem(item_name, ItemClassification.progression, None, world.player)

            quest_task = (
                (task_key // CH_MULT) + 1,
                (task_key % CH_MULT) + 1
            )

            location = world.get_location(LOCATION_NAME_STRING_QUEST.format(*quest_task))
            location.place_locked_item(quest_item)


def create_event_dict(world: MushroomAgeWorld) -> dict[int, list]:
    quest_dict = {}

    victory_cond = world.options.victory_condition.current_key
    use_quests = VICTORY_CONDITIONS[victory_cond]["use_quests"]
    if use_quests:
        for quest_id, quest_task in KEY_QUESTS.items():
            task_id = (quest_task[0] - 1) * CH_MULT + (quest_task[1] - 1)

            if task_id not in quest_dict:
                quest_dict[task_id] = []

            quest_dict[task_id].append(quest_id)

    return quest_dict