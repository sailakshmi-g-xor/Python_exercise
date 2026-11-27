import sys

def is_palindrome(text):
    cleaned = "".join(character.lower() for character in text if character.isalnum())
    return cleaned == cleaned[::-1]

def main():
    for line in sys.stdin:
        line = line.rstrip("\r\n")
        if not line.strip():
            continue
        result = "yes" if is_palindrome(line) else "no"
        print(f"{line!r} -> {result}")


if __name__ == "__main__":
    main()

