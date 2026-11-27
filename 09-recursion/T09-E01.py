def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def countdown(n):
    if n<=0:
        return []
    return [n].append(countdown(n-1))
def sum_list(l):
    if l == []:
        return 0
    return l[0]+sum(l[1:])

print(factorial(0), factorial(1), factorial(5))
print(factorial(20))
print(countdown(5))
print(countdown(0))
print(sum_list([1, 2, 3, 4]))
print(sum_list([]))
try:
    factorial(-3)
except ValueError as err:
    print("Error:", err)