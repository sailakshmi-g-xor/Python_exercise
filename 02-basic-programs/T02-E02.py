def grade(score):
    token = str(score)
    if not token.isdigit():
        return None

    value = int(token)
    if not 0 <= value <= 100:
        return None
    if value >= 90:
        return "A"
    if value >= 80:
        return "B"
    if value >= 70:
        return "C"
    if value >= 60:
        return "D"
    return "F"


def main():
    scores = input().split()
    valid_scores = []
    for token in scores:
        letter_grade = grade(token)
        if letter_grade is None:
            print(f"{token}: invalid")
        else:
            value = int(token)
            valid_scores.append(value)
            print(f"{value}: {letter_grade}")

    if valid_scores:
        average = sum(valid_scores) / len(valid_scores)
        print(f"Average of valid scores: {average:.1f}")
    else:
        print("No valid scores")


if __name__ == "__main__":
    main()
