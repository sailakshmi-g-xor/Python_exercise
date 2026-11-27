def c_to_f(c):
    return (c * 9 / 5) + 32


def c_to_k(c):
    return c + 273.15


def main():
    print(f"{'C':>5}{'F':>9}{'K':>9}")
    for celsius in range(-20, 41, 10):
        print(
            f"{celsius:>5}"
            f"{c_to_f(celsius):>9.1f}"
            f"{c_to_k(celsius):>9.2f}"
        )


if __name__ == "__main__":
    main()