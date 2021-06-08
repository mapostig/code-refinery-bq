import pytest

def test_fahrenheit_to_celsius():
    temp_c = fahrenheit_to_celsius(temp_f = 100)
    expected_result = 37.7777777
    assert abs(temp_c - expected_result) < 1.0e-6
