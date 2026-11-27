def compare_attendance(day1, day2):
    first = set(day1)
    second = set(day2)
    return {
        "both": sorted(first & second),
        "either": sorted(first | second),
        "only_day1": sorted(first - second),
        "only_day2": sorted(second - first),
        "one_day_only": sorted(first ^ second),
    }


def dedupe_keep_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def min_max(nums):
    return min(nums), max(nums)


def main():
    day1 = ["asha", "ben", "chen", "dina", "emil", "farah"]
    day2 = ["ben", "dina", "gita", "hugo", "asha"]
    signups = ["asha", "ben", "asha", "chen", "ben", "dina"]
    low, high = min_max([7, 2, 9, 4])
    attendance = compare_attendance(day1, day2)
    for key, value in attendance.items():
        print(f"{key}: {value}")
    print(f"unique signups: {dedupe_keep_order(signups)}")
    print(f"min={low} max={high}")


if __name__ == "__main__":
    main()