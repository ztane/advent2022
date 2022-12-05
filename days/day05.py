from helpers import *

test_data = test_input(
    """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
)

test_case(1, test_data, "CMZ")
test_case(2, test_data, "MCD")


def part1_and_2(d: Input, ans: Answers) -> None:
    stacks, instructions = d.paragraphs()

    stacks = stacks.lines
    columns = stacks[-1].as_ints

    n_stacks = len(columns)

    part1_stacks = defaultdict(deque)
    part2_stacks = defaultdict(deque)
    for stack_number in columns:
        for row in stacks[:-1]:
            idx = (stack_number - 1) * 4 + 1
            if idx >= len(row):
                continue

            if (c := row[idx]) != ' ':
                part1_stacks[stack_number].append(c)
                part2_stacks[stack_number].append(c)

    for n_to_move, from_, to in instructions.parsed_lines(
        "move <int> from <int> to <int>"
    ):
        part2_temp_buffer = deque()
        for i in range(n_to_move):
            part2_temp_buffer.appendleft(part2_stacks[from_].popleft())
            part1_stacks[to].appendleft(part1_stacks[from_].popleft())

        part2_stacks[to].extendleft(part2_temp_buffer)

    # return string of top of each stack
    ans.part1 = ''.join(part1_stacks[stack][0] for stack in columns)
    ans.part2 = ''.join(part2_stacks[stack][0] for stack in columns)


run([1, 2], day=5, year=2022, submit=True)
