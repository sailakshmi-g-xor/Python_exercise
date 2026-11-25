def compare_attendance(day1,day2):
    s1 = set(day1)
    s2 = set(day2)
    d = {}
    d['both'] = s1 & s2
    d['either'] = s1 | s2
    d['day1_only'] = s1 - s2
    d['day2_only'] = s2 - s1
    d['one_day_only'] = s1 ^ s2

    return d
def dedupe_keep_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
def min_max(nums):
    return (min(nums),max(nums))

day1 = ["asha", "ben", "chen", "dina", "emil", "farah"]
day2 = ["ben", "dina", "gita", "hugo", "asha"]
signups = ["asha", "ben", "asha", "chen", "ben", "dina"]
nums = [7,2,9,4]

print(compare_attendance(day1,day2))
print(dedupe_keep_order(signups))
print(min_max(nums))