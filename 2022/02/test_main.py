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
    "Uses example1.txt"
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return main.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [["A", "Y"], ["B", "X"], ["C", "Z"]]


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert main.part1(example1) == 15


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert main.part2(example1) == 45000
