def mask_card(number):
    return "*" * max(0, len(number) - 4) + number[-4:]


def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])


def middle(text):
    midpoint = len(text) // 2
    return text[midpoint - 1 : midpoint + 1] if len(text) % 2 == 0 else text[midpoint]


def every_other(text):
    return text[::2]


def main():
    print(mask_card("4111111111111111"))
    print(reverse_words("learning python is fun"))
    print(middle("python"), middle("slicing"))
    print(every_other("abcdefghij"))
    print("Programming"[::-1])


if __name__ == "__main__":
    main()