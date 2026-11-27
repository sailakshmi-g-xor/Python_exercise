def even_squares(nums):
    return [number**2 for number in nums if number % 2 == 0]


def word_lengths(words):
    return {word: len(word) for word in words}


def first_letters(words):
    return {word[0] for word in words if word}


def flatten(matrix):
    return [value for row in matrix for value in row]


def transpose(matrix):
    return [
        [row[column] for row in matrix]
        for column in range(len(matrix[0]))
    ] if matrix else []


def main():
    print(even_squares(range(1, 11)))
    print(word_lengths(["apple", "kiwi", "banana", "fig"]))
    print(sorted(first_letters(["apple", "avocado", "banana", "blueberry", "cherry"])))
    print(flatten([[1, 2, 3], [4, 5, 6]]))
    print(transpose([[1, 2, 3], [4, 5, 6]]))


if __name__ == "__main__":
    main()
