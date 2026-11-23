def divide_line(line):
    
    try:
        words = line.split()
        a = float(words[0])
        b = float(words[1])
        result = a/b
    except ValueError:
        return "Error: Invalid input. Please enter two numbers."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"{a:g}/{b:g} = {result:g}"

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line.strip():
        continue

    print(divide_line(line))