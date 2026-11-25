from pathlib import Path
def append_entry(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write(text + "\n")
def count_lines(path):
    if not path.exists():
        return 0

    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

journal_path = Path("output/journal.txt")
journal_path.parent.mkdir(exist_ok=True)
journal_path.unlink(missing_ok=True)

print(f"Lines before: {count_lines(journal_path)}")

entries = [
    "Started the course",
    "Finished file exercises",
    "Reviewed CSV handling"
]

for entry in entries:
    append_entry(journal_path, entry)

print(f"Lines after first run: {count_lines(journal_path)}")

append_entry(journal_path, "Added one more entry")

print(f"Lines after append: {count_lines(journal_path)}")
print()

with open(journal_path, "r", encoding="utf-8") as f:
    print(f.read(), end="")