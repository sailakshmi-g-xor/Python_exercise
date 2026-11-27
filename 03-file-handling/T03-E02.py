from pathlib import Path


def write_squares(path, n):
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        for number in range(1, n + 1):
            file.write(f"{number} squared is {number * number}\n")
    return n


def main():
    output_path = Path(__file__).parent / "output" / "squares.txt"
    count = write_squares(output_path, 8)
    print(f"Lines written: {count}")
    print(output_path.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
