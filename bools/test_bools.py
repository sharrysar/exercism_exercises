import pytest
import triangle

@pytest.mark.parametrize("sides, expected", [([5,5,5], True), ([2, 3, 2], False)])
def test_equilateral(sides, expected):
    result = triangle.equilateral(sides)
    assert result == expected

@pytest.mark.parametrize("sides, expected", [([3,4,4], True), ([2, 3, 4], False)])
def test_isosceles(sides, expected):
    result = triangle.isosceles(sides)
    assert result == expected

@pytest.mark.parametrize("sides, expected", [([5,4,6], True), ([7, 3, 2], False)])
def test_scalene(sides, expected):
    result = triangle.scalene(sides)
    assert result == expected