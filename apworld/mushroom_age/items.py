from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .game_constants import *
from .rules import create_gate_dict

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
    key_item_pool = []

    all_items = KEY_ITEMS.copy()

    if world.options.region_gates: # if extra region locks are included in the pool
        all_items += KEY_REGION_ITEMS

    gate_dict = create_gate_dict(world, set_goal = False)
    starting_spots = 0
    ideal_start = None
    for gates in gate_dict.values():
        if gates == []:
            starting_spots += 1
        elif gates != [(0, 0)] and ideal_start is None:
            ideal_start = gates

    # if player doesn't have enough tasks at the start, give them enough items for the first task they can reach
    if ideal_start is not None and starting_spots < len(ideal_start):
        for item_id, item_amt in ideal_start:
            if item_id not in all_items: continue
            for _ in range(item_amt):
                all_items.remove(item_id)
                item_name = GAME_ITEMS[item_id]["name"]
                item = world.create_item(item_name)
                world.multiworld.push_precollected(item)

    for item in all_items:
        item_name = GAME_ITEMS[item]["name"]
        key_item_pool.append(world.create_item(item_name))
    
    world.random.shuffle(key_item_pool)

    number_of_items = len(key_item_pool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    item_pool = []

    victory_cond = world.options.victory_condition.current_key
    macguffins = VICTORY_CONDITIONS[victory_cond].get("macguffins")
    if macguffins is not None:
        macguffin_amount = min(world.options.macguffin_amount, max(needed_number_of_filler_items, 1))
        world.total_macguffin_amount = macguffin_amount

        item_pool.extend([world.create_item(GAME_ITEMS[macguffins]["name"]) for _ in range(macguffin_amount)])
        needed_number_of_filler_items -= macguffin_amount
    
    item_pool.extend(key_item_pool)

    # if there are too many items for the number of locations, just give the extras to the player outright
    while number_of_unfilled_locations < len(item_pool):
        world.multiworld.push_precollected(item_pool.pop())

    item_pool.extend([world.create_filler() for _ in range(needed_number_of_filler_items)])

    world.multiworld.itempool += item_pool