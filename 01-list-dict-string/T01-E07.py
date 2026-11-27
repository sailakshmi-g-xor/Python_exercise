import csv
from pathlib import Path


def summarize(rows):
    departments = {}
    for row in rows:
        department = row["department"]
        name = row["name"]
        salary = int(row["salary"])
        if department not in departments:
            departments[department] = {
                "count": 0,
                "total_salary": 0,
                "top_salary": salary,
                "top": name,
            }
        data = departments[department]
        data["count"] += 1
        data["total_salary"] += salary
        if salary > data["top_salary"]:
            data["top_salary"] = salary
            data["top"] = name

    return {
        department: {
            "count": data["count"],
            "average": round(data["total_salary"] / data["count"], 2),
            "top": data["top"],
        }
        for department, data in departments.items()
    }


def main():
    employees_path = Path(__file__).parent / "data" / "employees.csv"
    with employees_path.open(newline="", encoding="utf-8") as employees_file:
        rows = list(csv.DictReader(employees_file))

    print(f"{'Department':<12}{'Count':>6}{'Average':>12}  Top earner")
    for department, info in sorted(summarize(rows).items()):
        print(
            f"{department:<12}"
            f"{info['count']:>6}"
            f"{info['average']:>12.2f}  "
            f"{info['top']}"
        )


if __name__ == "__main__":
    main()