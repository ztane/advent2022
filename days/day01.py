import textwrap

from helpers import *


test_data = test_input(
    """
    1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000
    """
)

test_case(1, test_data, 24000)
test_case(2, test_data, 45000)


def part1(d: Input, ans: Answers) -> None:
    ans.part1 = max(
        (sum(elf.as_ints) for elf in d.paragraphs()),
    )


def part2(d: Input, ans: Answers) -> None:
    ans.part2 = sum(
        heapq.nlargest(
            3,
            (sum(elf.as_ints) for elf in d.paragraphs()),
        )
    )


run([1, 2], day=1, year=2022, submit=False)
