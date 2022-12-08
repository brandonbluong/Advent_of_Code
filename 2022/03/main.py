import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1."""
    from string import ascii_letters

    item_priority_sum = 0
    item_priority = dict(zip(ascii_letters, range(1, 53)))

    for line in data:
        compartment = set()
        # add first half letters to compartment
        for part_1 in line[: len(line) // 2]:
            compartment.add(part_1)
        # compare second half letters to compartment
        for part_2 in line[len(line) // 2 :]:
            if part_2 in compartment:
                item_priority_sum += item_priority[part_2]
                break

    return item_priority_sum


def part2(data):
    """Solve part 2.

    Each group is 3 lines. Create sets for each line within each group. Find the intersection and sum its priority score."""
    from string import ascii_letters

    item_priority = dict(zip(ascii_letters, range(1, 53)))
    item_priority_sum = 0
    group = []

    for rucksack in data:
        unique_item = set()
        for item in rucksack:
            unique_item.add(item)
        group.append(unique_item)
        if len(group) == 3:
            badge = group[0].intersection(group[1], group[2]).pop()
            item_priority_sum += item_priority[badge]
            group = []

    return item_priority_sum


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
