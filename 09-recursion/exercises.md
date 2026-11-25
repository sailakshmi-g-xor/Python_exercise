# Topic 09: Recursion - Exercises

Write your solution in a file such as `t09_e01.py` and paste the driver code from "Sample input" at the
bottom, inside `if __name__ == "__main__":`. Run it with `python t09_e01.py` (Windows: `py t09_e01.py`).
Your output must match "Expected output" exactly. Use the standard library only, and **use recursion**
where the exercise asks for it (loops are allowed only where the problem statement says so).

---

## T09-E01: Factorial, countdown and list sum

**Level:** Easy | **Estimated time:** 10 minutes | **Practises:** Base case, recursive case, recursion on lists

### Problem

Write three recursive functions:

- `factorial(n)`: `n! = n * (n-1)!`, with `0! = 1! = 1`. Negative `n` raises `ValueError("n must be non-negative")`.
- `countdown(n)`: returns the list `[n, n-1, ..., 1]`; for `n <= 0` return an empty list.
- `sum_list(numbers)`: the sum of a list of numbers without using `sum()` or loops.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
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
```

### Expected output

```text
1 1 120
2432902008176640000
[5, 4, 3, 2, 1]
[]
10
0
Error: n must be non-negative
```

### Hints

- Ask first: what is the smallest input for which the answer is obvious? That is the base case.
- For lists: the sum is the first element plus the sum of the rest (`numbers[1:]`).
- `[n] + countdown(n - 1)` builds the list from the front.

### Acceptance checklist

- [ ] Each function has a base case that stops the recursion
- [ ] No loops and no `sum()` are used
- [ ] Negative input to `factorial` raises the required error
- [ ] Output matches the expected output exactly

---

## T09-E02: Digits, reversing and palindromes

**Level:** Easy | **Estimated time:** 15 minutes | **Practises:** Recursion on integers and strings, slicing

### Problem

Write recursive functions:

- `sum_of_digits(n)`: sum of the decimal digits of an integer (ignore the sign: `-907` gives `16`).
- `reverse_string(text)`: the string reversed, without `[::-1]` or `reversed()`.
- `is_palindrome(text)`: `True` if the text reads the same forwards and backwards, ignoring case and any
  character that is not a letter or digit. The empty string is a palindrome. (Cleaning the text with a
  comprehension first is fine; the comparison itself must be recursive.)

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(sum_of_digits(12345))
print(sum_of_digits(-907))
print(sum_of_digits(0))
print(reverse_string("recursion"))
print(repr(reverse_string("")))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Python"))
print(is_palindrome(""))
```

### Expected output

```text
15
16
0
noisrucer
''
True
False
True
```

### Hints

- `n % 10` is the last digit and `n // 10` is everything else.
- Reverse: the reverse of `text` is the reverse of `text[1:]` followed by `text[0]`.
- Palindrome: compare first and last characters, then recurse on `s[1:-1]`.

### Acceptance checklist

- [ ] Base cases handle single digits, empty strings and one-character strings
- [ ] The comparison in `is_palindrome` is recursive
- [ ] Punctuation and capitalisation are ignored in palindromes
- [ ] Output matches the expected output exactly

---

## T09-E03: Recursion versus iteration

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** Fast exponentiation, Euclid's algorithm, recursion limit, converting recursion to loops

### Problem

Implement each task twice: recursively and iteratively.

- `power(base, exp)`: recursive **fast exponentiation** using the idea `x^n = (x^(n//2))^2`, times `x` when `n` is
  odd. It must need only about `log2(exp)` calls. `power_iter(base, exp)` is the loop version. Negative `exp`
  raises `ValueError("exp must be non-negative")`.
- `gcd(a, b)`: Euclid's algorithm recursively (`gcd(a, b) = gcd(b, a % b)`, `gcd(a, 0) = a`) and `gcd_iter`.
- `sum_to(n)`: `1 + 2 + ... + n` recursively and `sum_to_iter(n)` with a loop. Show that `sum_to(5000)` raises
  `RecursionError` while the loop version works.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(power(2, 10), power(3, 0), power(2, 100))
print(power(7, 13) == power_iter(7, 13))
print(gcd(48, 18), gcd(17, 5), gcd(0, 9))
print(gcd(1071, 462) == gcd_iter(1071, 462))
print(sum_to(100), sum_to_iter(100))
print(sum_to_iter(5000))
try:
    sum_to(5000)
except RecursionError:
    print("RecursionError: too deep")
```

### Expected output

```text
1024 1 1267650600228229401496703205376
True
6 1 9
True
5050 5050
12502500
RecursionError: too deep
```

### Hints

- Compute `half = power(base, exp // 2)` once and reuse it; calling `power` twice destroys the speed-up.
- Python's default recursion limit is about 1000 frames (`sys.getrecursionlimit()`).
- Iterative Euclid: `while b: a, b = b, a % b`.
- When is recursion the better choice and when is a loop? Be ready to discuss it.

### Acceptance checklist

- [ ] `power` makes a single recursive call per level
- [ ] Recursive and iterative versions give identical results
- [ ] `RecursionError` is caught and reported, not left to crash the program
- [ ] Output matches the expected output exactly

---

## T09-E04: Fibonacci with memoization

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** Overlapping subproblems, memoization with a dictionary, counting calls

### Problem

Write three Fibonacci functions (`fib(0) = 0`, `fib(1) = 1`):

- `fib_naive(n, counter=None)`: plain double recursion. If `counter` is a one-element list, add 1 to `counter[0]`
  on every call.
- `fib_memo(n, memo=None, counter=None)`: recursive, but results are stored in a dictionary `memo` that is
  shared by all recursive calls and created fresh on each top-level call. Count calls the same way.
- `fib_iter(n)`: a loop version, used to cross-check the other results.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print([fib_memo(i) for i in range(10)])
naive_calls = [0]
print(fib_naive(20, naive_calls), naive_calls[0])
memo_calls = [0]
print(fib_memo(20, counter=memo_calls), memo_calls[0])
print(fib_memo(90))
print(fib_memo(90) == fib_iter(90))
```

### Expected output

```text
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
6765 21891
6765 39
2880067194370816120
True
```

### Hints

- Mutable default arguments are dangerous: use `memo=None` and create `{}` inside the function.
- Pass `memo` and `counter` down in every recursive call.
- Naive `fib(20)` makes 21891 calls; the memoized version makes 39.

### Acceptance checklist

- [ ] `fib_memo(90)` returns instantly
- [ ] The call counts match the expected output
- [ ] The memo dictionary is not shared between separate top-level calls
- [ ] Output matches the expected output exactly

---

## T09-E05: Flatten a nested list

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** Recursion on nested data, `isinstance`, depth calculation

### Problem

Write recursive functions that work on arbitrarily nested lists:

- `flatten(nested)`: returns a new flat list with all non-list items in their original left-to-right order. Strings
  are items, not lists (do not split them into characters). The input must not be modified.
- `max_depth(nested)`: depth of nesting; a flat list (or an empty list) has depth 1.
- `deep_sum(nested)`: sum of all numbers at any depth.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
data = [1, [2, [3, [4]], 5], [], [[6]]]
print(flatten(data))
print(max_depth(data), max_depth([1, 2, 3]), max_depth([]))
print(deep_sum(data))
print(flatten(["ab", ["cd", ["ef"]]]))
print(data)
```

### Expected output

```text
[1, 2, 3, 4, 5, 6]
4 1 1
21
['ab', 'cd', 'ef']
[1, [2, [3, [4]], 5], [], [[6]]]
```

### Hints

- Loop over the items; for a list item recurse, otherwise keep the item.
- Use `isinstance(item, list)`; do not use `try/iter`, because strings are iterable.
- `max_depth`: one more than the deepest sub-list.

### Acceptance checklist

- [ ] Works for empty sub-lists and for deep nesting
- [ ] Strings stay whole
- [ ] The original list is unchanged (the driver prints it at the end)
- [ ] Output matches the expected output exactly

---

## T09-E06: Walk a directory tree

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Recursion over a nested dictionary, path building, aggregation

### Problem

A folder is modelled as a dictionary: values that are dictionaries are sub-folders and values that are integers
are file sizes in bytes. Use the `TREE` below and write recursive functions:

- `tree_lines(tree, depth=0)`: a list of lines for a printable tree. Folders end with `/`, files show their size in
  brackets, and each level is indented by two spaces.
- `total_size(tree)`: sum of all file sizes in the tree.
- `count_files(tree)`: number of files.
- `find_files(tree, extension, prefix="")`: list of full paths (joined with `/`, starting at the top folder name)
  of files whose name ends with `extension`, in tree order.
- `folder_depth(tree)`: number of folder levels; the top-level dictionary counts as one level and an empty folder as one level.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
TREE = {
    "project": {
        "README.md": 1200,
        "src": {
            "main.py": 3400,
            "utils.py": 800,
            "pkg": {"__init__.py": 0, "core.py": 5200},
        },
        "tests": {"test_main.py": 1500},
        "docs": {},
    }
}

print("\n".join(tree_lines(TREE)))
print(total_size(TREE))
print(count_files(TREE))
print(find_files(TREE, ".py"))
print(find_files(TREE, ".md"))
print(folder_depth(TREE))
print(total_size(TREE["project"]["src"]))
```

### Expected output

```text
project/
  README.md (1200)
  src/
    main.py (3400)
    utils.py (800)
    pkg/
      __init__.py (0)
      core.py (5200)
  tests/
    test_main.py (1500)
  docs/
12100
6
['project/src/main.py', 'project/src/utils.py', 'project/src/pkg/__init__.py', 'project/src/pkg/core.py', 'project/tests/test_main.py']
['project/README.md']
4
9400
```

### Hints

- Use `isinstance(value, dict)` to tell folders from files.
- To build a path, pass the path so far (`prefix`) down the recursion.
- `max(..., default=0)` avoids errors for empty folders.
- The same traversal pattern works for real folders with `os.scandir`, but this exercise uses a dictionary only.

### Acceptance checklist

- [ ] Folders are detected with `isinstance` and files are not recursed into
- [ ] Empty folders (`docs`) are handled
- [ ] `find_files` returns full paths such as `project/src/main.py`
- [ ] Output matches the expected output exactly

---

## T09-E07: Subsets and the power set

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Include/exclude recursion, combinations, subset sum

### Problem

Write recursive functions that take any iterable and return lists of lists:

- `subsets(items)`: all subsets (the power set). Order the result like this: first all subsets that do not
  contain the first item, then those same subsets with the first item added in front (see expected output).
- `combinations_of_size(items, k)`: all subsets with exactly `k` items, preserving the original item order
  inside each combination (include-the-first-item results come before exclude-the-first-item results).
- `subset_sum(items, target)`: all subsets whose items add up to `target` (include-first results first).

A set of `n` items has `2**n` subsets; the driver checks this for `n = 10`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(subsets([1, 2, 3]))
print(len(subsets(range(10))))
print(combinations_of_size(["a", "b", "c", "d"], 2))
print(subset_sum([3, 34, 4, 12, 5, 2], 9))
print(subset_sum([1, 2], 10))
```

### Expected output

```text
[[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
1024
[['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd']]
[[3, 4, 2], [4, 5]]
[]
```

### Hints

- For each item there are two choices: it is in the subset or it is not.
- `subsets([])` is `[[]]`: one subset, the empty one.
- `subset_sum`: choosing `first` reduces the target by `first`.
- Do not use `itertools` for the solution; you may use it to double-check your answers.

### Acceptance checklist

- [ ] `subsets([])` returns `[[]]`
- [ ] `len(subsets(range(10)))` is 1024
- [ ] Results are new lists (no shared references between subsets)
- [ ] Output matches the expected output exactly

---

## T09-E08: Tower of Hanoi

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Divide and conquer, returning a list of moves, verifying a solution

### Problem

Move `n` disks from peg `A` to peg `C` using peg `B`, moving one disk at a time and never placing a larger disk on a
smaller one. Disk 1 is the smallest.

- `hanoi(n, source="A", target="C", spare="B")` returns the list of moves as tuples `(disk, from_peg, to_peg)`.
- `hanoi_move_count(n)` returns the number of moves required by formula (`2**n - 1`).
- `is_valid_solution(n, moves)` replays a list of moves on three pegs and returns `True` only if every move is legal
  and all disks end on peg `C` in the right order. (This helper does not need to be recursive.)

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
for disk, src, dst in hanoi(3):
    print(f"Move disk {disk} from {src} to {dst}")
print(len(hanoi(3)), hanoi_move_count(3))
print(len(hanoi(10)), hanoi_move_count(10))
print(is_valid_solution(4, hanoi(4)))
print(is_valid_solution(3, [(1, "A", "C"), (3, "A", "B")]))
```

### Expected output

```text
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
7 7
1023 1023
True
False
```

### Hints

- To move `n` disks: move `n-1` to the spare peg, move the big disk, then move the `n-1` disks onto it.
- The base case is `n == 0`: no moves.
- Represent each peg as a list and use `.pop()` / `.append()` when replaying moves.

### Acceptance checklist

- [ ] `hanoi(3)` has 7 moves and `hanoi(10)` has 1023
- [ ] Your own moves pass `is_valid_solution` for several values of `n`
- [ ] An illegal list of moves is rejected
- [ ] Output matches the expected output exactly

---

## T09-E09: Permutations

**Level:** Hard | **Estimated time:** 30 minutes | **Practises:** Choose-and-recurse, building results, avoiding duplicates

### Problem

Write:

- `permutations(items)`: every ordering of the items as a list of lists, in this order: pick each item in turn as the
  first element, then append all permutations of the remaining items. `permutations([])` is `[[]]`.
  Do not use `itertools`.
- `unique_permutations(text)`: the distinct permutations of a string that may contain repeated letters, as a list
  of strings, without generating duplicates and removing them afterwards.
- `permutation_count(n)`: `n!` computed recursively.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(permutations([1, 2, 3]))
print(len(permutations(range(5))), permutation_count(5))
print(["".join(p) for p in permutations("abc")][:3])
print(unique_permutations("aab"))
print(len(permutations("aab")), len(unique_permutations("aab")))
print(permutations([]))
```

### Expected output

```text
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
120 120
['abc', 'acb', 'bac']
['aab', 'aba', 'baa']
6 3
[[]]
```

### Hints

- Loop over the positions: choose `items[i]`, recurse on `items[:i] + items[i+1:]`.
- For unique permutations keep a `seen` set of letters already tried at this position.
- The number of permutations grows fast: 10 items already give 3,628,800.

### Acceptance checklist

- [ ] Result order matches the expected output
- [ ] `unique_permutations("aab")` returns three strings, not six
- [ ] Duplicates are skipped during generation (no `set(...)` of the final result)
- [ ] Output matches the expected output exactly

---

## T09-E10: N-Queens

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Backtracking: choose, explore, un-choose

### Problem

Place `n` queens on an `n x n` chessboard so that no two attack each other (no shared row, column or diagonal).

- `solve_n_queens(n)` returns a list of **all** solutions. A solution is a list of length `n` where item `r` is the
  column of the queen in row `r`. Solutions appear in the order a row-by-row, left-to-right search finds them.
- `format_board(solution)` returns a multi-line string with `Q` for a queen and `.` for empty squares.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(solve_n_queens(4))
print(format_board(solve_n_queens(4)[0]))
print([len(solve_n_queens(n)) for n in range(1, 9)])
print(solve_n_queens(3))
print(solve_n_queens(6)[0])
```

### Expected output

```text
[[1, 3, 0, 2], [2, 0, 3, 1]]
.Q..
...Q
Q...
..Q.
[1, 0, 0, 2, 10, 4, 40, 92]
[]
[1, 3, 5, 0, 2, 4]
```

### Hints

- Place one queen per row. For each row try every column and recurse only if the square is safe.
- Two queens share a diagonal when `abs(col1 - col2) == abs(row1 - row2)`.
- After the recursive call returns, remove the queen you placed (backtrack) and try the next column.
- Known solution counts for n = 1..8: 1, 0, 0, 2, 10, 4, 40, 92.

### Acceptance checklist

- [ ] Backtracking removes the queen after exploring a column
- [ ] The solution counts for n = 1 to 8 match the known values
- [ ] `solve_n_queens(3)` returns an empty list
- [ ] Output matches the expected output exactly

---

## T09-E11: Sudoku-lite (4x4 solver)

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Backtracking on a grid, constraint checking, counting solutions

### Problem

A 4x4 sudoku uses the digits 1 to 4; each row, column and 2x2 box must contain every digit exactly once. Empty cells
are `0`. Use the `PUZZLE` below.

- `can_place(grid, row, col, value)`: `True` if `value` does not already appear in that row, column or 2x2 box.
- `solve(grid)`: returns a **solved copy** of the grid, or `None` if there is no solution. The input grid must not be
  modified.
- `count_solutions(grid, limit=2)`: number of solutions, stopping early once `limit` is reached (never return more than
  `limit`). A well-formed puzzle has exactly one.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
PUZZLE = [
    [1, 0, 0, 0],
    [0, 0, 3, 0],
    [0, 4, 0, 0],
    [0, 0, 0, 2],
]

solved = solve(PUZZLE)
for row in solved:
    print(" ".join(str(v) for v in row))
print(count_solutions(PUZZLE))
print(count_solutions([[0] * 4 for _ in range(4)], limit=5))
print(solve([[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
print(PUZZLE[0])
```

### Expected output

```text
1 3 2 4
4 2 3 1
2 4 1 3
3 1 4 2
1
5
None
[1, 0, 0, 0]
```

### Hints

- Find the first empty cell; try values 1 to 4; recurse; undo the placement when the recursion fails.
- The box of cell `(r, c)` starts at `(r // 2 * 2, c // 2 * 2)`.
- Copy the grid first (`[row[:] for row in grid]`) so the caller's data is untouched.
- `solve` returns as soon as one solution is found; `count_solutions` has to keep exploring.

### Acceptance checklist

- [ ] The returned grid satisfies the row, column and box rules
- [ ] The original `PUZZLE` is unchanged after solving
- [ ] The empty 4x4 grid has at least 5 solutions with `limit=5`
- [ ] A puzzle with a duplicate digit in a row returns `None`
- [ ] Output matches the expected output exactly
