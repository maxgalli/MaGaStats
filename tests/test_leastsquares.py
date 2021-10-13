import pytest
from magastats.least_squares import LeastSquares
import numpy as np


def straight_line(x, a, b):
    return a * x + b


def test_least_squares():
    x = np.array([0, 1, 2])
    y = np.array([3.02, 3.93, 5.001])
    cov_matrix = np.array([[0.1, 0.0, 0.0], [0.0, 0.1, 0.0], [0.0, 0.0, 0.1]])

    ls = LeastSquares(x, y, straight_line, cov_matrix)
    with pytest.raises(ValueError):
        m = ls.minimize_with_scipy()
