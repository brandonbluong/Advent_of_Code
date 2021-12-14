"""Main file for Day 3: Binary Diagnostic"""
import pathlib
import sys


def parse(puzzle_in):
    """Parse input"""
    return [line for line in puzzle_in.split("\n")]


def part1(data):
    """Solve part 1"""
    one_counter = [0 for _ in range(len(data[0]))]
    gamma_rate = ""
    epsilon_rate = ""
    for binary_num in data:
        for i, bit in enumerate(binary_num):
            if int(bit) == 1:
                one_counter[i] += 1
    for num in one_counter:
        if num / len(data) > 0.50:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(data):
    """Solve part 2"""
    pass


def solve(puzzle_in):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_in)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text("utf-8").strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
