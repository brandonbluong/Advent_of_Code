import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    parsed = []
    row = []
    for char in puzzle_input:
        if char.isalpha():
            row.append(char)
        elif char == "\n":
            parsed.append(row)
            row = []
    if row:
        parsed.append(row)
    return parsed


def part1(strat_guide):
    """Solve part 1.

    Rock = (A, X), Paper = (B, Y), Scissor = (C, Z)
    """

    def calculate_score(round):
        score_shape = {"X": 1, "Y": 2, "Z": 3}
        score_outcome = {
            # TODO can't have list as a dict key
            # Rock outcomes
            ["C", "X"]: 6,
            ["A", "X"]: 3,
            ["B", "X"]: 0,
            # Paper outcomes
            ["A", "Y"]: 6,
            ["B", "Y"]: 3,
            ["C", "Y"]: 0,
            # Scissor outcomes
            ["B", "Z"]: 6,
            ["C", "Z"]: 3,
            ["A", "Z"]: 0,
        }
        return score_shape[round[1]] + score_outcome[round]

    total_score = 0
    for round in strat_guide:
        total_score += calculate_score(round)

    return total_score


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
