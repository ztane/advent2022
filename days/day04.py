from helpers import *

test_data = test_input(
    """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
)

test_case(1, test_data, 2)
test_case(2, test_data, 4)


def part1(d: Input, ans: Answers) -> None:
    score = 0
    for a, b, c, d in d.parsed_lines("<int>-<int>,<int>-<int>"):
        if interval(a, b).either_fully_contains_other(interval(c, d)):
            score += 1

    ans.part1 = score


def part2(d: Input, ans: Answers) -> None:
    score = 0
    for a, b, c, d in d.parsed_lines("<int>-<int>,<int>-<int>"):
        if interval(a, b).overlaps(interval(c, d)):
            score += 1

    ans.part2 = score


run([1, 2], day=4, year=2022)
