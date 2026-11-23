# Topic 02: Basic programs: exercises

Work from the topic folder (the one that contains `data/`). Put your own scripts in a folder of your choice, open data files as `data/<name>` when you run from the topic folder, and write any output files into an `output/` folder (create it with `pathlib`), never into `data/`.

Expected output below was produced by running the trainer solutions with Python 3.12.

## T02-E01 - FizzBuzz

**Level:** Easy  |  **Estimated time:** 10 minutes  |  **Practises:** Loops and conditions

**Data files:** none (all data is given in the exercise)

### Problem

Read a whole number `n` (one line, no prompt text). Write a function `fizzbuzz(n)` that returns a list of strings for the numbers 1 to `n`: `"Fizz"` for multiples of 3, `"Buzz"` for multiples of 5, `"FizzBuzz"` for multiples of both, otherwise the number itself as text. Print one item per line.

### Sample input

Typed into the program (standard input):

```text
15
```

### Expected output

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

### Hints

- `input()` without any text inside the brackets reads a line silently; convert with `int(...)`.
- `range(1, n + 1)` includes `n`.
- Check the multiple-of-both case first, or the Fizz branch will catch it.
- `i % 3 == 0` tests divisibility.

### Acceptance checklist

- [ ] Multiples of 15 print `FizzBuzz` (not `Fizz`).
- [ ] The function returns a list; printing happens outside it.
- [ ] `fizzbuzz(0)` returns an empty list.
- [ ] Output matches the expected output.

---

## T02-E02 - Grade calculator

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** if/elif chains and input checking

**Data files:** none (all data is given in the exercise)

### Problem

Read one line containing several scores separated by spaces. Write `grade(score)`: 90 and above is `A`, 80 to 89 `B`, 70 to 79 `C`, 60 to 69 `D`, below 60 `F`. A token is valid only if it is a whole number from 0 to 100; anything else (for example `-5`, `abc`, `4.5`, `101`) is printed as `<token>: invalid` and is excluded from the average. Print `<score>: <grade>` for valid scores, then `Average of valid scores: <value>` with one decimal, or `No valid scores` when there are none.

### Sample input

Typed into the program (standard input):

```text
95 82 67 45 100 -5 abc 73
```

### Expected output

```text
95: A
82: B
67: D
45: F
100: A
-5: invalid
abc: invalid
73: C
Average of valid scores: 77.0
```

### Hints

- `token.isdigit()` is `False` for `"-5"`, `"abc"` and `"4.5"`.
- Check `isdigit()` before calling `int(token)`.
- Keep the valid scores in a list, then use `sum()` and `len()`.
- Guard against dividing by zero when the list is empty.

### Acceptance checklist

- [ ] Boundaries 90, 80, 70, 60 give the higher grade.
- [ ] Invalid tokens are reported and do not affect the average.
- [ ] The empty case prints `No valid scores`, with no crash.
- [ ] Output matches the expected output.

---

## T02-E03 - Temperature table

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** for loops with range, formatted output

**Data files:** none (all data is given in the exercise)

### Problem

Print a table of temperatures from -20 to 40 degrees Celsius in steps of 10. Write `c_to_f(c)` and `c_to_k(c)` (Kelvin = Celsius + 273.15). Each row has Celsius right-aligned in width 5, Fahrenheit right-aligned in width 9 with one decimal, Kelvin right-aligned in width 9 with two decimals. Print a header row with the column names `C`, `F`, `K` using the same widths.

### Sample input

No input.

### Expected output

```text
    C        F        K
  -20     -4.0   253.15
  -10     14.0   263.15
    0     32.0   273.15
   10     50.0   283.15
   20     68.0   293.15
   30     86.0   303.15
   40    104.0   313.15
```

### Hints

- `range(start, stop, step)`; stop is exclusive, so use 41.
- Fahrenheit = Celsius * 9 / 5 + 32.
- `f"{value:>9.1f}"` right-aligns in 9 characters with one decimal.
- `f"{'C':>5}"` formats a text header with the same width.

### Acceptance checklist

- [ ] Seven data rows from -20 to 40.
- [ ] Columns line up under the header.
- [ ] 0 C shows 32.0 F and 273.15 K.
- [ ] Output matches the expected output.

---

## T02-E04 - Prime check

**Level:** Easy  |  **Estimated time:** 20 minutes  |  **Practises:** while loops, functions, early return

**Data files:** none (all data is given in the exercise)

### Problem

Write `is_prime(n)` (numbers below 2 are not prime) and `primes_up_to(limit)`. Read one line of numbers separated by spaces and print `<n> is prime` or `<n> is not prime` for each. Then print `Primes up to 50:` followed by the list, and `Count:` followed by how many there are.

### Sample input

Typed into the program (standard input):

```text
29 1 49 97 0 2
```

### Expected output

```text
29 is prime
1 is not prime
49 is not prime
97 is prime
0 is not prime
2 is prime
Primes up to 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Count: 15
```

### Hints

- You only need to test divisors up to the square root: loop `while i * i <= n`.
- Return `False` as soon as you find a divisor.
- 0 and 1 are not prime; 2 is.
- A list comprehension can build `primes_up_to` from `is_prime`.

### Acceptance checklist

- [ ] 0, 1 and negative numbers are not prime.
- [ ] 2 is prime and 49 is not.
- [ ] `primes_up_to(50)` has 15 numbers.
- [ ] Output matches the expected output.

---

## T02-E05 - Palindrome checker

**Level:** Medium  |  **Estimated time:** 15 minutes  |  **Practises:** String processing and reading all of standard input

**Data files:** none (all data is given in the exercise)

### Problem

Write `is_palindrome(text)` that ignores case, spaces and punctuation (only letters and digits count). Read lines until the input ends, skip blank lines, and print `'<line>' -> yes` or `'<line>' -> no` (the line printed with `repr`, so the quotes show).

### Sample input

Typed into the program (standard input):

```text
Racecar
A man, a plan, a canal: Panama
Hello, World

Was it a car or a cat I saw?
No lemon, no melon
Python
```

### Expected output

```text
'Racecar' -> yes
'A man, a plan, a canal: Panama' -> yes
'Hello, World' -> no
'Was it a car or a cat I saw?' -> yes
'No lemon, no melon' -> yes
'Python' -> no
```

### Hints

- `for line in sys.stdin:` reads every line until the end of input (add `import sys`).
- `line.strip()` removes the newline.
- Build a cleaned list with `ch.lower() for ch in text if ch.isalnum()`.
- A sequence is a palindrome when it equals its reverse: `cleaned == cleaned[::-1]`.

### Acceptance checklist

- [ ] Punctuation and capital letters do not matter.
- [ ] Blank lines produce no output.
- [ ] The empty string counts as a palindrome in the function.
- [ ] Output matches the expected output.

---

## T02-E06 - Word count

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** Dictionaries, string cleaning, sorting

**Data files:** none (all data is given in the exercise)

### Problem

Read all of standard input as text. Write `word_stats(text)` returning a dictionary with `lines` (non-blank lines), `words`, `unique` (distinct words), `longest` (first longest word) and `top` (the 3 most common words as `(word, count)`, ties alphabetical). Words are lower-cased with leading and trailing punctuation removed. Print the result in the layout shown.

### Sample input

Typed into the program (standard input):

```text
Python is easy to learn, and Python is fun.
The best way to learn Python is to write code!
Practice every day; the code will become easy.
```

### Expected output

```text
Lines: 3
Words: 27
Unique words: 17
Longest word: practice
Most common:
  is: 3
  python: 3
  to: 3
```

### Hints

- `sys.stdin.read()` returns all the input as one string.
- `string.punctuation` holds the punctuation characters; use `word.strip(string.punctuation)`.
- Count with `counts[w] = counts.get(w, 0) + 1`.
- `sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:3]` gives the top three.

### Acceptance checklist

- [ ] `Python` and `python` count as the same word.
- [ ] Trailing commas, full stops and exclamation marks are removed.
- [ ] Ties in the top list are alphabetical.
- [ ] Output matches the expected output.

---

## T02-E07 - Simple menu program

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** while True loop, menu handling, input validation

**Data files:** none (all data is given in the exercise)

### Problem

Write a calculator that shows a menu and repeats until the user chooses Quit. Print the menu exactly as shown each time, then read the choice (no prompt text). For choices 1 to 4 read two more lines (the two numbers). Behaviour:

- `5` prints `Goodbye` and ends the program.
- Any other choice prints `Invalid choice` and shows the menu again.
- If either number is not a valid number, print `Not a number` and show the menu again.
- Division by zero prints `Cannot divide by zero`.
- Otherwise print `Result: <value>` formatted with `:g` (so 8.0 shows as `8`).

Put the arithmetic in `calculate(op, a, b)` which returns `None` for division by zero.

### Sample input

Typed into the program (standard input):

```text
1
5
3
4
7
0
9
3
x
2
4
10
4
5
```

### Expected output

```text
--- Calculator ---
1) Add
2) Subtract
3) Multiply
4) Divide
5) Quit
Result: 8
--- Calculator ---
1) Add
2) Subtract
3) Multiply
4) Divide
5) Quit
Cannot divide by zero
--- Calculator ---
1) Add
2) Subtract
3) Multiply
4) Divide
5) Quit
Invalid choice
--- Calculator ---
1) Add
2) Subtract
3) Multiply
4) Divide
5) Quit
Not a number
--- Calculator ---
1) Add
2) Subtract
3) Multiply
4) Divide
5) Quit
Result: 2.5
--- Calculator ---
1) Add
2) Subtract
3) Multiply
4) Divide
5) Quit
Goodbye
```

### Hints

- `while True:` with `break` on the quit choice.
- Use `continue` to go back to the menu after an error.
- `float(text)` raises `ValueError` for bad text: wrap it in `try/except ValueError` and return `None`.
- `f"{result:g}"` prints `8.0` as `8` and `2.5` as `2.5`.

### Acceptance checklist

- [ ] The menu is displayed again after every action.
- [ ] Invalid choices and invalid numbers do not crash the program.
- [ ] Division by zero is handled.
- [ ] Output matches the expected output.

---

## T02-E08 - Number guessing with a fixed seed

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** random with seed, loops, counting attempts

**Data files:** none (all data is given in the exercise)

### Problem

Make a guessing game that is reproducible. At the start call `random.seed(42)` and pick the secret with `random.randint(1, 100)` (this gives the same number every run). The player has 7 valid attempts. Read one guess per line (no prompt text):

- Not a whole number: print `Please enter a whole number` (does not use an attempt).
- Outside 1 to 100: print `Out of range, use 1 to 100` (does not use an attempt).
- Valid guess number `k`: print `Guess k: <guess> is too low` or `... is too high`, or on success `Guess k: <guess> is correct! Solved in k attempts` and stop.
- After 7 valid wrong guesses print `Out of attempts. The number was <secret>`.

Write a helper `check_guess(secret, guess)` returning `"low"`, `"high"` or `"correct"`.

### Sample input

Typed into the program (standard input):

```text
50
abc
0
75
90
82
```

### Expected output

```text
Guess 1: 50 is too low
Please enter a whole number
Out of range, use 1 to 100
Guess 2: 75 is too low
Guess 3: 90 is too high
Guess 4: 82 is correct! Solved in 4 attempts
```

### Hints

- `import random`, then `random.seed(42)` before `random.randint(1, 100)`.
- Keep an `attempts` counter and increase it only for valid guesses.
- `text.isdigit()` checks that the input is a whole number.
- Use `while attempts < 7:` and `return` (or `break`) on a correct guess.

### Acceptance checklist

- [ ] The secret number is the same on every run.
- [ ] Invalid input does not use up an attempt.
- [ ] The game ends after a correct guess or after 7 valid attempts.
- [ ] Output matches the expected output.

---

## T02-E09 - Challenge: Roman numerals both ways

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Algorithms, lookup tables, validation by round trip

**Data files:** none (all data is given in the exercise)

### Problem

Write `to_roman(n)` for 1 to 3999 (raise `ValueError` outside this range) and `from_roman(text)` that returns the number, or `None` when the text is not a correct Roman numeral (so `IIII`, `IC`, `VX` and `ABC` are rejected). Reading is case-insensitive. Read lines until the input ends, skip blank lines and print `<token> -> <result>`: a whole number is converted to Roman (`out of range (1-3999)` if outside the range), anything else is converted from Roman (`invalid` if it is not correct).

### Sample input

Typed into the program (standard input):

```text
4
9
14
1994
2026
MCMXCIV
xlii
3999
4000
IIII
IC
```

### Expected output

```text
4 -> IV
9 -> IX
14 -> XIV
1994 -> MCMXCIV
2026 -> MMXXVI
MCMXCIV -> 1994
xlii -> 42
3999 -> MMMCMXCIX
4000 -> out of range (1-3999)
IIII -> invalid
IC -> invalid
```

### Hints

- Use an ordered list of `(value, symbol)` pairs including the subtractive pairs: 900 `CM`, 400 `CD`, 90 `XC`, 40 `XL`, 9 `IX`, 4 `IV`.
- To Roman: for each pair, subtract the value from `n` while `n >= value`, appending the symbol.
- From Roman: if a symbol is smaller than the next one, subtract it; otherwise add it.
- Validate by converting the result back with `to_roman` and comparing with the (upper-cased) input.

### Acceptance checklist

- [ ] 1994 gives `MCMXCIV` and back again.
- [ ] Lower-case input is accepted.
- [ ] `IIII`, `IC` and out-of-range numbers are rejected without crashing.
- [ ] Output matches the expected output.

---

## T02-E10 - Challenge: tic-tac-toe referee

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Lists, state, helper functions, validation

**Data files:** none (all data is given in the exercise)

### Problem

Read moves from standard input, one cell number (1 to 9) per line; `X` plays first and the players alternate. Cells are numbered left to right, top to bottom. Write `winner(board)` (returns `"X"`, `"O"` or `None`; the board is a list of 9 single characters with `" "` for empty), `render(board)` and `play(moves)` which returns `(board, result, messages)`.

- Invalid moves do not change the board or the current player and add one message: `Invalid move <m>: not a number`, `Invalid move <m>: must be 1-9` or `Invalid move <m>: cell taken`.
- Stop processing moves once someone has won or the board is full.
- Result is `X wins`, `O wins`, `Draw` or `Game in progress`.

Print the messages, then the board (empty cells show their number), then the result. Board layout is shown in the expected output.

### Sample input

Typed into the program (standard input):

```text
10
5
5
1
abc
3
2
7
4
```

### Expected output

```text
Invalid move 10: must be 1-9
Invalid move 5: cell taken
Invalid move abc: not a number
 O | O | X
---+---+---
 4 | X | 6
---+---+---
 X | 8 | 9
X wins
```

### Hints

- Keep the 8 winning triples of indexes in a list: rows, columns and the two diagonals (index = cell number minus 1).
- A line wins when all three cells are equal and not `" "`.
- Use a variable `player` and swap it only after a valid move.
- `" | ".join(row)` builds a row; `"---+---+---"` separates rows.

### Acceptance checklist

- [ ] Invalid moves are reported and the same player moves again.
- [ ] Moves after the game is over are ignored.
- [ ] Rows, columns and both diagonals are detected.
- [ ] Draw and in-progress results are correct.
- [ ] Output matches the expected output.

---
