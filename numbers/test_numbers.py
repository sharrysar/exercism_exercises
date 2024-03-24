import pytest
from grains import square
from armstrong_numbers import is_armstrong_number

@pytest.mark.parametrize("num, expected_ans", [(5, 16), (8, 128), (16, 32768)])
def test_square(num, expected_ans):
    assert square(num) == expected_ans

@pytest.mark.parametrize("num, expected_ans", [(153, True), (154, False), (9, True)])
def test_armstrong_nums(num, expected_ans):
    assert is_armstrong_number(num) == expected_ans