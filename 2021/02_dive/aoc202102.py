"""Main file for Day 2: Dive """
import pathlib
import sys


def parse(puzzle_in):
    """Parse input"""
    parsed_direction = []
    for line in puzzle_in.split("\n"):
        letter = line[0]
        num = int(line[-1])
        if letter == "d":
            parsed_direction.append((0, num))  # (horizontal_position, depth)
        elif letter == "u":
            parsed_direction.append((0, -num))
        else:
            parsed_direction.append((num, 0))
    return parsed_direction


def parse_with_aim(puzzle_in):
    """Parse input to include aim"""
    aim = 0
    parsed_direction = []
    for line in puzzle_in.split("\n"):
        letter = line[0]
        num = int(line[-1])
        if letter == "d":
            aim += num
        elif letter == "u":
            aim -= num
        else:
            parsed_direction.append((num, aim * num))
    return parsed_direction


def part1(data):
    """Solve part 1"""
    horizontal_position = 0
    depth = 0
    for direction in data:
        horizontal_position += direction[0]
        depth += direction[1]
    return horizontal_position * depth


def part2(data):
    """Solve part 2"""
    return part1(data)


def solve(puzzle_inputs):
    """Solve the puzzle for the given input"""
    data1 = parse(puzzle_inputs)
    data2 = parse_with_aim(puzzle_inputs)
    solution1 = part1(data1)
    solution2 = part2(data2)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text("utf-8").strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
