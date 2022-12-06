import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    strat_guide = []
    round = ""
    for char in puzzle_input.strip("\n"):
        if char.isalpha():
            round += char
        if len(round) == 2:
            strat_guide.append(round)
            round = ""

    return strat_guide


def part1(strat_guide):
    """Solve part 1.

    Rock = (A, X), Paper = (B, Y), Scissor = (C, Z)
    """

    def calculate_score(round):
        score_shape = {"X": 1, "Y": 2, "Z": 3}  # Rock, Paper, Scissor
        score_outcome = {
            # Rock outcomes
            "CX": 6,
            "AX": 3,
            "BX": 0,
            # Paper outcomes
            "AY": 6,
            "BY": 3,
            "CY": 0,
            # Scissor outcomes
            "BZ": 6,
            "CZ": 3,
            "AZ": 0,
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
