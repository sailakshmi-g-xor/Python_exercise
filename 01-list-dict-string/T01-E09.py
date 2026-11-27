import csv
from pathlib import Path


def sort_employees(rows):
    return sorted(
        rows,
        key=lambda row: (
            row["department"],
            -int(row["salary"]),
            row["name"],
        ),
    )


def sort_words(words):
    return sorted(words, key=lambda word: (len(word), word))


def sort_by_value(values):
    return sorted(values.items(), key=lambda item: (-item[1], item[0]))


def main():
    data_directory = Path(__file__).parent / "data"
    with (data_directory / "employees.csv").open(
        newline="", encoding="utf-8"
    ) as employees_file:
        employees = sort_employees(list(csv.DictReader(employees_file)))
    words = sort_words(
        (data_directory / "words.txt").read_text(encoding="utf-8").split()
    )
    stock = {"apples": 12, "pears": 5, "plums": 12, "figs": 30, "dates": 5}

    for employee in employees[:8]:
        print(
            f"{employee['department']:<12}"
            f"{employee['name']:<14}"
            f"{int(employee['salary']):>7}"
        )
    print(words[:8])
    print(sort_by_value(stock))


if __name__ == "__main__":
    main()

