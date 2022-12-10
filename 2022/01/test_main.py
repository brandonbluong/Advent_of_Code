import pathlib
import pytest
import main

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return main.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly.

    A blank line is represented with a 0. No food should be listed with 0 calories."""
    assert example == [
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


def test_part1_example(example):
    """Test part 1 on example input."""
    assert main.part1(example) == 24000


def test_part2_example(example):
    """Test part 2 on example input."""
    assert main.part2(example) == 45000
