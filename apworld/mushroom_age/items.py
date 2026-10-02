from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .game_constants import *

if TYPE_CHECKING:
    from .world import MushroomAgeWorld


class MushroomAgeItem(Item):
    game = "Mushroom Age"

def item_names_to_ids() -> dict[str, int]:
    items = {}

    for item_id, item_data in GAME_ITEMS.items():
        items[item_data["name"]] = item_id
    
    for i, item in enumerate(FILLER_ITEMS):
        items[item + FILLER_SUFFIX] = FILLER_ITEMS_ID + i

    return items


def get_random_filler_item_name(world: MushroomAgeWorld) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        trap = GAME_ITEMS[MAIN_MENU_TRAP]["name"]
        return trap

    item = world.random.choice(FILLER_ITEMS)
    return item + FILLER_SUFFIX

def create_item_with_correct_classification(world: MushroomAgeWorld, name: str) -> MushroomAgeItem:
    classification = ItemClassification.filler
    item_id = FILLER_ITEMS_ID

    for item_id_actual, item in GAME_ITEMS.items():
        if name != item["name"]: continue
        
        match item["type"]:
            case "filler":      classification = ItemClassification.filler
            case "progression": classification = ItemClassification.progression
            case "trap":        classification = ItemClassification.trap
            case "useful":      classification = ItemClassification.useful

        item_id = item_id_actual

    junk_name = name.removesuffix(FILLER_SUFFIX)
    if junk_name in FILLER_ITEMS:
        item_id += FILLER_ITEMS.index(junk_name)

    return MushroomAgeItem(name, classification, item_id, world.player)

def create_all_items(world: MushroomAgeWorld) -> None:
    item_pool = []

    all_items = KEY_ITEMS

    if world.options.phone_numbers: # if extra region locks are included in the pool
        all_items += KEY_REGION_ITEMS

    for item in all_items:
        item_name = GAME_ITEMS[item]["name"]
        print(item_name)
        item_pool.append(world.create_item(item_name))

    number_of_items = len(item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    victory_cond = world.options.victory_condition.current_key
    macguffins = VICTORY_CONDITIONS[victory_cond].get("macguffins")
    if macguffins is not None:
        egg_amount = min(world.options.egg_amount, needed_number_of_filler_items)
        world.dino_egg_amount = egg_amount

        item_pool.extend([world.create_item(GAME_ITEMS[macguffins]["name"]) for _ in range(egg_amount)])
        needed_number_of_filler_items -= egg_amount

    item_pool.extend([world.create_filler() for _ in range(needed_number_of_filler_items)])

    world.multiworld.itempool += item_pool