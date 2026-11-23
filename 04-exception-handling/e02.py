from pathlib import Path


def parse_readings(lines):
    values = []
    bad = []

    for line_number, line in enumerate(lines, start=1):
        text = line.strip()

        try:
            value = float(text)
        except ValueError:
            bad.append((line_number, text))
        else:
            values.append(value)

    return values, bad


lines = Path("data/readings.txt").read_text(
    encoding="utf-8"
).splitlines()

values, bad = parse_readings(lines)

print(f"Lines: {len(lines)}")
print(f"Valid: {len(values)}")
print(f"Invalid lines: {[line_no for line_no, _ in bad]}")

for line_no, text in bad:
    print(f" line {line_no}: {text!r}")

if values:
    average = sum(values) / len(values)
    print(f"Average: {average:.2f}")
    print(f"Min: {min(values)} Max: {max(values)}")