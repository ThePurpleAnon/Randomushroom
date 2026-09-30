from __future__ import annotations

import operator
from functools import reduce
from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .game_constants import *

if TYPE_CHECKING:
    from .world import MushroomAgeWorld


def set_all_rules(world: MushroomAgeWorld) -> None:
    set_gates(world, return_dict = False)

def set_gates(world, return_dict):
    gatekeepers = KEY_ITEMS | KEY_QUESTS

    if world.options.phone_numbers: # if phone numbers are in the pool
        gatekeepers |= KEY_PHONE_NUMBERS

    gate_dict = {}
    name_or_id = "id" if return_dict else "name"

    for period in TIME_PERIODS.values():
        gates = []
        for chapter in period["chapters"]:
            for task in TASK_IDS:
                if chapter != task[0]: continue

                for gatekeeper_key, gatekeeper_dict in gatekeepers.items():
                    if task in gatekeeper_dict.get("gates", []):
                        pool_name = gatekeeper_dict.get("pool_name")
                        if pool_name is not None:
                            count = PROGRESSION_ITEMS[pool_name].index(gatekeeper_key) + 1
                            gates.append([gatekeeper_dict[name_or_id], count])
                        else:
                            gates.append([gatekeeper_dict[name_or_id], 1])

                rules_list = []

                if len(gates) == 0:
                    if not return_dict:
                        continue

                if return_dict: # if returning a dict
                    gate_dict[(task[0] - 1) * 100 + (task[1] - 1)] = list(gates)
                    continue
                else: # if setting locations for world
                    for rule in gates:
                        rules_list.append(Has(rule[0], count = rule[1]))

                rule = reduce(operator.and_, rules_list)

                location = world.get_location(LOCATION_NAME_STRING.format(*task))
                world.set_rule(location, rule)

                if task in BONUS_ITEM_TASKS:
                    location = world.get_location(LOCATION_NAME_STRING_BONUS.format(*task))
                    world.set_rule(location, rule)

                for quest in KEY_QUESTS.values():
                    if task != quest["task"]: continue
                    location = world.get_location(LOCATION_NAME_STRING_QUEST.format(*task))
                    world.set_rule(location, rule)

    # set completion rule
    item_name_or_id = "id" if return_dict else "name"

    item = KEY_QUESTS["victory"][item_name_or_id]
    item_amt = 1

    if return_dict: # if returning a dict
        # gate_dict key -1 is reserved for win conditions
        gate_dict[-1] = [[item, item_amt]]
    else: # if setting locations for world
        world.set_completion_rule(Has(item, count = item_amt))

    if return_dict:
        return gate_dict


def create_gate_dict(world):
    return set_gates(world, return_dict = True)