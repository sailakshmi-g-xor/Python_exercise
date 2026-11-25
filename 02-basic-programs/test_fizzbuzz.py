import pytest
from e01 import fizzbuzz


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, "1\n"),
        (3, "1\n2\nFizz\n"),
        (5, "1\n2\nFizz\n4\nBuzz\n"),
        (15,
         "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n"
         "11\nFizz\n13\n14\nFizzBuzzz\n"),
    ],
)
def test_fizzbuzz(n, expected, capsys):
    fizzbuzz(n)

    captured = capsys.readouterr()

    assert captured.out == expected