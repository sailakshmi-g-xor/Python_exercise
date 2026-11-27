from pathlib import Path


def group_anagrams(words):
    groups = {}
    for word in set(words):
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    anagrams = [sorted(group) for group in groups.values() if len(group) >= 2]
    return sorted(anagrams, key=lambda group: (-len(group), group[0]))


def main():
    words_path = Path(__file__).parent / "data" / "words.txt"
    words = words_path.read_text(encoding="utf-8").split()
    groups = group_anagrams(words)
    print(f"groups: {len(groups)}")
    for group in groups:
        print(f"{len(group)}: {' '.join(group)}")
    if groups:
        print(f"largest: {groups[0][0]} ... {len(groups[0])} words")


if __name__ == "__main__":
    main()