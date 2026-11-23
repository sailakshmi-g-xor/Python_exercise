# Topic 04: Exception handling: exercises

Work from the topic folder (the one that contains `data/`). Put your own scripts in a folder of your choice, open data files as `data/<name>` when you run from the topic folder, and write any output files into an `output/` folder (create it with `pathlib`), never into `data/`.

Expected output below was produced by running the trainer solutions with Python 3.12.

## T04-E01 - Safe division

**Level:** Easy  |  **Estimated time:** 10 minutes  |  **Practises:** try/except with specific exceptions

**Data files:** none (all data is given in the exercise)

### Problem

Read lines from standard input until the input ends; skip blank lines. Each line should hold two numbers separated by a space. Write `divide_line(line)` that returns a message string:

- Normal case: `<a> / <b> = <result>` using `:g` formatting for all three numbers (so `10.0` shows as `10`).
- Division by zero: `Cannot divide by zero`.
- Anything else wrong (not numbers, or not exactly two items): `Invalid input: expected two numbers`.

Use `try`, specific `except` clauses and `else`; do not use a bare `except:`. Print the message for every line.

### Sample input

Typed into the program (standard input):

```text
10 2
7 0
x 3
5
7 2
1 2 3
```

### Expected output

```text
10 / 2 = 5
Cannot divide by zero
Invalid input: expected two numbers
Invalid input: expected two numbers
7 / 2 = 3.5
Invalid input: expected two numbers
```

### Hints

- `float("x")` raises `ValueError`; dividing by zero raises `ZeroDivisionError`.
- `a_text, b_text = line.split()` raises `ValueError` when there are not exactly two items.
- Put the code that can fail in `try`; put the success message in `else`.
- Catch the more specific exception types, never a bare `except:`.

### Acceptance checklist

- [ ] Each of the three situations gives its own message.
- [ ] No bare `except:` is used.
- [ ] The program keeps going after an error.
- [ ] Output matches the expected output.

---

## T04-E02 - Parse sensor readings

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** ValueError when converting, collecting bad lines

**Data files:** `data/readings.txt`

### Problem

`data/readings.txt` holds temperature readings, one per line, but some lines are not numbers. Write `parse_readings(lines)` that returns `(values, bad)`: `values` is a list of floats, `bad` is a list of `(line_number, text)` for lines that cannot be converted (line numbers start at 1; text is stripped). Print: the number of lines, the number of valid readings, the list of invalid line numbers, each invalid line as `  line <n>: <text as repr>`, the average with two decimals, and the minimum and maximum.

### Sample input

`data/readings.txt` (30 lines).

### Expected output

```text
Lines: 30
Valid: 26
Invalid lines: [4, 7, 17, 23]
  line 4: 'N/A'
  line 7: 'abc'
  line 17: 'error'
  line 23: ''
Average: 26.99
Min: 21.5  Max: 120.5
```

### Hints

- `float(" 25.1 ")` works: surrounding spaces are allowed, but an empty string or `"abc"` raises `ValueError`.
- Use `enumerate(lines, start=1)` for line numbers.
- Read the file with `Path(...).read_text(encoding="utf-8").splitlines()`.
- Compute statistics only from the valid values.

### Acceptance checklist

- [ ] The conversion is wrapped in `try/except ValueError`.
- [ ] Blank or whitespace-only lines are reported as invalid.
- [ ] Line numbers start at 1.
- [ ] Output matches the expected output.

---

## T04-E03 - Exception tour

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** Common built-in exceptions and the hierarchy

**Data files:** none (all data is given in the exercise)

### Problem

Write `risky_calls()` returning a list of `(label, function)` pairs, one for each of these expressions (each function takes no arguments and runs the expression): `int('abc')`, `[1, 2, 3][5]`, `{'a': 1}['b']`, `10 / 0`, `open('missing_file.txt')`, `'5' + 5`, `None.upper()`. Write `describe(func)` which calls `func` and returns `"<ExceptionName>: <message>"` or `"no error"`. Print each label (left-aligned width 26), `-> ` and the description. Then print the four `issubclass` facts shown in the expected output.

### Sample input

No input.

### Expected output

```text
int('abc')                -> ValueError: invalid literal for int() with base 10: 'abc'
[1, 2, 3][5]              -> IndexError: list index out of range
{'a': 1}['b']             -> KeyError: 'b'
10 / 0                    -> ZeroDivisionError: division by zero
open('missing_file.txt')  -> FileNotFoundError: [Errno 2] No such file or directory: 'missing_file.txt'
'5' + 5                   -> TypeError: can only concatenate str (not "int") to str
None.upper()              -> AttributeError: 'NoneType' object has no attribute 'upper'
KeyError is a LookupError: True
IndexError is a LookupError: True
ZeroDivisionError is an ArithmeticError: True
FileNotFoundError is an OSError: True
```

### Hints

- `lambda: int("abc")` wraps an expression in a function.
- `except Exception as exc:` and then `type(exc).__name__` and `str(exc)`.
- Messages come from Python 3.12; other versions may word some of them differently.
- `issubclass(KeyError, LookupError)` is `True`.

### Acceptance checklist

- [ ] Seven different exception types are shown.
- [ ] `describe` returns text; printing happens in the main program.
- [ ] You can explain why `KeyError` and `IndexError` can both be caught as `LookupError`.
- [ ] Output matches the expected output.

---

## T04-E04 - try, except, else, finally

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** Order of execution

**Data files:** `data/readings.txt` (and a file name that does not exist)

### Problem

Write `read_first_line(path)` that returns `(first_line, steps)`. `steps` is a list of strings recording the blocks that ran, in order: `try: opening file`, then either `except: file not found` (when the file is missing, and the result is `None`) or `else: read succeeded`, and always `finally: always runs` at the end. Also write `finally_before_return()` whose `try` block does `return "value from try", log` and whose `finally` block appends `finally ran before return` to `log`.

Main program: run `read_first_line` on `data/readings.txt` and on `data/nope.txt` and print the result and each step (indented two spaces), then print the value and log from `finally_before_return()` as `value | log`.

### Sample input

No input.

### Expected output

```text
existing file: result='21.5'
  try: opening file
  else: read succeeded
  finally: always runs
missing file: result=None
  try: opening file
  except: file not found
  finally: always runs
value from try | ['finally ran before return']
```

### Hints

- The `else` block runs only when `try` finished without an exception.
- The `finally` block runs in every case, even after a `return`.
- Catch `FileNotFoundError` only.
- Use `with open(...)` inside the `try`.

### Acceptance checklist

- [ ] For a missing file the `else` step is absent and the `except` step is present.
- [ ] `finally` appears in both cases.
- [ ] You can explain why the log of `finally_before_return` is not empty.
- [ ] Output matches the expected output.

---

## T04-E05 - Validate input by raising

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** raise, ValueError vs TypeError, helpful messages

**Data files:** none (all data is given in the exercise)

### Problem

Write two validators that raise exceptions instead of returning flags.

`validate_age(value)`: accepts an `int`, or a string of digits (surrounding spaces allowed); returns an `int`. Raise `TypeError` for any other type (floats, `None`, `bool`, lists). Raise `ValueError` with the message `age must be a whole number, got <repr>` for non-numeric text, and `age must be between 0 and 120, got <n>` for out-of-range numbers (a string like `"-5"` is not a whole number).

`validate_password(password)`: needs at least 8 characters, a digit and an upper-case letter. Raise one `ValueError` listing all missing requirements, for example `password needs at least 8 characters, a digit, an upper-case letter`.

Write `attempt(check, value)` that returns `OK: <result as repr>` or `<ExceptionName>: <message>`. Print the results in the format shown.

### Sample input

```python
ages = (25, "42", "abc", -5, 130, 3.5, None)
passwords = ("Secret123", "short", "alllowercase1", "NoDigitsHere")
```

### Expected output

```text
age 25     -> OK: 25
age '42'   -> OK: 42
age 'abc'  -> ValueError: age must be a whole number, got 'abc'
age -5     -> ValueError: age must be between 0 and 120, got -5
age 130    -> ValueError: age must be between 0 and 120, got 130
age 3.5    -> TypeError: age must be an int or a string, not float
age None   -> TypeError: age must be an int or a string, not NoneType
password 'Secret123'      -> OK: 'Secret123'
password 'short'          -> ValueError: password needs at least 8 characters, a digit, an upper-case letter
password 'alllowercase1'  -> ValueError: password needs an upper-case letter
password 'NoDigitsHere'   -> ValueError: password needs a digit
```

### Hints

- `raise ValueError("message")` stops the function and passes the error to the caller.
- `isinstance(value, (int, str))` checks the type; remember `True` is an `int` in Python.
- Collect the problems in a list and join them with `", ".join(...)`.
- `except (TypeError, ValueError) as exc:` catches both.

### Acceptance checklist

- [ ] Wrong types raise `TypeError`, wrong values raise `ValueError`.
- [ ] The password error lists every problem at once.
- [ ] Validators raise; they never print.
- [ ] Output matches the expected output.

---

## T04-E06 - Custom exceptions for a bank account

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** Exception classes, attributes, hierarchy

**Data files:** none (all data is given in the exercise)

### Problem

Define these exceptions:

- `BankError(Exception)` - base class.
- `InvalidAmountError(BankError)` and `AccountFrozenError(BankError)`.
- `InsufficientFundsError(BankError)` - created with `(balance, amount)`, stores attributes `balance`, `amount` and `shortfall`, and has the message `Insufficient funds: balance 70.00, requested 100.00 (short by 30.00)`.

Write a class `Account(owner, balance=0)` with a `frozen` flag and methods `deposit(amount)` and `withdraw(amount)`. A frozen account raises `AccountFrozenError` (message `Account of <owner> is frozen`); an amount of zero or less raises `InvalidAmountError` (message `Amount must be positive, got <amount>`); withdrawing more than the balance raises `InsufficientFundsError`. A failed operation must not change the balance.

Run the script of operations below on `Account("Asha")`. Catch `InsufficientFundsError` separately (also print its `shortfall` attribute) and everything else with one `except BankError`.

### Sample input

```text
deposit 100, withdraw 30, withdraw 100, deposit -5, freeze, deposit 10, withdraw 10
```

### Expected output

```text
deposit 100: balance 100.00
withdraw 30: balance 70.00
withdraw 100: InsufficientFundsError: Insufficient funds: balance 70.00, requested 100.00 (short by 30.00)
  shortfall attribute: 30.00
deposit -5: InvalidAmountError: Amount must be positive, got -5
freeze: account frozen
deposit 10: AccountFrozenError: Account of Asha is frozen
withdraw 10: AccountFrozenError: Account of Asha is frozen
```

### Hints

- `class MyError(BaseError): pass` is enough for simple exceptions.
- Call `super().__init__(message)` in a custom `__init__` so `str(exc)` shows your message.
- Order `except` clauses from most specific to most general.
- `getattr(account, "deposit")(100)` calls a method by name.

### Acceptance checklist

- [ ] All custom exceptions inherit from `BankError`.
- [ ] `InsufficientFundsError` carries `balance`, `amount` and `shortfall`.
- [ ] The balance is unchanged after any failed operation.
- [ ] Output matches the expected output.

---

## T04-E07 - Ask until valid

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** while loop, try/except/else, retry limit, custom exception

**Data files:** none (all data is given in the exercise)

### Problem

Write `read_int(prompt, low, high, max_tries=3, read=input, out=print)` that asks for a whole number between `low` and `high`. Each time it asks, call `out(prompt)` (print the prompt on its own line), then `read()` to get the text. Messages: `Not a whole number, try again` for text that is not an integer, `Must be between <low> and <high>` for an out-of-range number. After `max_tries` invalid answers raise your own `TooManyAttemptsError`. Return the number as soon as it is valid.

Main program: read an age (0 to 120) and print `Age accepted: <age>`. Then ask for a month (1 to 12) inside `try`; if `TooManyAttemptsError` is raised print `Giving up: too many invalid attempts`.

### Sample input

Typed into the program (standard input):

```text
abc
150
42
x
0
13
```

### Expected output

```text
Enter age (0-120):
Not a whole number, try again
Enter age (0-120):
Must be between 0 and 120
Enter age (0-120):
Age accepted: 42
Enter month (1-12):
Not a whole number, try again
Enter month (1-12):
Must be between 1 and 12
Enter month (1-12):
Must be between 1 and 12
Giving up: too many invalid attempts
```

### Hints

- The extra parameters `read` and `out` let tests replace `input` and `print` with fake functions.
- Count invalid answers with a counter; compare it with `max_tries`.
- The `else` block of `try` is a good place for the range check.
- Define `class TooManyAttemptsError(Exception): pass`.

### Acceptance checklist

- [ ] Both kinds of invalid input are handled and reported.
- [ ] After three invalid answers the custom exception is raised.
- [ ] A valid answer on a later try is returned.
- [ ] Output matches the expected output.

---

## T04-E08 - Logging instead of print

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** logging levels, handlers, formatters

**Data files:** `data/readings.txt`

### Problem

Process `data/readings.txt` with the `logging` module. Write `process_readings(lines, logger)` that returns the list of accepted floats and logs:

- `WARNING` `line <n>: empty line` for blank lines.
- `WARNING` `line <n>: not a number: <text as repr>` for lines that are not numbers.
- `WARNING` `line <n>: reading <value> out of range` for values outside -20 to 60.
- `DEBUG` `line <n>: accepted <value>` for good lines.
- `INFO` `Processed <total> lines: <valid> valid, <skipped> skipped` at the end.

Write `average(values, logger)` that returns the mean, or logs an `ERROR` `Could not compute average: <exception>` and returns `None` when there are no values (catch `ZeroDivisionError`).

Set up a logger named `readings` with format `%(levelname)s:%(name)s:%(message)s`: a console handler showing `INFO` and above, and a file handler writing everything (`DEBUG` and above) to `output/readings.log`. In the main program print the average, call `average([], logger)` to show the error, and print the number of lines in the log file.

### Sample input

`data/readings.txt` (30 lines).

### Expected output

```text
WARNING:readings:line 4: not a number: 'N/A'
WARNING:readings:line 7: not a number: 'abc'
WARNING:readings:line 11: reading 120.5 out of range
WARNING:readings:line 17: not a number: 'error'
WARNING:readings:line 23: empty line
INFO:readings:Processed 30 lines: 25 valid, 5 skipped
Average: 23.25
ERROR:readings:Could not compute average: division by zero
Lines in log file: 32
```

### Hints

- Use `%s`-style arguments: `logger.warning("line %d: empty line", number)`; do not build the string yourself.
- Set the logger level to `DEBUG`; set the handler levels separately.
- `logging.StreamHandler(sys.stdout)` and `logging.FileHandler(path, mode="w", encoding="utf-8")`.
- `logger.exception("...")` inside an `except` block also records the traceback (not used here because tracebacks contain file paths).

### Acceptance checklist

- [ ] The console shows no `DEBUG` lines but the file does.
- [ ] Messages use the exact format and levels listed.
- [ ] Log setup is in its own function (no duplicated handlers when called twice).
- [ ] Output matches the expected output.

---

## T04-E09 - Challenge: retry decorator with backoff

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Decorators, closures, re-raising, exponential backoff

**Data files:** none (all data is given in the exercise)

### Problem

Write a decorator factory `retry(attempts=3, delay=1.0, backoff=2.0, exceptions=(Exception,), sleep=time.sleep)`. The decorated function is called; if it raises one of `exceptions`, wait with `sleep(wait)` and try again. The first wait is `delay`, and each following wait is multiplied by `backoff`. If the last attempt also fails, re-raise that exception (no sleep after the last attempt). Exceptions that are not in `exceptions` must propagate immediately without retrying. Keep the function name and docstring (`functools.wraps`).

Also write `make_flaky(failures)` returning a function that raises `ConnectionError("temporary failure on call <n>")` for its first `failures` calls and then returns `data after <n> calls`.

Main program (never really sleep: pass a `sleep` function that records the waits in a list):
1. `attempts=4, delay=1.0, backoff=2.0` on a service that fails twice: print the result and the recorded sleeps.
2. `attempts=3, delay=0.5` on a service that always fails: print `Gave up: <message>` and the sleeps.
3. A function raising `ValueError` decorated to retry only on `ConnectionError`: print the error, the number of calls and the sleeps, then the function's `__name__`.

### Sample input

No input.

### Expected output

```text
Result: data after 3 calls
Sleeps: [1.0, 2.0]
Gave up: temporary failure on call 3
Sleeps: [0.5, 1.0]
Not retried: bad input, retrying will not help | calls: 1 | sleeps: []
Name kept: broken
```

### Hints

- A decorator factory is three nested functions: `retry(...)` returns `decorator(func)` which returns `wrapper(*args, **kwargs)`.
- Use `for attempt in range(1, attempts + 1):` and a bare `raise` on the last attempt.
- `except exceptions:` accepts a tuple of exception classes.
- Passing `sleep` as a parameter makes the code testable without waiting.

### Acceptance checklist

- [ ] Waits are 1.0 then 2.0 for the first demo, and 0.5 then 1.0 for the second.
- [ ] No sleep happens after the final failed attempt.
- [ ] Unlisted exception types are not retried.
- [ ] `wrapper.__name__` is the original function name.
- [ ] Output matches the expected output.

---

## T04-E10 - Challenge: robust order processor

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Exception hierarchy, chaining with from, ExceptionGroup and except*

**Data files:** `data/orders.csv`

### Problem

`data/orders.csv` has columns `order_id,customer,quantity,unit_price`, and some rows are bad. Build an order processor.

1. Exceptions: `OrderError(Exception)` with attributes `row` (data row number, starting at 1) and `order_id`; subclasses `MissingFieldError` and `InvalidValueError`.
2. `parse_order(row_number, row)` returns a dictionary `order_id, customer, quantity, unit_price, total` (total rounded to 2 decimals). Checks in this order: empty `customer` or empty `unit_price` raise `MissingFieldError` with the messages `customer is missing` / `unit_price is missing`. Then `quantity` must be a whole number (`quantity must be a whole number (got 'two')`) and positive (`quantity must be positive (got 0)`); then `unit_price` must be a number (`unit_price must be a number (got 'abc')`) and not negative (`unit_price must not be negative (got -5.0)`). Use `raise ... from exc` when you convert a `ValueError` into your own exception.
3. `process_orders(path)` returns `(orders, errors)`; a bad row must not stop the processing of the other rows.
4. Main program: print `Row <n> (order <id>): <message>` for each error, then `Processed <n> rows: <ok> ok, <bad> failed`, then `Total value of valid orders: <value>` (two decimals). If there are errors, raise `ExceptionGroup("order errors", errors)` and handle it with two `except*` clauses, printing `except* MissingFieldError: <n> errors` and `except* InvalidValueError: <n> errors`.

### Sample input

`data/orders.csv` (25 data rows).

### Expected output

```text
Row 4 (order 1004): quantity must be a whole number (got 'two')
Row 6 (order 1006): customer is missing
Row 7 (order 1007): quantity must be positive (got 0)
Row 8 (order 1008): unit_price must not be negative (got -5.0)
Row 10 (order 1010): unit_price is missing
Row 13 (order 1013): unit_price must be a number (got 'abc')
Row 16 (order 1016): quantity must be positive (got -3)
Row 20 (order 1020): quantity must be a whole number (got '2.5')
Processed 25 rows: 17 ok, 8 failed
Total value of valid orders: 1520.57
except* MissingFieldError: 2 errors
except* InvalidValueError: 6 errors
```

### Hints

- `raise InvalidValueError(...) from exc` keeps the original `ValueError` in `__cause__`.
- `int("2.5")` raises `ValueError`, so a decimal quantity is invalid.
- `except* SomeError as group:` receives an `ExceptionGroup`; use `group.exceptions` (Python 3.11 and newer).
- Test `parse_order` on single rows before you run the whole file.

### Acceptance checklist

- [ ] A bad row never stops the processing of later rows.
- [ ] The checks run in the order stated, so each bad row gets the stated message.
- [ ] Converted errors keep their cause (`__cause__` is a `ValueError`).
- [ ] The `ExceptionGroup` is handled by two `except*` clauses.
- [ ] Output matches the expected output.

---
