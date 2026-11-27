import importlib.util
from pathlib import Path

import pytest


spec = importlib.util.spec_from_file_location(
    "t02_e01", Path(__file__).with_name("T02-E01.py")
)
fizzbuzz_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fizzbuzz_module)
fizzbuzz = fizzbuzz_module.fizzbuzz


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, ["1"]),
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (15, [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz",
        ]),
    ],
)
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected