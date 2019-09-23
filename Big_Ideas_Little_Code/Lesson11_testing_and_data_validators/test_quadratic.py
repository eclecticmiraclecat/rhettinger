import pytest
from quadratic import quadratic
import itertools

def test_quadratic():
    x1, x2 = quadratic(a=8, b=22, c=15)
    assert 8*x1**2 + 22*x1 + 15 == 0
    assert 8*x2**2 + 22*x2 + 15 == 0

def test_quadratic_types():
    with pytest.raises(TypeError):
        quadratic(a=8, b='hello', c=15)
    with pytest.raises(TypeError):
        quadratic(a=8, b=22, c=15, d=4)

def test_torture_test():
    args = [10, 0, 1, 18, -5, -1, 0.5, -1.5]
    for t in itertools.permutations(args, 3):
        x1, x2 = quadratic(*t)
