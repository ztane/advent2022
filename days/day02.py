from enum import Enum

from helpers import *

test_data = test_input(
    """
A Y
B X
C Z
"""
)

test_case(1, test_data, 15)
test_case(2, test_data, 12)


# make Enum of rock, papers, scissors
class RPS(Enum):
    rock = 1
    paper = 2
    scissors = 3


class Outcome(Enum):
    lose = 0
    tie = 3
    win = 6


rps_symbols = {
    "A": RPS.rock,
    "B": RPS.paper,
    "C": RPS.scissors,
    "X": RPS.rock,
    "Y": RPS.paper,
    "Z": RPS.scissors,
}

outcome_symbols = {
    "X": Outcome.lose,
    "Y": Outcome.tie,
    "Z": Outcome.win,
}

result_table: Dict[Tuple[RPS, RPS], Outcome] = {
    (RPS.rock, RPS.rock): Outcome.tie,
    (RPS.rock, RPS.paper): Outcome.lose,
    (RPS.rock, RPS.scissors): Outcome.win,
    (RPS.paper, RPS.rock): Outcome.win,
    (RPS.paper, RPS.paper): Outcome.tie,
    (RPS.paper, RPS.scissors): Outcome.lose,
    (RPS.scissors, RPS.rock): Outcome.lose,
    (RPS.scissors, RPS.paper): Outcome.win,
    (RPS.scissors, RPS.scissors): Outcome.tie,
}

# what I need to choose so that the outcome is what I want
# (other, outcome) -> me, i.e. (rock, win) -> paper...
choice_table: Dict[Tuple[RPS, Outcome], RPS] = {}

for (my_choice, others_choice), resulting_outcome in result_table.items():
    choice_table[others_choice, resulting_outcome] = my_choice


def part1(d: Input, ans: Answers) -> None:
    score = 0

    for other, me in d.parsed_lines("<> <>"):
        other = rps_symbols[other]
        me = rps_symbols[me]

        outcome = result_table[me, other]
        score += outcome.value
        score += me.value

    ans.part1 = score


def part2(d: Input, ans: Answers) -> None:
    score = 0

    for other, outcome in d.parsed_lines("<> <>"):
        other = rps_symbols[other]
        outcome = outcome_symbols[outcome]

        me = choice_table[other, outcome]
        score += outcome.value
        score += me.value

    ans.part2 = score


run([1, 2], day=2, year=2022)
