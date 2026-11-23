def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul
}


def calculate(op_name, a, b):
    try:
        return OPERATIONS[op_name](a, b)
    except KeyError:
        raise ValueError(f"Unknown operation: {op_name}")


def apply_twice(func, value):
    return func(func(value))


def compose(f, g):
    def h(x):
        return f(g(x))
    return h


print(calculate("add", 2, 3))
print(calculate("mul", 4, 5))

print(apply_twice(lambda s: s + "!", "hey"))

shout = compose(str.upper, lambda s: s + "!")
print(shout("hello"))

print(add.__name__, callable(add), type(add).__name__)

print(sorted(OPERATIONS))

try:
    calculate("pow", 2, 3)
except ValueError as err:
    print("Error:", err)