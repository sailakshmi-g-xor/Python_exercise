ROMAN_MAP = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def to_roman(n):
    if not (1 <= n <= 3999):
        raise ValueError("out of range")

    result = []

    for value, symbol in ROMAN_MAP:
        while n >= value:
            result.append(symbol)
            n -= value

    return "".join(result)


def from_roman(text):
    text = text.upper()

    if not text:
        return None

    for ch in text:
        if ch not in VALUES:
            return None

    total = 0
    i = 0

    while i < len(text):
        current = VALUES[text[i]]

        if i + 1 < len(text):
            nxt = VALUES[text[i + 1]]

            if current < nxt:
                total += nxt - current
                i += 2
                continue

        total += current
        i += 1

    try:
        if to_roman(total) != text:
            return None
    except ValueError:
        return None

    return total


def main():
    import sys

    for line in sys.stdin:
        token = line.strip()
        if not token:
            continue

        if token.isdigit():
            try:
                print(f"{token} -> {to_roman(int(token))}")
            except ValueError:
                print(f"{token} -> out of range (1-3999)")
        else:
            value = from_roman(token)
            if value is None:
                print(f"{token} -> invalid")
            else:
                print(f"{token} -> {value}")


if __name__ == "__main__":
    main()