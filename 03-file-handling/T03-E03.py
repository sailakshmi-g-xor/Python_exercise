from pathlib import Path


def append_entry(path, text):
    journal_path = Path(path)
    journal_path.parent.mkdir(parents=True, exist_ok=True)
    with journal_path.open("a", encoding="utf-8") as file:
        file.write(f"{text}\n")


def count_lines(path):
    journal_path = Path(path)
    if not journal_path.exists():
        return 0
    with journal_path.open(encoding="utf-8") as file:
        return sum(1 for _ in file)


def main():
    journal_path = Path(__file__).parent / "output" / "journal.txt"
    journal_path.unlink(missing_ok=True)
    print(f"Lines before: {count_lines(journal_path)}")

    entries = [
        "Started the course",
        "Finished file exercises",
        "Reviewed CSV handling",
    ]
    for entry in entries:
        append_entry(journal_path, entry)

    print(f"Lines after first run: {count_lines(journal_path)}")
    append_entry(journal_path, "Added one more entry")
    print(f"Lines after append: {count_lines(journal_path)}")
    print(journal_path.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
