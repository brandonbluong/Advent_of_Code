import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1. Calculate each subroutine and return if unique."""

    first_marker_index = []

    for signal in data:
        first_marker = 4
        while first_marker < len(signal):
            subroutine = signal[first_marker - 4 : first_marker]
            if len(set(subroutine)) == 4:
                first_marker_index.append(first_marker)
                break
            first_marker += 1

    return first_marker_index


def part2(data):
    """Solve part 2."""
    first_marker_index = []

    for signal in data:
        first_marker = 14
        while first_marker < len(signal):
            subroutine = signal[first_marker - 14 : first_marker]
            if len(set(subroutine)) == 14:
                first_marker_index.append(first_marker)
                break
            first_marker += 1

    return first_marker_index


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
