import pathlib
import pytest
import main

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return main.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example):
    """Test that input is parsed properly."""
    assert example[0] == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example2(example):
    """Test that input is parsed properly."""
    assert example[1] == "bvwbjplbgvbhsrlpgdmjqwftvncz"


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example3(example):
    """Test that input is parsed properly."""
    assert example[2] == "nppdvjthqldpwncqszvftbrmjlhg"


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example4(example):
    """Test that input is parsed properly."""
    assert example[3] == "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example5(example):
    """Test that input is parsed properly."""
    assert example[4] == "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example(example):
    """Test part 1 on example input."""
    assert main.part1(example) == [7, 5, 6, 10, 11]


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example(example):
    """Test part 2 on example input."""
    assert main.part2(example) == ...
