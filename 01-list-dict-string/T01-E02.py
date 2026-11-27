def clean_name(raw):
    return " ".join(raw.split()).title()


def initials(name):
    return ".".join(word[0] for word in name.split()) + "." if name.split() else ""


def main():
    names = [
        " aNNa maRIA smith ",
        "o'brien john",
        "MARY-JANE watson",
        "li wei",
    ]
    for raw in names:
        cleaned = clean_name(raw)
        print(f"{cleaned!r} -> {initials(cleaned)}")


if __name__ == "__main__":
    main()
