import functools

from helpers import *

test_data = test_input(
    """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""
)

test_case(1, test_data, 13)
test_case(2, test_data, 140)


def compare_recursive(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            if a != b:
                return -1 if a < b else 1
            return 0
        else:
            a = [a]
    elif isinstance(b, int):
        b = [b]

    for i in range(min(len(a), len(b))):
        if (rv := compare_recursive(a[i], b[i])) != 0:
            return rv

    return -1 if len(a) < len(b) else 1 if len(a) > len(b) else 0


def part1_and_2(d: Input, ans: Answers) -> None:
    ans.part1 = 0
    all_packets = []

    for idx, l in enumerate(d.paragraphs(), 1):
        a = eval(l.lines[0])
        b = eval(l.lines[1])

        if compare_recursive(a, b) <= 0:
            ans.part1 += idx

        all_packets.append(a)
        all_packets.append(b)

    all_packets.extend(([[2]], [[6]]))
    all_packets.sort(key=functools.cmp_to_key(compare_recursive))
    ans.part2 = (
        (all_packets.index([[2]]) + 1) *
        (all_packets.index([[6]]) + 1)
    )


run([1, 2], day=13, year=2022, submit=False)
