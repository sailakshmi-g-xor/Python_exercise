def group_anagrams(words):
    words = set(words)
    d = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)
    for key,value in sorted(d.items(),
                            key = lambda x : len(x[1]),
                            reverse = True):
        if len(value) < 2:
            continue
        print(f"{len(value)}:{" ".join(word for word in value)}")
      
with open("01-list-dict-string/data/words.txt", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

group_anagrams(words)