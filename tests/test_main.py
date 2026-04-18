import pytest

def fast_exponentiation(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result

def test_fast_exponentiation():
    assert fast_exponentiation(2, 3, 10) == 8
    assert fast_exponentiation(5, 4, 10) == 5
    assert fast_exponentiation(10, 2, 10) == 0
    assert fast_exponentiation(2, 10, 100) == 24
    assert fast_exponentiation(5, 5, 100) == 25

def test_fast_exponentiation_large_numbers():
    assert fast_exponentiation(2, 100, 1000) == 376
    assert fast_exponentiation(5, 50, 1000) == 625

def test_fast_exponentiation_edge_cases():
    assert fast_exponentiation(1, 10, 10) == 1
    assert fast_exponentiation(0, 10, 10) == 0
    assert fast_exponentiation(10, 0, 10) == 1

pytest.main([__file__])
