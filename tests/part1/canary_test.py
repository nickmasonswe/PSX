# test_sample.py
'''This should yield 3 passes and 3 fails'''

import pytest
from units.part1.canary_problem import solve_example_problem

def test_example_fail():
    assert 1 + 1 == 3  # This will fail

def test_example_pass():
    assert 1 + 1 == 2  # This will pass

@pytest.fixture
def sample_data():
    return {"key1": "value1", "key2": "value2"}

def test_sample_data_correct(sample_data):
    assert sample_data["key1"] == "value1"
    assert sample_data["key2"] == "value2"

def test_sample_data_incorrect(sample_data):
    assert sample_data["key1"] == "wrong_value"  # This will fail

def test_solve_example_problem_correct():
    data = [1, 2, 3]
    expected_result = 6
    assert solve_example_problem(data) == expected_result #This will pass

def test_solve_example_problem_incorrect():
    data = [1, 2, 3]
    wrong_result = 7
    assert solve_example_problem(data) == wrong_result  # This will fail


'''This should yield 3 passes and 3 fails'''