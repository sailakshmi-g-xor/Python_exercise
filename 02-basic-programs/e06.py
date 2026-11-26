import sys
import string

def word_stats(text):
    lines = [line for line in text.splitlines() if line.strip()]

    words = []
    longest = ""

    for line in lines:
        for word in line.split():
            w = word.strip(string.punctuation).lower()

            if not w:
                continue

            words.append(w)

            if len(w) > len(longest):
                longest = w

    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    top = sorted(
        counts.items(),
        key=lambda kv: (-kv[1], kv[0])
    )[:3]

    return {
        "lines": len(lines),
        "words": len(words),
        "unique": len(counts),
        "longest": longest,
        "top": top
    }

text = sys.stdin.read()
stats = word_stats(text)

print("Lines:", stats["lines"])
print("Words:", stats["words"])
print("Unique words:", stats["unique"])
print("Longest word:", stats["longest"])
print("Most common:")

for word, count in stats["top"]:
    print(f" {word}: {count}")