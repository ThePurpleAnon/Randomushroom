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
    set_gates(world)

def set_gates(world: MushroomAgeWorld) -> None:
    gate_dict = create_gate_dict(world)

    for task_key, gates in gate_dict.items():
        if task_key == -1:
            task = None
        else:
            task = (
                (task_key // CH_MULT) + 1,
                (task_key % CH_MULT) + 1
            )

        if gates == [(0, 0)]: continue

        rules_list = []
        for rule_tuple in gates:
            rules_list.append(Has(GAME_ITEMS[rule_tuple[0]]["name"], count = rule_tuple[1]))

            rule = reduce(operator.and_, rules_list)

            if task is None:
                world.set_completion_rule(rule)
            else:
                location = world.get_location(LOCATION_NAME_STRING.format(*task))
                world.set_rule(location, rule)

                if task in BONUS_ITEM_TASKS:
                    location = world.get_location(LOCATION_NAME_STRING_BONUS.format(*task))
                    world.set_rule(location, rule)

                victory_cond = world.options.victory_condition.current_key
                use_quests = VICTORY_CONDITIONS[victory_cond]["use_quests"]
                if use_quests:
                    for quest_task in KEY_QUESTS.values():
                        if task != quest_task: continue
                        location = world.get_location(LOCATION_NAME_STRING_QUEST.format(*quest_task))
                        world.set_rule(location, rule)


def create_gate_dict(world: MushroomAgeWorld, set_goal: bool = True) -> dict[int, list]:
    gatekeepers = KEY_ITEMS.copy()

    if world.options.region_gates: # if extra region locks are included in the pool
        gatekeepers += KEY_REGION_ITEMS

    victory_cond = world.options.victory_condition.current_key
    use_quests = VICTORY_CONDITIONS[victory_cond]["use_quests"]
    if use_quests:
        gatekeepers += list(KEY_QUESTS.keys())

    gate_dict = {}

    for period in REGIONS.values():
        gates = []
        for chapter in period["chapters"]:
            for task in TASK_IDS:
                if chapter != task[0]: continue

                for item_gate_id, task_gates in GAME_GATES.items():
                    if item_gate_id[0] not in gatekeepers: continue

                    if task in task_gates:
                        gates.append(item_gate_id)
                
                task_is_required = use_quests and task in KEY_QUESTS.values()

                task_key = (task[0] - 1) * CH_MULT + (task[1] - 1)
                if str(chapter) in world.options.blocked_chapters and not task_is_required:
                    gate_dict[task_key] = [(0, 0)] # "this task is blocked"
                elif str(chapter) in world.options.blocked_chapters and task_is_required:
                    gate_dict[task_key] = []
                else:
                    gate_dict[task_key] = gates.copy()

    if not set_goal:
        return gate_dict

    # set completion rule
    gate_dict[-1] = []
    for item, item_amt in VICTORY_CONDITIONS[victory_cond].get("items", []):
        gate_dict[-1].append([item, item_amt])
    
    macguffins = VICTORY_CONDITIONS[victory_cond].get("macguffins")
    if macguffins is not None:
        macguffin_amt = max(1, round(world.total_macguffin_amount * (world.options.macguffin_percent / 100)))
        gate_dict[-1].append([macguffins, macguffin_amt])
        

    return gate_dict