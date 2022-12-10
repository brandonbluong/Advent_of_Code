import pathlib
import pytest
import main

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return main.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    """Test that input is parsed properly."""
    assert example == [
        [[2, 4], [6, 8]],
        [[2, 3], [4, 5]],
        [[5, 7], [7, 9]],
        [[2, 8], [3, 7]],
        [[6, 6], [4, 6]],
        [[2, 6], [4, 8]],
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example(example):
    """Test part 1 on example input."""
    assert main.part1(example) == 2


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input."""
    assert main.part2(example) == 4
