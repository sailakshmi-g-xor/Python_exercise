def letter_frequency(text):
    freq = {}
    s = set()
    for letter in text :
        s.add(letter)
        if letter.isalpha():
            letter = letter.lower()
            if letter in freq:
                freq[letter]+=1
            else:
                freq[letter]=1
    print(f"Total unique letters: {len(s)}")
    return freq
def top_n(dict,n):
    l = sorted(dict.items(), key=lambda x: x[1], reverse=True)[:n]
    for key, value in l:
        print(f"{key}: {value}")

text = "The quick brown fox jumps over the lazy dog and the cat"
dict = letter_frequency(text)
top_n(dict,5)
