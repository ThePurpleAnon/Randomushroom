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
    locations |= get_location_names_with_ids([{"task_id": quest["task"], "offset": None, "string": LOCATION_NAME_STRING_QUEST} for quest in KEY_QUESTS.values()])

    return locations


def get_location_names_with_ids(location_dicts: list[dict]) -> dict[str, int | None]:
    return_dict = {}

    for location in location_dicts:
        location_id = (location["task_id"][0]) * 1000 + (location["task_id"][1] * 10)
        return_dict[location["string"].format(*location["task_id"])] = None if location["offset"] is None else location_id + location["offset"]

    return return_dict


def create_all_locations(world: MushroomAgeWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: MushroomAgeWorld) -> None:
    chapter_regions = {}
    for time_period in TIME_PERIODS.values():
        region = world.get_region(time_period["name"])
        for chapter in time_period["chapters"]:
            chapter_regions[chapter] = region

    all_locations = location_names_to_ids()

    for task in TASK_IDS:
        region = chapter_regions[task[0]]
        locations = {}
        for name_string in [LOCATION_NAME_STRING, LOCATION_NAME_STRING_BONUS, LOCATION_NAME_STRING_QUEST]:
            location_name = name_string.format(*task)
            if location_name in all_locations:
                locations[location_name] = all_locations[location_name]

        region.add_locations(locations, MushroomAgeLocation)

def create_events(world: MushroomAgeWorld) -> None:
    for quest in KEY_QUESTS.values():
        quest_item = items.MushroomAgeItem(quest["name"], ItemClassification.progression, None, world.player)
        location = world.get_location(LOCATION_NAME_STRING_QUEST.format(*quest["task"]))

        location.place_locked_item(quest_item)


def create_event_dict(world):
    quest_dict = {}
    for quest in KEY_QUESTS.values():
        task = quest["task"]
        task_id = ((task[0] - 1) * 100) + (task[1] - 1)

        if task_id not in quest_dict:
            quest_dict[task_id] = []

        quest_dict[task_id].append(quest["id"])

    return quest_dict