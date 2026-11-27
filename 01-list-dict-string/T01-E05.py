def letter_frequency(text):
    frequency = {}
    for character in text.lower():
        if character.isalpha():
            frequency[character] = frequency.get(character, 0) + 1
    return frequency


def top_n(freq, n):
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]


def main():
    text = "The quick brown fox jumps over the lazy dog and the cat"
    frequency = letter_frequency(text)
    print(f"distinct letters: {len(frequency)}")
    for letter, count in top_n(frequency, 5):
        print(f"{letter}: {count}")


if __name__ == "__main__":
    main()
