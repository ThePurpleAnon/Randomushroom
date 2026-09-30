from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, DefaultOnToggle


class VictoryCondition(Choice):
    """
    Controls the conditions for goaling:
    Get Married -> Return Tom Scout home safely, return peace to the timeline, cheer up the professor, and get married to Tom.
    Collect Dinosaur Eggs -> Collect all of Dino's dino eggs that were scattered across the multiverse.
    """

    display_name = "Victory Condition"

    option_get_married = 0
    option_collect_dinosaur_eggs = 1

    default = option_get_married


class DinoEggAmount(Range):
    """
    Controls the amount of Dinosaur Eggs that are in the item pool if the victory condition is to collect dinosaur eggs.
    """

    display_name = "Amount of Dinosaur Eggs"

    range_start = 3
    range_end = 50
    default = 20


class DinoEggPercentage(Range):
    """
    Controls the percentage of Dinosaur Eggs that are required to beat the game if the victory condition is to collect dinosaur eggs.
    """

    display_name = "Dinosaur Eggs Required Percentage"

    range_start = 0
    range_end = 100
    default = 75


class PhoneNumbers(DefaultOnToggle):
    """
    Controls whether certain areas are gated behind phone number items that need to be collected before reaching those areas.
    """

    display_name = "Use Phone Numbers"


class TrapChance(Range):
    """
    Controls the percentage chance that any given filler item will be replaced by a trap item.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 0


@dataclass
class MushroomAgeOptions(PerGameCommonOptions):
    victory_condition: VictoryCondition
    egg_amount: DinoEggAmount
    egg_percent: DinoEggPercentage
    phone_numbers: PhoneNumbers
    trap_chance: TrapChance

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [VictoryCondition, DinoEggAmount, DinoEggPercentage, PhoneNumbers, TrapChance],
    ),
]