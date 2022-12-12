from helpers import *

test_data = test_input(
    """\n
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
)

test_case(1, test_data, 31)
test_case(2, test_data, 29)


def part1(d: Input, ans: Answers) -> None:
    the_map = SparseComplexMap(d.lines, convert=lambda x: ord(x) - ord('a'))
    start = end = 0
    for i in the_map:
        if the_map[i] == ord('S') - ord('a'):
            start = i
        if the_map[i] == ord('E') - ord('a'):
            end = i

    the_map[start] = 0
    the_map[end] = ord('z') - ord('a')

    def filter_neighbours(x):
        from_ = the_map[x]
        for i in [1, -1, 1j, -1j]:
            if the_map[x + i] is None:
                continue

            if the_map[x + i] - from_ <= 1:
                yield 1, x + i

    distance, nodes = a_star_solve(
        start,
        target=end,
        neighbours=filter_neighbours,
        heuristic=lambda x, y: cmanhattan(x - y),
    )

    ans.part1 = distance


def part2(d: Input, ans: Answers) -> None:
    the_map = SparseComplexMap(d.lines, convert=lambda x: ord(x) - ord('a'))
    start = end = 0
    for i in the_map:
        if the_map[i] == ord('S') - ord('a'):
            start = i
            the_map[start] = 0
        if the_map[i] == ord('E') - ord('a'):
            end = i
            the_map[end] = ord('z') - ord('a')

    def filter_neighbours(x):
        from_ = the_map[x]
        for i in [1, -1, 1j, -1j]:
            if the_map[x + i] is None:
                continue

            if the_map[x + i] - from_ <= 1:
                yield 1, x + i

    possible_starts = [i for i in the_map if the_map[i] == 0]

    lowest_distance = 10000
    for s in possible_starts:
        d_nodes = a_star_solve(
            s,
            target=end,
            neighbours=filter_neighbours,
            max_distance=lowest_distance - 1,
            heuristic=lambda x, y: cmanhattan(x - y),
        )
        if isinstance(d_nodes, tuple):
            distance, nodes = d_nodes
            lowest_distance = distance

    ans.part2 = lowest_distance


run([1, 2], day=12, year=2022)
