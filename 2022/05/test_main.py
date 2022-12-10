import pathlib
import pytest
import main
from collections import deque

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return main.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    """Test that input is parsed properly."""

    example_crates = ["Z", "N"], ["M", "C", "D"], ["P"]
    move_set = [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
    assert example == (example_crates, move_set)


@pytest.mark.skip(reason="Not implemented")
def test_part1_example(example):
    """Test part 1 on example input."""
    assert main.part1(example) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input."""
    assert main.part2(example) == ...
