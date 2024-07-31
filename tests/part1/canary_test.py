# test_sample.py
import pytest
from units.part1.canary_problem import solve_example_problem
def test_example():
    assert 1 + 1 == 3

@pytest.fixture
def test_sample_data():
    return {"key1": "value1", "key2": "value2"}

def test_example(sample_data):
    assert sample_data["key1"] == "value1"
    assert sample_data["key2"] == "value2"

def test_solve_example_problem():
    data = [1, 2, 3]
    expected_result = 6
    assert solve_example_problem(data) == expected_result 