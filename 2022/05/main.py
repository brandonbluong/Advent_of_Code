import pathlib
import sys
import copy


def parse(puzzle_input):
    """Parse input."""
    example_crates = list("ZN"), list("MCD"), list("P")

    input_crates = (
        list("BGSC"),
        list("TMWHJNVG"),
        list("MQS"),
        list("BSLTWNM"),
        list("JZFTVGWP"),
        list("CTBGQHS"),
        list("TJPBW"),
        list("GDCZFTQM"),
        list("NSHBPF"),
    )

    move_set = []
    for line in puzzle_input.split("\n"):
        if line and line[0] == "m":
            directions = line.split(" ")
            move = [int(directions[1]), int(directions[3]), int(directions[5])]
            move_set.append(move)

    return (example_crates, input_crates, move_set)


def part1(data):
    """Solve part 1."""

    def rearrange(crate_stack, move_set):
        for move in move_set:
            for step in range(move[0]):
                crate = crate_stack[move[1] - 1].pop()
                crate_stack[move[2] - 1].append(crate)

        return crate_stack

    data1 = copy.deepcopy(data)
    example_crates, input_crates, move_set = data1[0], data1[1], data1[2]

    if len(move_set) == 4:
        final_config = rearrange(example_crates, move_set)
    else:
        final_config = rearrange(input_crates, move_set)

    top_crates = ""

    for stack in final_config:
        top_crates += stack[-1]

    return top_crates


def part2(data):
    """Solve part 2."""

    def rearrange(crate_stack, move_set):

        for move in move_set:
            move_nums, move_from, move_to = move[0], move[1] - 1, move[2] - 1

            # create new list of last num of crates
            picked_crates = crate_stack[move_from][-move_nums:]

            # remove the picked_crates from from_crates
            for _ in range(move_nums):
                crate_stack[move_from].pop()

            # add picked_crates to the move_to pile
            crate_stack[move_to].extend(picked_crates)

        return crate_stack

    data2 = copy.deepcopy(data)
    example_crates, input_crates, move_set = data2[0], data2[1], data2[2]

    if len(move_set) <= 4:
        final_config = rearrange(example_crates, move_set)
    else:
        final_config = rearrange(input_crates, move_set)

    top_crates = ""

    for stack in final_config:
        top_crates += stack[-1]

    return top_crates


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
