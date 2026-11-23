def make_counter(start=0, step=1):
    current = start - step

    def counter():
        nonlocal current
        current += step
        return current

    return counter


def make_multiplier(n):
    def multiplier(x):
        return x * n

    return multiplier


def build_multipliers(factors):
    return [make_multiplier(factor) for factor in factors]


# Driver code
c1 = make_counter()
c2 = make_counter(start=10, step=5)

print(c1(), c1(), c1())
print(c2(), c2())

double = make_multiplier(2)
print(double(21))

print([f(10) for f in build_multipliers([2, 3, 4])])

print(double.__closure__[0].cell_contents)

broken = [lambda x: x * factor for factor in [2, 3, 4]]
print([f(10) for f in broken])