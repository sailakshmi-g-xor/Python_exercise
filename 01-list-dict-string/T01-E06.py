from pathlib import Path


def group_by_length(words):
    groups = {}
    for word in set(words):
        groups.setdefault(len(word), []).append(word)
    return {length: sorted(group) for length, group in sorted(groups.items())}


def main():
    words_path = Path(__file__).parent / "data" / "words.txt"
    words = words_path.read_text(encoding="utf-8").split()
    for length, group in group_by_length(words).items():
        print(f"{length}: {', '.join(group)}")


if __name__ == "__main__":
    main()