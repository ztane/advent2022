import string

from more_itertools import chunked

from helpers import *

test_data = test_input(
    """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
)

letters = string.ascii_letters

test_case(1, test_data, 157)
test_case(2, test_data, 70)


def part1(d: Input, ans: Answers) -> None:
    score = 0
    for l in d.lines:
        half = len(l) // 2
        left, right = l[:half], l[half:]
        shared = intersection([left, right])
        for i in shared:
            score += letters.index(i) + 1

    ans.part1 = score


def part2(d: Input, ans: Answers) -> None:
    score = 0
    for chunk in chunked(d.lines, 3):
        shared = intersection(chunk)
        for i in shared:
            score += letters.index(i) + 1

    ans.part2 = score


run([1, 2], day=3, year=2022)
