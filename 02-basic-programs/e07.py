def calculate(op, a, b):
    if op == "1":
        return a + b
    elif op == "2":
        return a - b
    elif op == "3":
        return a * b
    elif op == "4":
        if b == 0:
            return None
        return a / b


while True:
    print("--- Calculator ---")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Quit")

    choice = input()

    if choice == "5":
        print("Goodbye")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice")
        continue

    try:
        a = float(input())
        b = float(input())
    except ValueError:
        print("Not a number")
        continue

    result = calculate(choice, a, b)

    if result is None:
        print("Cannot divide by zero")
    else:
        print(f"Result: {result:g}")