import csv
def summarize(rows):
    result = {}
    for row in rows:
        dept = row["department"]
        name = row["name"]
        salary = float(row["salary"])

        if dept not in result:
            result[dept] = {
                "count": 0,
                "total_salary": 0,
                "top_salary": salary,
                "top": name
            }

        result[dept]["count"] += 1
        result[dept]["total_salary"] += salary

        if salary > result[dept]["top_salary"]:
            result[dept]["top_salary"] = salary
            result[dept]["top"] = name

    summary = {}

    for dept, data in result.items():
        summary[dept] = {
            "count": data["count"],
            "average": round(
                data["total_salary"] / data["count"], 2
            ),
            "top": data["top"]
        }

    return summary

with open("01-list-dict-string/data/employees.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
data = summarize(rows)
for dept in sorted(data):
    info = data[dept]
    print(
        f"{dept:<12}"
        f"{info['count']:>6}"
        f"{info['average']:>12.2f}  "
        f"{info['top']}"
    )