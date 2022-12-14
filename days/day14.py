import typing

from helpers import *

test_data = test_input(
    """\n
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
)

test_case(1, test_data, 24)
test_case(2, test_data, 93)


def form_map(d: Input) -> typing.Tuple[SparseComplexMap, int]:
    the_map = SparseComplexMap(default=0)
    max_y = 0
    for line in d.lines:
        points = [complex(*map(int, x.split(','))) for x in line.split(' -> ')]
        for start, end in pairwise(points):
            delta = cdir.one_step_towards(start, end)
            while start != end:
                the_map[start] = 1
                start += delta
                max_y = max(max_y, start.imag)
                the_map[start] = 1

    return the_map, max_y

def part1(d: Input, ans: Answers) -> None:
    the_map, max_y = form_map(d)

    grain_position = 500
    n_grains = 0
    while True:
        if not the_map[grain_position + 1j]:
            grain_position += 1j
        elif not the_map[grain_position - 1 + 1j]:
            grain_position += -1 + 1j
        elif not the_map[grain_position + 1 + 1j]:
            grain_position += 1 + 1j
        else:
            the_map[grain_position] = 1
            grain_position = 500
            n_grains += 1
            continue

        if grain_position.imag > max_y:
            break

    ans.part1 = n_grains


def part2(d: Input, ans: Answers) -> None:
    the_map, max_y = form_map(d)

    grain = 500
    n_grains = 0

    while True:
        if the_map[grain + 1j] == 0:
            grain += 1j
        elif the_map[grain - 1 + 1j] == 0:
            grain += -1 + 1j
        elif the_map[grain + 1 + 1j] == 0:
            grain += 1 + 1j
        else:
            the_map[grain] = 1
            n_grains += 1

            if grain == 500:
                break

            grain = 500
            continue

        if grain.imag == max_y + 1:
            the_map[grain] = 1
            grain = 500
            n_grains += 1
            continue

    ans.part2 = n_grains


run([1, 2], day=14, year=2022, submit=False)
