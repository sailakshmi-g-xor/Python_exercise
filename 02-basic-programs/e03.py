def c_to_f(c):
    return (c*9/5)+32

def c_to_k(c):
    return c + 273.1

print(f"{'C':>5}{'F':>9}{'K':>9}")

for i in range(-20, 41, 10):
    fahrenheit = c_to_f(i)
    kelvin = c_to_k(i)
    print(f"{i:>5}{fahrenheit:>9.1f}{kelvin:>9.2f}")