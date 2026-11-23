# Topic 06: Regular expressions: exercises

Work from the topic folder (the one that contains `data/`). Put your own scripts in a folder of your choice, open data files as `data/<name>` when you run from the topic folder, and write any output files into an `output/` folder (create it with `pathlib`), never into `data/`.

Expected output below was produced by running the trainer solutions with Python 3.12.

## T06-E01 - match, search and fullmatch

**Level:** Easy  |  **Estimated time:** 10 minutes  |  **Practises:** The three basic matching functions

**Data files:** none (all data is given in the exercise)

### Problem

Write three functions using `re`:

- `starts_with_number(text)` - `True` if the text begins with digits (use `re.match`).
- `first_number(text)` - the first run of digits anywhere in the text as an `int`, or `None` (use `re.search`).
- `is_whole_number(text)` - `True` only if the whole text is digits (use `re.fullmatch`).

For every string in the list below print one line: the string with `repr` left-aligned in width 12, then `match=`, `search=` and `fullmatch=` with the results (each result left-aligned in width 5, except the last).

### Sample input

```python
samples = ["42 apples", "apples 42", "42", "forty-two", ""]
```

### Expected output

```text
'42 apples'  match=True  search=42    fullmatch=False
'apples 42'  match=False search=42    fullmatch=False
'42'         match=True  search=42    fullmatch=True
'forty-two'  match=False search=None  fullmatch=False
''           match=False search=None  fullmatch=False
```

### Hints

- `re.match` only looks at the start of the string; `re.search` scans the whole string; `re.fullmatch` needs the entire string to match.
- The result is a match object or `None`; `match.group()` gives the matched text.
- `\d+` means one or more digits. Use a raw string: `r"\d+"`.
- `f"{value!s:<5}"` left-aligns the text form of any value.

### Acceptance checklist

- [ ] Patterns are raw strings.
- [ ] `is_whole_number("")` is `False`.
- [ ] `first_number` returns an `int`, not text.
- [ ] Output matches the expected output.

---

## T06-E02 - findall for numbers, tags and pairs

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** findall, groups in findall, quantifiers

**Data files:** none (all data is given in the exercise)

### Problem

Write `extract_numbers(text)` returning all numbers as strings (integers and decimals, with an optional minus sign), `extract_hashtags(text)` returning every `#word` (letters, digits and underscore), and `extract_pairs(text)` returning `(key, value)` tuples for every `key=value` in a string. Print the numbers, their sum rounded to 2 decimals, the hashtags, the pairs, and the pairs as a dictionary.

### Sample input

```python
text = ("Order 1042 shipped on 14 March: 3 items, total 59.97 EUR, "
        "discount -5.5 applied. Tags: #sale #newArrival #eco_friendly")
settings = "mode=fast; retries=3; name=Zed; level=7"
```

### Expected output

```text
numbers: ['1042', '14', '3', '59.97', '-5.5']
sum: 1113.47
hashtags: ['#sale', '#newArrival', '#eco_friendly']
pairs: [('mode', 'fast'), ('retries', '3'), ('name', 'Zed'), ('level', '7')]
as dict: {'mode': 'fast', 'retries': '3', 'name': 'Zed', 'level': '7'}
```

### Hints

- `\d+(?:\.\d+)?` matches an integer with an optional decimal part; `-?` makes the minus optional.
- `(?:...)` groups without capturing, so `findall` still returns whole matches.
- `\w` matches letters, digits and underscore.
- When a pattern has two capturing groups, `findall` returns a list of 2-tuples.

### Acceptance checklist

- [ ] `-5.5` is found as one number, not as `5.5`.
- [ ] Hashtags include the `#`.
- [ ] `extract_pairs` returns tuples and `dict(pairs)` works.
- [ ] Output matches the expected output.

---

## T06-E03 - Clean text with sub

**Level:** Easy  |  **Estimated time:** 20 minutes  |  **Practises:** re.sub with strings, callbacks, flags

**Data files:** none (all data is given in the exercise)

### Problem

Write four functions with `re.sub`:

1. `collapse_spaces(text)` - replace every run of whitespace (spaces, tabs, newlines) by one space and strip the ends.
2. `mask_numbers(text)` - every run of 6 or more digits is replaced by asterisks except its last 4 digits (use a function as the replacement). Shorter numbers stay.
3. `camel_to_snake(name)` - `userFirstName` becomes `user_first_name`; `HTTPResponse` becomes `h_t_t_p_response` with this simple rule (capital letter becomes `_` plus lower-case letter, no leading underscore).
4. `censor(text, words)` - replace each whole word from the list, ignoring case, by asterisks of the same length. `badminton` must not be touched when `bad` is censored.

Print the results in the order shown.

### Sample input

```python
collapse_spaces("  too    many \t spaces\n here  ")
mask_numbers("Call 9876543210 or card 4111111111111111, ref 12345")
camel_to_snake("userFirstName"), camel_to_snake("HTTPResponse"), camel_to_snake("simple")
censor("That was a Bad idea, a really BAD one, not badminton.", ["bad", "idea"])
```

### Expected output

```text
'too many spaces here'
Call ******3210 or card ************1111, ref 12345
userFirstName -> user_first_name
HTTPResponse -> h_t_t_p_response
simple -> simple
That was a *** ****, a really *** one, not badminton.
```

### Hints

- `re.sub(pattern, replacement, text)`; the replacement can be a function that receives the match object.
- `\s+` matches whitespace runs.
- `\b` is a word boundary: `\bbad\b` does not match inside `badminton`.
- `re.IGNORECASE` ignores case; `re.escape(word)` protects special characters in words.

### Acceptance checklist

- [ ] Short digit groups such as `12345` stay unchanged.
- [ ] The whole-word match leaves `badminton` alone.
- [ ] `censor` is case-insensitive.
- [ ] Output matches the expected output.

---

## T06-E04 - Dates with groups

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** Capturing groups, alternatives, validating after matching

**Data files:** `data/dates.txt`

### Problem

`data/dates.txt` has 25 lines, each supposed to be a date. Accepted shapes are `YYYY-MM-DD`, `DD/MM/YYYY` and `D Mon YYYY` (for example `5 Jan 2026`, month names `Jan` to `Dec`). Write `parse_date(text)` that returns a `datetime.date`. It must raise `ValueError("unrecognised format")` when the text matches none of the shapes (the whole text must match) and `ValueError("invalid date")` when the shape is right but the calendar date does not exist (`31/02/2026`, month 13, 29 February in a non-leap year).

Print one line per input line: the text left-aligned in width 15, ` -> `, and the ISO date (`YYYY-MM-DD`) or the error message. Finally print a dictionary with the counts of `ok`, `invalid date` and `unrecognised format`.

### Sample input

`data/dates.txt` (25 lines).

### Expected output

```text
2026-03-14      -> 2026-03-14
14/03/2026      -> 2026-03-14
14 Mar 2026     -> 2026-03-14
2025-12-31      -> 2025-12-31
01/01/2026      -> 2026-01-01
5 Jan 2026      -> 2026-01-05
2026-13-01      -> invalid date
31/02/2026      -> invalid date
2026-3-5        -> unrecognised format
14.03.2026      -> unrecognised format
March 14, 2026  -> unrecognised format
2024-02-29      -> 2024-02-29
29/02/2025      -> invalid date
30 Feb 2026     -> invalid date
2026-04-31      -> invalid date
07/08/2026      -> 2026-08-07
12 Dec 2025     -> 2025-12-12
2026-06-15      -> 2026-06-15
15/06/26        -> unrecognised format
1 Sep 2026      -> 2026-09-01
2026/03/14      -> unrecognised format
31 Apr 2026     -> invalid date
2026-02-28      -> 2026-02-28
28/02/2026      -> 2026-02-28
9 Oct 2026      -> 2026-10-09
{'ok': 14, 'invalid date': 6, 'unrecognised format': 5}
```

### Hints

- Use one compiled pattern per shape with groups, e.g. `(\d{4})-(\d{2})-(\d{2})`, and `re.fullmatch`.
- `m.groups()` returns all captured parts as strings; convert with `int`.
- A regular expression checks the shape only: build `datetime.date(year, month, day)` and catch its `ValueError`.
- Map month names to numbers with a dictionary.

### Acceptance checklist

- [ ] `2026-3-5` and `14.03.2026` are unrecognised formats.
- [ ] `31/02/2026` and `2026-13-01` are invalid dates.
- [ ] `2024-02-29` is accepted and `29/02/2025` is rejected.
- [ ] Output matches the expected output.

---

## T06-E05 - Validate and extract e-mail addresses

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** fullmatch validation, findall extraction, character classes

**Data files:** `data/contacts.txt`

### Problem

Rules for a valid address: a local part of letters, digits and the characters `. _ + -`, then exactly one `@`, then a domain made of one or more labels (letters, digits, hyphen) each followed by a dot, and ending in a top-level domain of at least 2 letters. No spaces anywhere.

Write `is_valid_email(text)` (the entire text must fit the rules) and `extract_emails(text)` (all valid-looking addresses inside free text). Using `data/contacts.txt` (lines of `name | email | phone`), print `Valid:` and `Invalid:` counts, each invalid address with its owner (name left-aligned width 13), the 3 most common domains (lower case, most common first, ties alphabetical) as `  <domain>: <n>`, and the result of `extract_emails` on the sentence below.

### Sample input

`data/contacts.txt` and
```python
sentence = "Write to ann@example.com or bob.smith@mail.example.org, not to carl@localhost."
```

### Expected output

```text
Valid: 22
Invalid: 8
  Dina Patel   dina.patel@example
  Emil Joseph  emil.joseph@@example.com
  Gita Rao     gita rao@example.com
  Jorge Silva  jorge.silva@.com
  Liam Brown   liam.brown.example.com
  Nikhil Shah  nikhil@shah
  Quentin Fox  quentin.fox@example.c
  Uday Verma   uday@verma@example.com
Top domains:
  example.com: 14
  example.co.uk: 1
  example.es: 1
In text: ['ann@example.com', 'bob.smith@mail.example.org']
```

### Hints

- Use a character class: `[A-Za-z0-9_.+-]+` (the `-` at the end is a literal hyphen).
- `(?:[A-Za-z0-9-]+\.)+` matches one or more `label.` parts; then `[A-Za-z]{2,}` is the top-level domain.
- `re.fullmatch` is stricter than `re.search`: it prevents extra characters at the ends.
- Compile the pattern once with `re.compile`.

### Acceptance checklist

- [ ] Upper-case addresses are accepted.
- [ ] `a@b`, `a@@b.com`, `a b@c.com` and `a@.com` are rejected.
- [ ] `carl@localhost` is not extracted from the sentence.
- [ ] Output matches the expected output.

---

## T06-E06 - Validate and normalise phone numbers

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** Alternation, optional parts, named groups

**Data files:** `data/contacts.txt`

### Problem

Two phone number styles are valid.

- India: an optional `+91` prefix (optionally followed by a space or hyphen), then 5 digits, an optional space or hyphen, and 5 digits. Examples: `98765 43210`, `+91-98765-43213`, `+91 9876543214`.
- US: an area code of 3 digits, either plain or in parentheses, an optional space or hyphen, 3 digits, a hyphen, and 4 digits. Examples: `(555) 123-4567`, `555-123-4568`, `(555)123-4570`.

Write `phone_kind(text)` returning `"IN"`, `"US"` or `None` (whole text must match) and `normalize_phone(text)` returning `+91XXXXXXXXXX` or `+1XXXXXXXXXX` (digits only after the prefix), or `None`. Use named groups in your patterns.

Using the phone column of `data/contacts.txt`: print the first 4 valid numbers as `phone` (left-aligned width 18), kind, two spaces and the normalised form; then `India: <n> | US: <n> | invalid: <n>`; then each invalid number with the owner name (left-aligned width 13).

### Sample input

`data/contacts.txt` (30 lines of `name | email | phone`).

### Expected output

```text
+91 98765 43210   IN  +919876543210
98765-43211       IN  +919876543211
(555) 123-4567    US  +15551234567
98765 43212       IN  +919876543212
India: 16 | US: 7 | invalid: 7
  Gita Rao     98765 4321
  Liam Brown   555-1234
  Omar Ali     0098765 43218
  Sanjay Gupta +44 20 7946 0958
  Vera Lopez   (555) 123-45
  Xena Paul    +91 98765 4323
  Yash Jain    555.123.4573
```

### Hints

- `(?:\+91[ -]?)?` is an optional prefix; `[ -]?` an optional separator.
- `(?:\((?P<area_paren>\d{3})\)|(?P<area>\d{3}))` accepts an area code with or without parentheses.
- `m["name"]` or `m.group("name")` reads a named group; one of the two area groups is `None`.
- Always use `fullmatch` so that extra digits make the number invalid.

### Acceptance checklist

- [ ] `555.123.4573` and `98765 4321` are invalid.
- [ ] Both `+91` and no prefix give the same normalised number.
- [ ] Parenthesised and plain US area codes normalise identically.
- [ ] Output matches the expected output.

---

## T06-E07 - Parse a web server log with named groups

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** Named groups, groupdict, Counter

**Data files:** `data/access.log`

### Problem

`data/access.log` is in the common web-server format, for example:

`10.0.0.7 - - [14/Mar/2026:09:08:18 +0000] "GET /static/app.js HTTP/1.1" 200 31518`

The size is `-` when no body was sent. One line in the file is damaged. Write a compiled pattern with the named groups `ip`, `time`, `method`, `path`, `status`, `size`, and `parse_line(line)` returning a dictionary (from `groupdict()`) with `status` as `int` and `size` as `int` (0 for `-`), or `None` for lines that do not match.

Print: `Parsed: <n>`, `Unparsed lines: <list of line numbers>`, `First entry: <dict>`, the number of requests per status code in code order (`  <status>: <n>`), the 3 busiest IP addresses (`  <ip>: <n>`, ties by IP), and `Total bytes: <n>`.

### Sample input

`data/access.log` (40 lines).

### Expected output

```text
Parsed: 39
Unparsed lines: [18]
First entry: {'ip': '10.0.0.7', 'time': '14/Mar/2026:09:08:18 +0000', 'method': 'GET', 'path': '/static/app.js', 'status': 200, 'size': 31518}
Status codes:
  200: 15
  201: 4
  302: 2
  304: 6
  403: 4
  404: 3
  500: 5
Top IPs:
  192.168.1.10: 9
  203.0.113.9: 9
  10.0.0.7: 8
Total bytes: 778380
```

### Hints

- `(?P<ip>\d{1,3}(?:\.\d{1,3}){3})` names a group; `\[(?P<time>[^\]]+)\]` captures everything between brackets.
- `m.groupdict()` returns the named groups as a dictionary.
- `(?P<size>\d+|-)` allows either digits or a dash.
- `collections.Counter` counts statuses and IPs.

### Acceptance checklist

- [ ] The damaged line is reported, not parsed and not a crash.
- [ ] `status` and `size` are integers.
- [ ] The pattern is compiled once, outside the loop.
- [ ] Output matches the expected output.

---

## T06-E08 - Flags: IGNORECASE, MULTILINE, DOTALL, VERBOSE

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** Regex flags and multi-line text

**Data files:** none (all data is given in the exercise)

### Problem

Work with the multi-line text below. Write:

- `error_lines(text)` - every line that starts with `error` in any capitalisation (`re.IGNORECASE | re.MULTILINE`).
- `blocks(text)` - the blocks between a `BEGIN <name>` line and an `END <name>` line (case-insensitive, same name on both lines) as a list of `(name, list_of_lines)` (`re.DOTALL` and a lazy `.*?`).
- `find_times(text)` - all clock times `H:MM` or `HH:MM` with optional `:SS`, hours 0 to 23, minutes and seconds 00 to 59. Write the pattern with `re.VERBOSE` and comments.

Print the three results (as shown), and the case-sensitive result for `^error.*$` with only `re.MULTILINE` to show what the flag changes.

### Sample input

```text
Error: disk full
warning: low memory
ERROR: network down
info: all good
BEGIN config
port=8080
host=localhost
END config
begin Notes
free text
end notes
Meeting at 9:30, break 10:15:45, lunch 12:00, bad time 25:99
```

### Expected output

```text
error lines: ['Error: disk full', 'ERROR: network down']
block config: ['port=8080', 'host=localhost']
block Notes: ['free text']
times: ['9:30', '10:15:45', '12:00']
case-sensitive 'error' lines: []
```

### Hints

- Without `re.MULTILINE`, `^` and `$` match only at the start and end of the whole text.
- Without `re.DOTALL`, `.` does not match a newline.
- `\1` repeats whatever group 1 matched; with `IGNORECASE` it matches case-insensitively.
- In verbose mode whitespace in the pattern is ignored and `#` starts a comment.

### Acceptance checklist

- [ ] `error_lines` finds both `Error` and `ERROR` lines but not `warning`.
- [ ] The two blocks are returned with their original names.
- [ ] `25:99` is not reported as a time.
- [ ] The time pattern uses `re.VERBOSE` with comments.
- [ ] Output matches the expected output.

---

## T06-E09 - Challenge: analyse an application log

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Multi-pattern parsing, continuation lines, aggregation

**Data files:** `data/app.log`

### Problem

`data/app.log` mixes single-line entries and multi-line Python tracebacks. An entry looks like `2026-03-14 09:05:10,120 ERROR [db.pool] Connection timeout after 30s (host=10.0.0.5)`; any line that is not an entry belongs to the previous entry (traceback lines).

Write `analyze_app_log(text)` returning a dictionary with:

- `entries` - number of entries; `continuation_lines` - number of non-blank lines that are not entries;
- `by_level` - dictionary of level to count, sorted by level name;
- `problems` - list of `(time_without_milliseconds, module, message)` for `ERROR` and `CRITICAL` entries in file order;
- `avg_request_ms` - the average of the numbers in `completed in <n>ms` messages rounded to 1 decimal (`None` if there are none);
- `timeout_seconds` - the sum of the numbers in `after <n>s` messages;
- `hosts` - sorted list of the distinct IPv4 addresses found in `host=<ip>`;
- `exceptions` - the exception names (such as `ValueError`) that end the tracebacks, in order.

Print the report in the layout shown.

### Sample input

`data/app.log` (31 lines).

### Expected output

```text
Entries: 23 | continuation lines: 8
By level: {'CRITICAL': 1, 'DEBUG': 3, 'ERROR': 4, 'INFO': 12, 'WARNING': 3}
Errors and criticals:
  09:05:10 db.pool      Connection timeout after 30s (host=10.0.0.5)
  09:05:10 web.request  Unhandled exception for user=chen
  09:08:02 db.pool      Connection timeout after 45s (host=10.0.0.6)
  09:11:55 web.server   Out of memory, restarting
  09:15:48 mailer       SMTP refused connection (host=10.0.0.9)
Average request time: 146.9 ms
Total timeout seconds: 75
Hosts: 10.0.0.5, 10.0.0.6, 10.0.0.9
Exception types: ['ValueError', 'MemoryError']
```

### Hints

- Use named groups in the entry pattern and `m.groupdict()`.
- Use `re.findall` with one capturing group to collect numbers from a message.
- For the exception names, search the continuation text with `^(\w+(?:Error|Exception))` and `re.MULTILINE`.
- Test `analyze_app_log` on a tiny hand-written log before using the real file.

### Acceptance checklist

- [ ] Traceback lines are counted separately and never counted as entries.
- [ ] The average and the timeout sum are computed from numbers extracted by regex.
- [ ] An empty input returns zero counts and `None` for the average.
- [ ] Output matches the expected output.

---

## T06-E10 - Challenge: a tiny template engine

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** re.sub with a callback, optional groups, filters, missing values

**Data files:** none (all data is given in the exercise)

### Problem

Build a template renderer with `re.sub`. Placeholders look like `{{ name }}`, `{{ user.name }}` (dotted path into nested dictionaries), `{{ name|upper }}` (filters `upper`, `lower`, `title`), and `{{ name|default:text }}` (use `text` when the value is missing). Spaces inside the braces are allowed (`{{ plan | upper }}` works).

Write `find_placeholders(template)` (list of the paths in order of appearance) and `render(template, context)` returning `(text, missing)`: placeholders whose path is missing and that have no `default` filter are left unchanged in the text and their paths are collected in `missing`. A falsy value such as `0` is a real value. Text produced by a replacement is not processed again.

Main program: print the placeholders, the rendered text and the missing list for the template below.

### Sample input

```python
template = (
    "Hello {{ user.name|title }}, you have {{ count }} new messages.\n"
    "Your plan: {{plan|upper}}. Coupon: {{ coupon|default:none }}. Account: {{ account.id }}."
)
context = {"user": {"name": "asha nair"}, "count": 3, "plan": "pro"}
```

### Expected output

```text
Placeholders: ['user.name', 'count', 'plan', 'coupon', 'account.id']
Hello Asha Nair, you have 3 new messages.
Your plan: PRO. Coupon: none. Account: {{ account.id }}.
Missing: ['account.id']
```

### Hints

- Pattern parts: `\{\{`, `\s*`, `(?P<path>[A-Za-z_][\w.]*)`, an optional `\|\s*(?P<filter>\w+)` and an optional `:(?P<arg>...)`, then `\s*\}\}`.
- `re.sub(pattern, function, template)` calls `function(match)` for every placeholder; return the replacement text.
- Return `m.group(0)` to keep a placeholder unchanged.
- Look values up with a loop over `path.split(".")`; use a unique sentinel object for "missing", not `None`.

### Acceptance checklist

- [ ] Filters work with and without spaces around `|`.
- [ ] Missing values are left in place and reported; `default` supplies a replacement.
- [ ] A value of `0` is rendered as `0`.
- [ ] Output matches the expected output.

---
