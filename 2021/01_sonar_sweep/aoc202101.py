import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split("\n")]


def parse_window_fn(puzzle_input):
    """Parse input using a sliding window function"""
    parse_window = []
    for i in range(len(puzzle_input) - 2):
        new_num = puzzle_input[i] + puzzle_input[i + 1] + puzzle_input[i + 2]
        parse_window.append(new_num)
    return parse_window


def part1(data):
    """Solve part 1"""
    measurement_increases = 0
    for i in range(len(data) - 1):
        if data[i + 1] > data[i]:
            measurement_increases += 1
    return measurement_increases


def part2(data):
    """Solve part 2"""
    new_data = parse_window_fn(data)
    return part1(new_data)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
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
