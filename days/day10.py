from more_itertools import chunked
from PIL import Image
import pytesseract

from helpers import *

test_data = test_input(
    """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
"""
)

data = """\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

test_case(1, test_data, 13140)
test_case(2, test_data, 'SUCCESS')


def part1_and_2(d: Input, ans: Answers) -> None:
    ans.part1 = 0
    x = 1
    n = 0
    output = ['.'] * 240
    for iteration, i in enumerate(d.lines, 0):
        # the delay slot for the addition
        to_add = None
        while True:
            n += 1
            # Find the signal strength during the 20th, 60th, 100th,
            # 140th, 180th, and 220th cycles. What is the sum of these
            # six signal strengths?
            if n in {20, 60, 100, 140, 180, 220}:
                ans.part1 += x * n

            px_pos = n - 1
            if (px_pos % 40) in {x - 1, x, x + 1}:
                output[px_pos] = '#'

            if to_add is not None:
                x += to_add
                to_add = None
                break

            if i.startswith("addx"):
                to_add = int(i[5:])
                continue

            elif i.startswith("noop"):
                break

            else:
                raise ValueError(i)

    answer_pixels = ''
    for i in chunked(output, 40):
        answer_pixels += ''.join(i) + '\n'
        print(''.join(i))

    # correct answer for test case but not for real data
    if answer_pixels == data:
        ans.part2 = 'SUCCESS'
    else:
        ans.part2 = ocr(answer_pixels, 40)


run([1, 2], day=10, year=2022)
