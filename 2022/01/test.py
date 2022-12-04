import pathlib
import pytest
import main

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return main.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return main.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly.

    A blank line is represented with a 0. No food should be listed with 0 calories."""
    assert example1 == [
        1000,
        2000,
        3000,
        0,
        4000,
        0,
        5000,
        6000,
        0,
        7000,
        8000,
        9000,
        0,
        10000,
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert main.part1(example1) == 24000


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert main.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert main.part2(example2) == ...
