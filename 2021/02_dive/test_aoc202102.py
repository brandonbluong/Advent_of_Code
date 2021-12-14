"""Test file for Day 2: Dive """
import pathlib
import pytest
import aoc202102 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    """Parses example1"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    """Parses example1 to include aim"""
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_with_aim(puzzle_input)


def test_parse_example1(example_1):
    """Test that input is parsed properly"""
    assert example_1 == [(5, 0), (0, 5), (8, 0), (0, -3), (0, 8), (2, 0)]


def test_part1_example1(example_1):
    """Test part 1 on example input"""
    assert aoc.part1(example_1) == 150


def test_parse_example2(example_2):
    """Test that input is parsed properly using window function"""
    assert example_2 == [(5, 0), (8, 40), (2, 20)]


def test_part2_example2(example_2):
    """Test part 2 on example input"""
    assert aoc.part2(example_2) == 900
