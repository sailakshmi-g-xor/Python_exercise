import csv
def sort_employees(rows):
    return sorted(
        rows,
        key=lambda r: (
            r["department"],
            -int(r["salary"]),
            r["name"]
        )
    )
def sort_words(words):
    return sorted(words, key=lambda w: (len(w), w))
def sort_by_value(d):
    return sorted(
        d.items(),
        key=lambda item: (-item[1], item[0])
    )
with open("01-list-dict-string/data/employees.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

with open("01-list-dict-string/data/words.txt", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]
employees = sort_employees(rows)
words = sort_words(words)

stock = {
    "apples": 12,
    "pears": 5,
    "plums": 12,
    "figs": 30,
    "dates": 5
}

for emp in employees[:8]:
    print(
        f"{emp['department']:<12}"
        f"{emp['name']:<14}"
        f"{int(emp['salary']):>7}"
    )
print(words[:8])
print(sort_by_value(stock))

