from helpers import *

test_data = test_input(
    """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
)

test_case(1, test_data, 7)
test_case(1, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10)
test_case(2, "mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19)


def part1_and_2(d: Input, ans: Answers) -> None:
    window1 = deque(maxlen=4)
    window2 = deque(maxlen=14)

    for i, c in enumerate(d, 1):
        window1.appendleft(c)
        window2.appendleft(c)

        if deque_full(window1) and all_unique(window1):
            ans.set_once(1, i)

        if deque_full(window2) and all_unique(window2):
            ans.set_once(2, i)


run([1, 2], day=6, year=2022, submit=True)
