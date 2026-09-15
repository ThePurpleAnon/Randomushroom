from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .game_info.key_constants import *

if TYPE_CHECKING:
    from .world import MushroomAgeWorld


def set_all_rules(world: MushroomAgeWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: MushroomAgeWorld) -> None:
    phone_gates = ["nostradamus", "socrates", "mushroom_age"]
    for location in phone_gates:
        phone_gate = f"Title Screen to {TIME_PERIODS[location]["name"]}"
        phone_item = KEY_PHONE_NUMBERS[f"{location}_number"]["name"]
        world.set_rule(phone_gate, Has(phone_item))

    wedding_gate_0 = KEY_QUESTS["professor_hope"]["name"]
    wedding_gate_1 = KEY_QUESTS["tom_return"]["name"]
    wedding_gate_2 = KEY_QUESTS["uber_mushroom"]["name"]

    world.set_rule(f"Title Screen to {TIME_PERIODS["wedding"]["name"]}", HasAll(wedding_gate_0, wedding_gate_1, wedding_gate_2))

def set_all_location_rules(world: MushroomAgeWorld) -> None:
    for period in TIME_PERIODS.values():
        gates = []
        for chapter in period_dict["chapters"]:
            for task in TASK_IDS:
                if chapter != task[0]: continue

                for gatekeeper_key, gatekeeper in KEY_ITEMS.items():
                    if task in gatekeeper_dict["gates"]:
                        pool_name = gatekeeper.get("pool_name")
                        if pool_name is not None:
                            count = PROGRESSION_ITEMS[pool_name].index(gatekeeper_key) + 1
                            gates.append([gatekeeper["name"], count])
                        else:
                            gates.append(gatekeeper["name"])

                match len(gates):
                    case 0: continue
                    case 1: rule = Has(gates[0])
                    case _: rule = HasAll(*gates)

                    location = world.get_location(LOCATION_NAME_STRING.format(task))
                    world.set_rule(location, rule)

                    if task in BONUS_ITEM_TASKS:
                        location = world.get_location(LOCATION_NAME_STRING_BONUS.format(task))
                        world.set_rule(location, rule)

def set_completion_condition(world: MushroomAgeWorld) -> None:
    world.set_completion_rule(Has(KEY_QUESTS["victory"]["name"]))