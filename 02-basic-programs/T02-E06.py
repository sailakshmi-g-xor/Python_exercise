import sys
import string


def word_stats(text):
    lines = [line for line in text.splitlines() if line.strip()]
    words = []
    longest = ""
    for line in lines:
        for word in line.split():
            cleaned = word.strip(string.punctuation).lower()
            if not cleaned:
                continue
            words.append(cleaned)
            if len(cleaned) > len(longest):
                longest = cleaned
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    top = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]
    return {
        "lines": len(lines),
        "words": len(words),
        "unique": len(counts),
        "longest": longest,
        "top": top,
    }


def main():
    stats = word_stats(sys.stdin.read())
    print("Lines:", stats["lines"])
    print("Words:", stats["words"])
    print("Unique words:", stats["unique"])
    print("Longest word:", stats["longest"])
    print("Most common:")
    for word, count in stats["top"]:
        print(f" {word}: {count}")


if __name__ == "__main__":
    main()