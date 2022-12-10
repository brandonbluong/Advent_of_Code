import pathlib
import sys
from collections import deque


def parse(puzzle_input):
    """Parse input."""
    for line in puzzle_input.split("\n"):
        print(line)
    # [int(line) for line in puzzle_input.split("\n")]
    stack_1 = deque("ZN")
    stack_2 = deque("MCD")
    stack_3 = deque("PZ")
    return stack_1, stack_2, stack_3


def part1(data):
    """Solve part 1."""
    return ...


def part2(data):
    """Solve part 2."""
    return ...


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
