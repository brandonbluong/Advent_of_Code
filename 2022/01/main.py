import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    parsed_input = [line for line in puzzle_input.split("\n")]
    for i, num in enumerate(parsed_input):
        if num == "":
            parsed_input[i] = 0
        else:
            parsed_input[i] = int(num)
    return parsed_input


def part1(food_list):
    """Solve part 1."""
    max_cal = 0
    current_cal = 0
    for cal in food_list:
        if cal:
            current_cal += cal
        else:
            if current_cal > max_cal:
                max_cal = current_cal
                current_cal = 0
    return max_cal


def part2(data):
    """Solve part 2."""


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
