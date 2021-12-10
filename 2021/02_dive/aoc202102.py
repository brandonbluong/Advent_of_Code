with open("advent_day_2.txt") as d:
    directions = [line.strip() for line in d]


def part_one(puzzle_input):
    """Returns answer to part one"""
    horizontal_position = 0
    depth = 0

    for direction in puzzle_input:
        letter = direction[0]
        num = int(direction[-1])
        if letter == "d":
            depth += num
        elif letter == "u":
            depth -= num
        else:
            horizontal_position += num
    return horizontal_position * depth


print(part_one(directions))


def part_two(puzzle_input):
    """Returns answer to part 2"""
    horizontal_position = 0
    depth = 0
    aim = 0

    for direction in puzzle_input:
        letter = direction[0]
        num = int(direction[-1])
        if letter == "d":
            aim += num
        elif letter == "u":
            aim -= num
        else:
            horizontal_position += num
            depth += aim * num
    return horizontal_position * depth


print(part_two(directions))
