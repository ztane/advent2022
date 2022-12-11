from helpers import *

test_data = test_input(
    """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
)

test_case(1, test_data, 10605)
test_case(2, test_data, 2713310158)


def solve(d: Input, iterations: int, worry_divisor: int) -> int:
    monkey_items = {}
    monkey_funcs = []
    counts = Counter()

    def make_monkey_func(n, operation, test, if_true, if_false):
        op_func_src = f"def op_func(old): return {operation}"
        scope = {}
        exec(op_func_src, globals(), scope)
        op_func = scope['op_func']

        def monkey():
            while monkey_items[n]:
                item = monkey_items[n].pop(0)
                new_item = op_func(item)
                new_item //= worry_divisor
                new_item %= max_modulo
                if new_item % test == 0:
                    monkey_items[if_true].append(new_item)
                else:
                    monkey_items[if_false].append(new_item)
                counts[n] += 1

        return monkey

    max_modulo = 1
    for n, monkey_instructions in enumerate(d.paragraphs()):
        monkey_instructions = monkey_instructions.lines
        starting_items = [int(i) for i in monkey_instructions[1].split(": ")[1].split(", ")]
        monkey_items[n] = starting_items
        operation = monkey_instructions[2].split("= ")[1]
        divisibility = monkey_instructions[3].as_ints[0]
        if_true = monkey_instructions[4].as_ints[0]
        if_false = monkey_instructions[5].as_ints[0]

        monkey_funcs.append(make_monkey_func(n, operation, divisibility, if_true, if_false))
        max_modulo *= divisibility

    for i in range(iterations):
        for monkey_func in monkey_funcs:
            monkey_func()

    return prod([i[1] for i in counts.most_common(2)])


def part1_and_2(d: Input, ans: Answers) -> None:
    ans.part1 = solve(d, 20, 3)
    ans.part2 = solve(d, 10000, 1)


run([1, 2], day=11, year=2022)
