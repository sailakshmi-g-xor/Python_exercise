from itertools import islice
from pathlib import Path


def file_stats(path):
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\r\n") for line in file]
    return {
        "lines": len(lines),
        "words": sum(len(line.split()) for line in lines),
        "characters": sum(len(line) for line in lines),
        "blank": sum(not line.strip() for line in lines),
    }


def main():
    notes_path = Path(__file__).parent / "data" / "notes.txt"
    with notes_path.open(encoding="utf-8") as file:
        for number, line in enumerate(islice(file, 5), start=1):
            content = line.rstrip("\r\n")
            print(f"{number:>3}: {content}")

    stats = file_stats(notes_path)
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
    print(f"Blank lines: {stats['blank']}")


if __name__ == "__main__":
    main()
