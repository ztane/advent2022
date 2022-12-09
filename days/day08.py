from helpers import *

test_data = test_input(
    """\n
30373
25512
65332
33549
35390
"""
)

test_case(1, test_data, 21)
test_case(2, test_data, 8)


def part1(d: Input, ans: Answers) -> None:
    map = SparseComplexMap(d.lines, convert=int, default=None)

    seeds = set(
        [
            *[i for i in range(map.columns)],
            *[i * 1j for i in range(map.rows)],
            *[i + (map.rows - 1) * 1j for i in range(map.columns)],
            *[i * 1j + map.columns - 1 for i in range(map.rows)],
        ]
    )
    visible = set(seeds)

    def generate_visibility(direction):
        for c in seeds:
            max_so_far = map[c]
            while True:
                c += direction
                if (v := map[c]) is None:
                    break

                if v > max_so_far:
                    visible.add(c)
                    max_so_far = v

    for direction in [-1, 1, -1j, 1j]:
        generate_visibility(direction)

    print(visible)
    ans.part1 = len(visible)


def part2(d: Input, ans: Answers) -> None:
    map = SparseComplexMap(d.lines, convert=int, default=None)
    seeds = {
        *[i for i in range(map.columns)],
        *[i * 1j for i in range(map.rows)],
        *[i + (map.rows - 1) * 1j for i in range(map.columns)],
        *[i * 1j + map.columns - 1 for i in range(map.rows)],
    }
    edges = set(seeds)

    def calculate_scenic_score(start_pos: complex):
        start_v = map[start_pos]
        scores = []
        for direction in [1, -1, 1j, -1j]:
            pos = start_pos
            for dist in count(1):
                pos += direction
                if (v := map[pos]) is None:
                    scores.append(dist - 1)
                    break
                if v >= start_v:
                    scores.append(dist)
                    break

        total = prod(scores)
        if total == 9:
            print(pos, scores, start_v, v)
        return total

    scenic_score = 0

    for pos in list(map):
        if pos in edges:
            continue
        scenic_score = max(calculate_scenic_score(pos), scenic_score)

    ans.part2 = scenic_score


run([1, 2], day=8, year=2022, submit=True)
