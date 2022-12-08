import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    parsed = []
    for line in puzzle_input.split("\n"):
        parsed_pair = []
        for pair in line.split(","):
            parsed_range = [int(num) for num in pair.split("-")]
            parsed_pair.append(parsed_range)
        parsed.append(parsed_pair)

    return parsed


def part1(data):
    """Solve part 1.

    For each pair, one section has to be of smaller or equal length to be fully contained.

    (1): Find the smaller section
    (2): Smaller section's first number must be >= the other's first number
    (3): Smaller section's second number must be <= other's second number.
    """

    def find_smaller_section(pair):
        if len(range(pair[0][0], pair[0][1])) <= len(range(pair[1][0], pair[1][1])):
            return pair[0], pair[1]  # left is smaller
        return pair[1], pair[0]  # right is smaller

    def compare_nums(small, big):
        if small[0] >= big[0] and small[1] <= big[1]:
            return "fully contained"

    num_pairs = 0
    for pair in data:
        small, big = find_smaller_section(pair)
        if compare_nums(small, big):
            num_pairs += 1

    return num_pairs


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
