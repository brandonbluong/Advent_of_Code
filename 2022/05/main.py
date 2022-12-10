import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    example_crates = list("ZN"), list("MCD"), list("P")
    move_set = []
    for line in puzzle_input.split("\n"):
        if line and line[0] == "m":
            directions = line.split(" ")
            move = (int(directions[1]), int(directions[3]), int(directions[5]))
            move_set.append(move)

    return (example_crates, move_set)


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
