# Topic 13: Complex Programs - Exercises

These are larger projects of 45 to 90 minutes each. Build each one as a small **package**: a
folder containing `__init__.py`, a few modules and a `__main__.py`. You then run it with
`python3 -m package_name`, or `python -m package_name` on Windows. The suggested module layout is
a guide. Splitting the work into separate pieces (data model, storage, logic, user interface) is
part of the exercise.

Sample data lives in the topic's `data/` folder. The sample commands are run from inside a
`solutions/` folder that sits next to `data/`, so data paths start with `../data/`. Put your own
packages in a folder next to `data/` and use the same paths.

Programs that read typed input are shown with the exact lines that were typed, followed by the
output. Each program echoes typed input when input is piped in, so the transcript you see here
matches what you see at a keyboard.

Use only the standard library.

---

## T13-E01 To-do app with a command line menu

**Level:** Easy | **Time:** 45 minutes | **Package:** `t13_e01_todo`

### Problem statement

Build a to-do list manager with a numbered menu:

1. Add task. Ask for a title and a priority (`high`, `medium` or `low`). Pressing Enter gives `medium`.
2. List tasks. Show open tasks first, then sort by priority, then by id. Show `[x]` for done
   and `[ ]` for open, and end with a count line.
3. Complete a task by id.
4. Delete a task by id.
5. Quit. Save and exit.

Tasks are saved to a JSON file, chosen with `--file` (default `todo.json`), after every change,
and loaded again at start-up. Bad input such as an unknown id, a non-number or a wrong menu choice
prints a friendly message, and the menu keeps going. End of input (Ctrl+D or Ctrl+Z) behaves like Quit.

Suggested modules: `models.py` (`Task` dataclass, `TodoList`), `storage.py` (`load`, `save`),
`cli.py` (menu loop), `__main__.py`.

### Sample input and expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e01_todo --file my_todo.json
```

Typed input, one line at a time (an empty line means just press Enter):

```text
1
Buy milk
low
1
Finish report
high
1
Call plumber
(Enter)
2
3
2
4
9
4
x
7
2
5
```

Expected output (the program echoes typed input when it is piped in, which is how this transcript was produced; at a real keyboard you see the same text):

```text
Loaded 0 task(s) from my_todo.json

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 1
Title: Buy milk
Priority (high/medium/low) [medium]: low
Added task 1.

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 1
Title: Finish report
Priority (high/medium/low) [medium]: high
Added task 2.

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 1
Title: Call plumber
Priority (high/medium/low) [medium]: 
Added task 3.

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 2
[ ]  2. Finish report (high)
[ ]  3. Call plumber (medium)
[ ]  1. Buy milk (low)
3 open, 0 done

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 3
Task id: 2
Completed: Finish report

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 4
Task id: 9
Error: no task with id 9

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 4
Task id: x
'x' is not a number.

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 7
Please choose 1-5.

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 2
[ ]  3. Call plumber (medium)
[ ]  1. Buy milk (low)
[x]  2. Finish report (high)
2 open, 1 done

1) Add task  2) List tasks  3) Complete task  4) Delete task  5) Quit
Choice: 5
Saved 3 task(s). Bye.
```

### Hints

- Use `@dataclass` with `asdict` to turn a task into a dict for JSON, and `Task(**data)` to turn it back.
- The next id is `max(existing ids) + 1`, so ids are never reused after a delete.
- Keep `input()` and `print()` in `cli.py` only. `TodoList` raises exceptions and the menu catches them.
- Save to a temporary file first and rename it over the real file. A crash then cannot leave a half-written file.

### Acceptance checklist

- [ ] Restarting the program shows the tasks from the previous run.
- [ ] Invalid input never crashes the program.
- [ ] `TodoList` can be tested without typing anything, because it does no input or output itself.

---

## T13-E02 Student grade manager

**Level:** Easy | **Time:** 50 minutes | **Package:** `t13_e02_grades`

### Problem statement

Read `data/grades.csv`, which has the columns `student,subject,score`, and build a command line
tool with `argparse` subcommands:

- `report` prints a table of every student and subject, with the average and letter grade, best
  student first. Then it prints the mean, median and range for each subject and the students
  averaging below 60.
- `student NAME` prints one student's scores and average.
- `top N` prints the best N students.
- `add NAME SUBJECT SCORE` adds or updates a score and saves the CSV. A score outside 0 to 100 is rejected.

The letter grades are A for 90 and above, B for 80 and above, C for 70 and above, D for 60 and
above, and F below 60. Rows with a missing or invalid score are skipped, with a warning that
gives the line number.

Suggested modules: `models.py` (`Student`, `letter_grade`), `gradebook.py` (`GradeBook` with CSV
load and save and statistics), `cli.py`.

### Sample input and expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e02_grades --file ../data/grades.csv report
```

Expected output:

```text
Warning: line 15: skipped bad score '' for Eva
Warning: line 19: skipped bad score 'abc' for Finn
Student   English     Math  Physics    Avg  Grade
-------------------------------------------------
Dev            91       99       94   94.7  A
Ana            78       92       85   85.0  B
Eva            84       81        -   82.5  B
Finn            -       73       79   76.0  C
Ben            88       67       72   75.7  C
Chloe          70       55       48   57.7  F

English: mean 82.2, median 84, range 70-91 (5 scores)
Math: mean 77.8, median 77, range 55-99 (6 scores)
Physics: mean 75.6, median 79, range 48-94 (5 scores)
Below 60 average: Chloe
```

Command (run inside `solutions/`):

```text
python3 -m t13_e02_grades --file ../data/grades.csv student Ana
```

Expected output:

```text
Warning: line 15: skipped bad score '' for Eva
Warning: line 19: skipped bad score 'abc' for Finn
  English     78
  Math        92
  Physics     85
  average 85.0 -> B
```

Command (run inside `solutions/`):

```text
python3 -m t13_e02_grades --file ../data/grades.csv top 3
```

Expected output:

```text
Warning: line 15: skipped bad score '' for Eva
Warning: line 19: skipped bad score 'abc' for Finn
1. Dev 94.7
2. Ana 85.0
3. Eva 82.5
```

Command (run inside `solutions/`):

```text
python3 -m t13_e02_grades --file ../data/grades.csv add Chloe Physics 101
```

Expected output:

```text
Warning: line 15: skipped bad score '' for Eva
Warning: line 19: skipped bad score 'abc' for Finn
Error: score must be 0-100, got 101.0
```

Exit code: 1

### Hints

- `csv.DictReader` gives you each row as a dict. Use `enumerate(reader, start=2)` to get line numbers, because line 1 is the header.
- `statistics.mean` and `statistics.median` do the maths.
- Rank with `sorted(students, key=lambda s: (-s.average(), s.name))`, so ties are broken by name.

### Acceptance checklist

- [ ] The bad rows for Eva and Finn produce warnings instead of crashing the program.
- [ ] A missing subject shows as `-` in the table.
- [ ] `add` with a score of 101 is rejected and the file is left unchanged.

---

## T13-E03 URL shortener (in memory)

**Level:** Medium | **Time:** 50 minutes | **Package:** `t13_e03_url_shortener`

### Problem statement

Build an in-memory URL shortener with a small command prompt:

- `shorten <url> [alias]` accepts only `http` and `https` URLs, and lowercases the scheme and
  host. Without an alias it generates a code by base62-encoding a counter that starts at 1000.
  Shortening the same URL twice returns the same code. An alias must be 3 to 20 letters, digits,
  `-` or `_`, and must not be taken already.
- `open <code>` prints the long URL and counts a click. A full short URL is accepted too.
- `delete <code>` and `stats` (the most clicked links first), plus `help` and `quit`.

Suggested modules: `codec.py` (`encode`, `decode` in base62), `shortener.py` (`URLShortener`,
`Link`, `ShortenerError`), `cli.py`.

### Sample input and expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e03_url_shortener
```

Typed input, one line at a time (an empty line means just press Enter):

```text
shorten https://docs.python.org/3/library/collections.html
shorten https://EXAMPLE.com/a/b?q=1
shorten https://github.com/python/cpython py-src
shorten https://docs.python.org/3/library/collections.html
shorten ftp://files.example.com
shorten https://example.org py-src
open py-src
open py-src
open zzz
stats
delete g9
stats
quit
```

Expected output (the program echoes typed input when it is piped in, which is how this transcript was produced; at a real keyboard you see the same text):

```text
URL shortener. Type 'help' for commands.
> shorten https://docs.python.org/3/library/collections.html
https://sho.rt/g8 -> https://docs.python.org/3/library/collections.html
> shorten https://EXAMPLE.com/a/b?q=1
https://sho.rt/g9 -> https://example.com/a/b?q=1
> shorten https://github.com/python/cpython py-src
https://sho.rt/py-src -> https://github.com/python/cpython
> shorten https://docs.python.org/3/library/collections.html
https://sho.rt/g8 -> https://docs.python.org/3/library/collections.html
> shorten ftp://files.example.com
Error: not a valid http(s) URL: 'ftp://files.example.com'
> shorten https://example.org py-src
Error: alias 'py-src' is already taken
> open py-src
redirect to https://github.com/python/cpython
> open py-src
redirect to https://github.com/python/cpython
> open zzz
Error: unknown code 'zzz'
> stats
3 link(s)
  py-src       2 click(s)  https://github.com/python/cpython
  g8           0 click(s)  https://docs.python.org/3/library/collections.html
  g9           0 click(s)  https://example.com/a/b?q=1
> delete g9
deleted g9
> stats
2 link(s)
  py-src       2 click(s)  https://github.com/python/cpython
  g8           0 click(s)  https://docs.python.org/3/library/collections.html
> quit
Bye.
```

### Hints

- Base62 uses the alphabet `0-9a-z A-Z`. Encoding repeats `divmod(n, 62)`, like converting to binary.
- `urllib.parse.urlparse(url)` gives you `.scheme` and `.netloc` for validation.
- Keep two dicts: code to link, and URL to link.
- A custom alias might match a code the counter will generate later. Skip codes that are already taken.
- `shlex.split(line)` splits a command line into words.

### Acceptance checklist

- [ ] `decode(encode(n)) == n` for many values of `n`.
- [ ] Invalid URLs, taken aliases and unknown codes give clear errors.
- [ ] `stats` sorts by clicks, then by code.

---

## T13-E04 Expense tracker with CSV and JSON storage

**Level:** Medium | **Time:** 60 minutes | **Package:** `t13_e04_expense_tracker`

### Problem statement

Build an expense tracker. The data file is given with `--file` and can be `.csv` or `.json`; the
file extension decides the format. It has these subcommands:

- `add DATE CATEGORY AMOUNT [--note TEXT]` validates the input: the date must be `YYYY-MM-DD`,
  the amount must be a positive number, and the category must not be empty. Categories are
  stored in lowercase.
- `list [--month YYYY-MM] [--category NAME]` lists matching expenses and their total.
- `summary [--month YYYY-MM] [--budget AMOUNT]` prints category totals, largest first, each with
  a text bar chart. Without a month, it also prints the total for each month. With a budget, it
  says whether you are under or over.
- `export OUTPUT` saves all the expenses in the other format.

Use `decimal.Decimal` for money, never `float`.

Suggested modules: `models.py` (`Expense` with validation), `storage.py` (CSV and JSON load and
save), `reports.py` (filters and totals), `cli.py`.

### Sample input and expected output

Each command below ran on a fresh copy of `data/expenses.csv`.

Command (run inside `solutions/`):

```text
python3 -m t13_e04_expense_tracker --file ../data/expenses.csv add 2026-10-28 Books 19.99 --note "python book"
```

Expected output:

```text
Added 19.99 for books on 2026-10-28. 13 expense(s) in ../data/expenses.csv
```

Command (run inside `solutions/`):

```text
python3 -m t13_e04_expense_tracker --file ../data/expenses.csv add 2026-10-32 books 5
```

Expected output:

```text
Error: date must be YYYY-MM-DD, got '2026-10-32'
```

Exit code: 1

Command (run inside `solutions/`):

```text
python3 -m t13_e04_expense_tracker --file ../data/expenses.csv list --category groceries
```

Expected output:

```text
2026-09-02  groceries      54.20  weekly shop
2026-09-12  groceries      61.75  weekly shop
2026-09-26  groceries      48.10
2026-10-04  groceries      57.30  weekly shop
4 expense(s), total 221.35
```

Command (run inside `solutions/`):

```text
python3 -m t13_e04_expense_tracker --file ../data/expenses.csv summary
```

Expected output:

```text
Summary for all months
  rent         1700.00  ################....
  groceries     221.35  ##..................
  utilities      72.45  #...................
  eating out     55.30  #...................
  transport      50.80  ....................
  TOTAL        2099.90
By month:
  2026-09   1085.45
  2026-10   1014.45
```

Command (run inside `solutions/`):

```text
python3 -m t13_e04_expense_tracker --file ../data/expenses.csv summary --month 2026-10 --budget 1000
```

Expected output:

```text
Summary for 2026-10
  rent          850.00  #################...
  utilities      72.45  #...................
  groceries      57.30  #...................
  eating out     31.80  #...................
  transport       2.90  ....................
  TOTAL        1014.45
Budget 1000.00: OVER by 14.45
```

Command (run inside `solutions/`):

```text
python3 -m t13_e04_expense_tracker --file ../data/expenses.csv export expenses.json
```

Expected output:

```text
Exported 12 expense(s) to expenses.json
```

### Hints

- `Decimal("54.20")` is exact, while `0.1 + 0.2` in floats is not. Store amounts as strings in JSON.
- `date.fromisoformat` raises `ValueError` for impossible dates such as `2026-10-32`.
- `collections.defaultdict(lambda: Decimal("0.00"))` makes adding up totals easy.
- Give each subcommand its own handler with `set_defaults(func=...)` so `main` stays short.

### Acceptance checklist

- [ ] Exporting to JSON and loading that file again gives the same expenses.
- [ ] Bad dates and amounts print an error and return exit code 1.
- [ ] Totals are exact: the grand total is `2099.90`, not `2099.8999999`.

---

## T13-E05 Text-based inventory with classes and file persistence

**Level:** Medium | **Time:** 60 minutes | **Package:** `t13_e05_inventory`

### Problem statement

Build a menu-driven inventory manager for a small shop. It loads from `data/inventory.json` and
saves back to the same file. The menu has these options:

1. List: a table of SKU, name, quantity, price and value, with `reorder` shown next to items at
   or below their reorder level, followed by the total stock value.
2. Add product. The SKU is stored in uppercase and must be unique.
3. Restock.
4. Sell. You cannot sell more than you have in stock.
5. Low stock report.
6. Save and quit.

Use custom exceptions (`InventoryError` and its subclasses `UnknownProduct`, `DuplicateProduct`
and `OutOfStock`) and keep a movement history (`add`, `restock` and `sell` entries) in the file.

Suggested modules: `models.py` (`Product`, `Inventory`, exceptions), `storage.py`, `cli.py`.

### Sample input and expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e05_inventory --file ../data/inventory.json
```

Typed input, one line at a time (an empty line means just press Enter):

```text
1
4
pen-blu
30
4
USB-32
10
3
MUG-LOGO
24
2
CAB-HDMI
HDMI cable
15
4.50
5
2
nb-a5
dup
1
1
1
5
9
6
```

Expected output (the program echoes typed input when it is piped in, which is how this transcript was produced; at a real keyboard you see the same text):

```text
Loaded 4 product(s) from ../data/inventory.json

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 1
SKU       Name              Qty   Price    Value
MUG-LOGO  Logo mug            0    6.25     0.00  reorder
NB-A5     A5 notebook        18    3.50    63.00  reorder
PEN-BLU   Blue pen          120    0.80    96.00
USB-32    USB stick 32GB      7    9.99    69.93
Stock value: 228.93

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 4
SKU: pen-blu
Amount: 30
Sold. Total 24.00. 90 left.

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 4
SKU: USB-32
Amount: 10
Error: only 7 x USB-32 in stock, cannot sell 10

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 3
SKU: MUG-LOGO
Amount: 24
MUG-LOGO now has 24.

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 2
SKU: CAB-HDMI
Name: HDMI cable
Quantity: 15
Price: 4.50
Reorder level: 5
Added CAB-HDMI.

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 2
SKU: nb-a5
Name: dup
Quantity: 1
Price: 1
Reorder level: 1
Error: SKU NB-A5 already exists

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 5
SKU       Name              Qty   Price    Value
NB-A5     A5 notebook        18    3.50    63.00  reorder

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 9
Please choose 1-6.

1) List  2) Add product  3) Restock  4) Sell  5) Low stock  6) Save and quit
Choice: 6
Saved to ../data/inventory.json. Units sold (all time): 30.
```

### Hints

- Give `Product` the properties `value` and `needs_reorder`, so the table code stays simple.
- Make every exception inherit from `InventoryError`, so the menu needs only one `except`.
- SKUs are not case-sensitive. Normalise them with `.strip().upper()` in one place.

### Acceptance checklist

- [ ] Overselling, unknown SKUs, duplicate SKUs and non-numeric input all show an error and the menu carries on.
- [ ] After quitting, the JSON file holds the new quantities and the history.
- [ ] Money values use `Decimal`.

---

## T13-E06 Bank account simulator with exceptions and decorators

**Level:** Medium | **Time:** 60 minutes | **Package:** `t13_e06_bank`

### Problem statement

Simulate a bank that runs a script of commands, one per line, from a file or from stdin. Lines
starting with `#` are comments. The commands are `open`, `deposit`, `withdraw`, `transfer`,
`interest`, `freeze`, `unfreeze`, `statement` and `summary`; see the sample file
`data/bank_commands.txt`. The bank has these rules:

- Account types are `basic`, `checking` and `savings`. A checking account may go up to 100 below
  zero. A savings account allows 3 withdrawals, and transfers out count as withdrawals.
- Write these decorators: `@validate_amount` (turns the amount into a positive `Decimal` or
  raises `InvalidAmount`), `@require_active` (raises `AccountFrozen` for a frozen account), and
  `@record(kind)` (adds `(kind, amount, balance)` to the history only when the operation succeeds).
- Write these exceptions, all subclasses of `BankError`: `InvalidAmount`, `InsufficientFunds`,
  `AccountFrozen`, `LimitExceeded` and `UnknownAccount`.
- A transfer is all or nothing. If the deposit fails, undo the withdrawal.
- A failing line prints its line number and the exception name, and the script carries on.

Suggested modules: `exceptions.py`, `decorators.py`, `accounts.py` (`Account`, `CheckingAccount`,
`SavingsAccount`, `Bank`), `cli.py`.

### Sample input

The script file `data/bank_commands.txt`:

```text
# Sample script for T13-E06. Lines starting with # are comments.
open checking alice 100
open savings bob 500
deposit alice 50
withdraw alice 200       # allowed: checking accounts may go 100 below zero
withdraw alice 100       # fails: would exceed the overdraft
transfer bob alice 120
withdraw bob 10
withdraw bob 10
withdraw bob 10          # fails: savings allows 3 withdrawals and the transfer counted
deposit carol 10         # fails: no such account
deposit alice -5         # fails: invalid amount
freeze bob
deposit bob 10           # fails: frozen
unfreeze bob
interest bob 2.5
statement alice
statement bob
summary
```

### Expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e06_bank ../data/bank_commands.txt
```

Expected output:

```text
opened checking account for alice, balance 100.00
opened savings account for bob, balance 500.00
alice balance 150.00
alice balance -50.00
line 6: InsufficientFunds: alice cannot withdraw 100.00: available 50.00
moved 120 from bob to alice
bob balance 370.00
bob balance 360.00
line 10: LimitExceeded: bob has used all 3 withdrawals
line 11: UnknownAccount: no account for carol
line 12: InvalidAmount: amount must be positive, got -5
bob is now frozen
line 14: AccountFrozen: account of bob is frozen
bob is now active
bob earned 9.00 interest, balance 369.00
statement for alice (checking)
  deposit     100.00  balance   100.00
  deposit      50.00  balance   150.00
  withdraw    200.00  balance   -50.00
  deposit     120.00  balance    70.00
statement for bob (savings)
  deposit     500.00  balance   500.00
  withdraw    120.00  balance   380.00
  withdraw     10.00  balance   370.00
  withdraw     10.00  balance   360.00
  interest      9.00  balance   369.00
alice    checking      70.00
bob      savings      369.00
total                 439.00
done, 5 error(s)
```

### Hints

- Decorators run from the top down, so the order you stack them in matters. Validate first, then
  check the freeze, and put `record` closest to the method so it only runs when the method succeeds.
- Use `functools.wraps` in every decorator so `deposit.__name__` stays `"deposit"`.
- Subclasses override `available()` (overdraft) and `_check_withdrawal()` (withdrawal limit). The
  `withdraw` method itself stays the same.

### Acceptance checklist

- [ ] The five failing lines in the sample produce five errors and the script still finishes.
- [ ] A failed transfer leaves both balances unchanged.
- [ ] Failed operations do not appear in the statement.

---

## T13-E07 Log analyser with regex and reports

**Level:** Medium | **Time:** 70 minutes | **Package:** `t13_e07_log_analyser`

### Problem statement

Analyse `data/access.log`, a web server log in Common Log Format:

```text
192.168.1.10 - - [21/Nov/2026:09:01:12 +0000] "GET /index.html HTTP/1.1" 200 5120
```

Parse every line with **one regular expression** that has named groups. Count lines that do not
match as malformed and report their line numbers. Print a report with these items:

- The number of requests and unique IPs, the bytes sent (`-` counts as 0) and the error rate (4xx and 5xx as a percentage).
- Counts for each status class, and the top N paths and top N IPs.
- Requests per hour as a text bar chart, with the busiest hour marked.
- Paths that returned 404, and suspicious IPs (3 or more 401 or 404 responses).

There are also two options: `--top N` and `--status CODE`, which analyses only that status. With
`--json FILE`, the summary is also written as JSON.

Suggested modules: `parser.py` (regex, `LogEntry`, `parse_lines`), `analysis.py` (`Counter`-based
statistics), `report.py` (text and JSON), `cli.py`.

### Sample input and expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e07_log_analyser ../data/access.log
```

Expected output:

```text
Requests:        28
Malformed lines: 2 [14, 28]
Unique IPs:      5
Bytes sent:      71,970
Error rate:      39.3%
Status classes:  2xx=14, 3xx=3, 4xx=9, 5xx=2

Top paths:
    5  /api/orders
    5  /login
    3  /index.html
Top IPs:
    8  192.168.1.10
    7  10.0.0.5
    6  192.168.1.22
Requests per hour:
  09:00   13  *************  <- busiest
  10:00    8  ********
  11:00    7  *******
404 paths:       /.env, /phpmyadmin, /products/999, /wp-admin
Suspicious IPs:  198.51.100.3, 203.0.113.7
```

Command (run inside `solutions/`):

```text
python3 -m t13_e07_log_analyser ../data/access.log --status 404 --top 2 --json report.json
```

Expected output:

```text
Requests:        4
Malformed lines: 2 [14, 28]
Unique IPs:      2
Bytes sent:      2,048
Error rate:      100.0%
Status classes:  4xx=4

Top paths:
    1  /.env
    1  /phpmyadmin
Top IPs:
    3  198.51.100.3
    1  10.0.0.5
Requests per hour:
  09:00    1  *
  10:00    3  ***  <- busiest
404 paths:       /.env, /phpmyadmin, /products/999, /wp-admin
Suspicious IPs:  198.51.100.3
JSON report written to report.json
```

### Hints

- Build the regex in pieces with `(?P<name>...)` groups, and test it on single lines first.
- `datetime.strptime(text, "%d/%b/%Y:%H:%M:%S %z")` parses the timestamp.
- `collections.Counter` with `most_common` is handy. Sort by `(-count, key)` to get stable tie-breaking.
- Line 28 has an IP of `-` and no bytes field. It must count as malformed.

### Acceptance checklist

- [ ] The two malformed lines, 14 and 28, are reported and do not crash the program.
- [ ] The status class counts add up to the number of requests.
- [ ] The JSON file contains the same numbers as the text report.

---

## T13-E08 Maze solver with BFS

**Level:** Hard | **Time:** 70 minutes | **Package:** `t13_e08_maze_solver`

### Problem statement

Load a maze from a text file. `#` is a wall, a space is open floor, `S` is the start and `E` is
the end. Find the **shortest** path with breadth-first search, then print the maze with the path
drawn as `*`. Validate the maze:

- It needs exactly one `S` and one `E`, and no other characters.
- Short rows are padded with walls.

The program has these options:

- `--visited` marks every explored cell with `.`.
- `--compare` also runs depth-first search and prints its path, which is often longer.

When there is no path, print the explored area and exit with code 2.

Suggested modules: `maze.py` (`Maze`, `MazeError`, `render`), `solver.py` (`solve_bfs`,
`solve_dfs`, `Result`), `cli.py`.

### Sample input and expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e08_maze_solver ../data/maze_small.txt
```

Expected output:

```text
Maze 10x9, start (1, 1), end (7, 8)
BFS: shortest path 13 steps, explored 34 cell(s)
##########
#S   #   #
#*## # # #
#**#   # #
##*##### #
# *****# #
# ####*# #
#    #**E#
##########
```

Command (run inside `solutions/`):

```text
python3 -m t13_e08_maze_solver ../data/maze_open.txt --visited --compare
```

Expected output:

```text
Maze 15x11, start (1, 1), end (5, 8)
BFS: shortest path 17 steps, explored 79 cell(s)
###############
#S*...........#
#.*#########..#
#.*#******.#..#
#.*#*.###*.#..#
#.***.# E*....#
#..#..###..#..#
#..#.......#..#
#..#########. #
#..........   #
###############
DFS: path 29 steps, explored 46 cell(s)
###############
#S            #
#* #########  #
#* #       #  #
#* #  ###  #  #
#*    # E**** #
#* #  ###  #* #
#* #       #**#
#* ######### *#
#*************#
###############
```

Command (run inside `solutions/`):

```text
python3 -m t13_e08_maze_solver ../data/maze_blocked.txt
```

Expected output:

```text
Maze 7x5, start (1, 1), end (3, 5)
No path. BFS explored 7 cell(s).
#######
#S..# #
###.# #
#...#E#
#######
```

Exit code: 2

### Hints

- Store cells as `(row, col)` tuples. Neighbours are up, right, down and left, if they are inside the grid and not a wall.
- A `parent` dict does two jobs: it is the visited set, and it lets you rebuild the path backwards from `E`.
- BFS reaches each cell first along a shortest route. That is why its path is never longer than the DFS path.

### Acceptance checklist

- [ ] The path on `maze_small.txt` is 13 steps.
- [ ] Every step in the path moves to a neighbouring open cell.
- [ ] Invalid mazes raise `MazeError`, and the command line prints the error instead of a traceback.

---

## T13-E09 Tokenizer plus calculator (challenge)

**Level:** Hard | **Time:** 90 minutes | **Package:** `t13_e09_calculator`

### Problem statement

Build an interactive calculator in three stages:

1. **Tokenizer.** Turn text into `Token(kind, text, pos)` items of kind NUMBER (including `3.5`,
   `.5` and `1e3`), NAME, OP (`+ - * / // % ** ^ =`, where `^` means `**`), LPAREN, RPAREN and
   COMMA, followed by an END token. Report an unknown character together with its position.
2. **Parser.** A recursive-descent parser that builds a tree of small dataclasses. The usual
   precedence rules apply, unary minus binds more loosely than `**` (so `-2 ** 2` is `-4`), and
   `**` is right-associative (so `2 ^ 3 ^ 2` is 512). It supports assignment (`x = 3`), calls
   (`max(1, 2, 3)`) and brackets.
3. **Evaluator.** Supports variables, `ans` (the last result), the constants `pi` and `e`, and the
   functions `sqrt`, `abs`, `round`, `log`, `min` and `max`, with argument-count checks.

Errors such as syntax errors, unknown names, division by zero and wrong argument counts print a
`^` under the position of the problem. The commands `:tokens <expr>`, `:vars`, `:help` and
`:quit` are also available.

Suggested modules: `errors.py` (`CalcError` with `pos`), `tokenizer.py`, `parser.py`
(grammar in its docstring), `evaluator.py`, `cli.py`.

### Sample input and expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e09_calculator
```

Typed input, one line at a time (an empty line means just press Enter):

```text
2 + 3 * 4
(2 + 3) * 4
2 ^ 3 ^ 2
-2 ** 2
rate = 0.2
price = 250
price * (1 + rate)
ans / 3
sqrt(16) + max(1, 7, 3)
round(pi, 3)
7 // 2 + 7 % 2
:tokens x1 = 3.5e2*(y-1)
10 / (5 - 5)
2 + * 3
foo + 1
sqrt(1, 2)
3 $ 4
(1 + 2
:vars
:quit
```

Expected output (the program echoes typed input when it is piped in, which is how this transcript was produced; at a real keyboard you see the same text):

```text
Calculator. Type :help for help.
> 2 + 3 * 4
14
> (2 + 3) * 4
20
> 2 ^ 3 ^ 2
512
> -2 ** 2
-4
> rate = 0.2
rate = 0.2
> price = 250
price = 250
> price * (1 + rate)
300
> ans / 3
100
> sqrt(16) + max(1, 7, 3)
11
> round(pi, 3)
3.142
> 7 // 2 + 7 % 2
4
> :tokens x1 = 3.5e2*(y-1)
NAME(x1)  OP(=)  NUMBER(3.5e2)  OP(*)  LPAREN(()  NAME(y)  OP(-)  NUMBER(1)  RPAREN())  END()
> 10 / (5 - 5)
     ^
Error: division by zero
> 2 + * 3
      ^
Error: unexpected '*'
> foo + 1
  ^
Error: unknown variable 'foo'
> sqrt(1, 2)
  ^
Error: sqrt() takes 1 argument(s), got 2
> 3 $ 4
    ^
Error: unexpected character '$'
> (1 + 2
        ^
Error: expected ')' but found end of input
> :vars
ans = 4
e = 2.718281828
pi = 3.141592654
price = 250
rate = 0.2
> :quit
Bye.
```

### Hints

- Write the grammar down first. Each grammar rule becomes one parser method that calls the next, tighter-binding rule.
- One combined regex with named groups, `(?P<NUMBER>...)|(?P<NAME>...)|...`, used with `match(text, pos)`, makes a compact tokenizer.
- Try `**` and `//` before `*` and `/` in the regex, or they are split into two tokens.
- To tell `x = 1` (assignment) from `x + 1`, look ahead one token after a NAME.

### Acceptance checklist

- [ ] Precedence and associativity match Python's for `+ - * / // % **`.
- [ ] Every error case in the sample shows the caret in the right column.
- [ ] Assigning to `pi` or to a function name is refused.

---

## T13-E10 Library search with a trie (challenge)

**Level:** Hard | **Time:** 90 minutes | **Package:** `t13_e10_library_search`

### Problem statement

Index `data/books.csv`, which has the columns `id,title,author,year,genre`, so that searching is
fast. The program works like this:

- Split titles and authors into lowercase words, dropping stopwords such as `the`, `of` and `and`.
  Insert each word into a **trie**, one for titles and one for authors, where each word node holds
  the set of book ids that contain the word.
- `search <words>` requires every query word to match the **start** of some word in the title or
  author, so `pyth eff` finds "Effective Python". Rank the results: an exact title word scores 3,
  an exact author word scores 2 and a prefix-only match scores 1. Ties are broken by title.
- `title <words>` and `author <words>` limit the search to one field.
- `suggest <prefix>` autocompletes a word, most frequent first.
- `info <id>`, `help` and `quit` are also available.

Suggested modules: `trie.py` (`Trie` with `insert`, `exact`, `prefix_ids` and `complete`),
`catalog.py` (`Book`, `load_books`, `words`), `index.py` (`LibraryIndex` with `search` and
`suggest`), `cli.py`.

### Sample input and expected output

Command (run inside `solutions/`):

```text
python3 -m t13_e10_library_search --books ../data/books.csv
```

Typed input, one line at a time (an empty line means just press Enter):

```text
search python
search pyth eff
author weir
title algo
search tolk ring
suggest pro
suggest th
search quantum
info 18
info 99
quit
```

Expected output (the program echoes typed input when it is piped in, which is how this transcript was produced; at a real keyboard you see the same text):

```text
Indexed 25 books (52 title words, 49 author words).
library> search python
5 result(s) for 'python':
   3  [ 5] Automate the Boring Stuff with Python - Al Sweigart (2015, programming)
   3  [24] Effective Python - Brett Slatkin (2015, programming)
   3  [ 3] Fluent Python - Luciano Ramalho (2015, programming)
   3  [ 4] Python Crash Course - Eric Matthes (2015, programming)
   3  [23] Python Tricks - Dan Bader (2017, programming)
library> search pyth eff
1 result(s) for 'pyth eff':
   2  [24] Effective Python - Brett Slatkin (2015, programming)
library> author weir
2 result(s) for 'weir':
   2  [20] Project Hail Mary - Andy Weir (2021, fiction)
   2  [19] The Martian - Andy Weir (2011, fiction)
library> title algo
2 result(s) for 'algo':
   1  [ 6] Grokking Algorithms - Aditya Bhargava (2016, computer science)
   1  [ 7] Introduction to Algorithms - Thomas H. Cormen (1990, computer science)
library> search tolk ring
1 result(s) for 'tolk ring':
   2  [17] The Lord of the Rings - J. R. R. Tolkien (1954, fiction)
library> suggest pro
programmer (1), programming (1), programs (1), project (1)
library> suggest th
thomas (2), thinking (1)
library> search quantum
No books match 'quantum'.
library> info 18
[18] Dune - Frank Herbert (1965, fiction)
library> info 99
No book with id '99'.
library> quit
Bye.
```

### Hints

- `prefix_ids` walks down to the prefix node, then collects the ids from every word below it.
- Intersect the sets of matching ids for each query word (`&`) to get AND search. Stop early when the result is empty.
- Keep each book's word sets as well, so you can tell an exact match from a prefix match when you score.

### Acceptance checklist

- [ ] A query made only of stopwords returns no results instead of every book.
- [ ] `author weir` and `title weir` give different results.
- [ ] Searching does not loop over every book. It looks words up in the trie.
