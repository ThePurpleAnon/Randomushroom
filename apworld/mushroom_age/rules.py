from __future__ import annotations

from functools import reduce
from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .randomushroom.key_constants import *

if TYPE_CHECKING:
    from .world import MushroomAgeWorld


def set_all_rules(world: MushroomAgeWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_location_rules(world: MushroomAgeWorld) -> None:
    gatekeepers = KEY_ITEMS | KEY_QUESTS | KEY_PHONE_NUMBERS

    for period in TIME_PERIODS.values():
        gates = []
        for chapter in period_dict["chapters"]:
            for task in TASK_IDS:
                if chapter != task[0]: continue

                for gatekeeper_key, gatekeeper in gatekeepers.items():
                    if task in gatekeeper_dict["gates"]:
                        pool_name = gatekeeper.get("pool_name")
                        if pool_name is not None:
                            count = PROGRESSION_ITEMS[pool_name].index(gatekeeper_key) + 1
                            gates.append([gatekeeper["name"], count])
                        else:
                            gates.append(gatekeeper["name"])

                if len(gates) == 0:
                    continue

                rules_list = []
                for rule in gates:
                    if isinstance(rule, list):
                        rules_list.append(Has(rule[0], count = rule[1]))
                    else:
                        rules_list.append(Has(rule))
                
                rule = reduce(operator.or_, rules_list)

                location = world.get_location(LOCATION_NAME_STRING.format(*task))
                world.set_rule(location, rule)

                if task in BONUS_ITEM_TASKS:
                    location = world.get_location(LOCATION_NAME_STRING_BONUS.format(*task))
                    world.set_rule(location, rule)

def set_completion_condition(world: MushroomAgeWorld) -> None:
    world.set_completion_rule(Has(KEY_QUESTS["victory"]["name"]))