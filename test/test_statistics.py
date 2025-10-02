import pytest

from geo212.statistics import *

@pytest.mark.parametrize('data,expected', [
    ([1], 1),
    ([1,1,1,1,1], 1),
    ([-1,1,-1,1], 0),
    ([3,1,2], 2),
    ([], 0),
])
def test_mode(data, expected):
    result = average(data)
    assert result == expected

def test_frequency():
    pass

def test_average():
    pass

def test_median():
    pass

def test_variance():
    pass

def test_standard_deviation():
    pass

def test_covariance():
    pass

def test_correlation():
    pass

def test_correlation_matrix():
    pass