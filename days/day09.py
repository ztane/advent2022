from helpers import *

test_data = test_input(
    """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
)

test_case(1, test_data, 13)
test_case(2, test_data, 1)
test_case(
    2,
    test_input(
        """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
    ),
    36,
)


def part1_and_2(d: Input, ans: Answers) -> None:
    knots = [0] * 10

    visited_p1 = set()
    visited_p1.add(0)
    visited_p2 = set()
    visited_p2.add(0)

    for x in d.parsed_lines("<> <int>"):
        move_dir, move_dist = x
        for _ in range(move_dist):
            knots[0] += cdir.plane(move_dir)

            for i in range(1, 10):
                while cinf_norm(knots[i - 1] - knots[i]) > 1:
                    knots[i] += cdir.one_step_towards(knots[i], knots[i - 1])

            visited_p2.add(knots[-1])
            visited_p1.add(knots[1])

    ans.part1 = len(visited_p1)
    ans.part2 = len(visited_p2)


run([1, 2], day=9, year=2022, submit=True)
