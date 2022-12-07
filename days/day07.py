import os

from helpers import *

test_data = test_input(
    """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
)

test_case(1, test_data, 95437)
test_case(2, test_data, 24933642)


def part1_and_2(d: Input, ans: Answers) -> None:
    it = fancyseqiter(d.lines)
    dir_tuple: Tuple[str, ...] = ()
    directory_sizes: Dict[Tuple[str, ...], int] = Counter()

    for i in it:
        if i.startswith("$ cd "):
            new_dir = i[5:]
            if new_dir == "/":
                dir_tuple = ()
            elif new_dir == "..":
                dir_tuple = dir_tuple[:-1]
            else:
                dir_tuple += (new_dir,)

        elif i == "$ ls":
            for j in it:
                if j.startswith("$"):
                    it.back()
                    break
                if j.startswith("dir "):
                    continue
                else:
                    file_size = int(j.split()[0])
                    for i in range(0, len(dir_tuple) + 1):
                        directory_sizes[dir_tuple[:i]] += file_size
        else:
            raise Exception("Unknown command {}".format(i))

    ans.part1 = 0
    for k, v in directory_sizes.items():
        if v < 100000:
            ans.part1 += v

    total_diskspace = 70000000
    total_used = directory_sizes[()]
    required_diskspace = 30000000
    need_to_free = required_diskspace - total_diskspace + total_used

    for i in sorted(directory_sizes.values()):
        if need_to_free <= i:
            ans.part2 = i
            break


run([1, 2], day=7, year=2022)
