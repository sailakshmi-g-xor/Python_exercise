# Topic 03: File handling: exercises

Work from the topic folder (the one that contains `data/`). Put your own scripts in a folder of your choice, open data files as `data/<name>` when you run from the topic folder, and write any output files into an `output/` folder (create it with `pathlib`), never into `data/`.

Expected output below was produced by running the trainer solutions with Python 3.12.

## T03-E01 - Read a text file and count

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** open(), with, iterating lines, enumerate

**Data files:** `data/notes.txt`

### Problem

Open `data/notes.txt` with a `with` statement and `encoding="utf-8"`. Print the first 5 lines, each preceded by its line number (right-aligned in width 3, then a colon and a space). Then write `file_stats(path)` that returns a dictionary with `lines`, `words`, `characters` (not counting the line ending) and `blank` (lines that are empty or only spaces), and print the four values.

### Sample input

`data/notes.txt` (25 lines, one of them blank).

### Expected output

```text
  1: Training notes - week 1
  2: Python is installed in two places: the laptop and the Ubuntu VM.
  3: Use VS Code with the Python extension.
  4: Remember to save the file before running it.
  5:
Lines: 25
Words: 150
Characters: 872
Blank lines: 1
```

### Hints

- `with open(path, encoding="utf-8") as f:` closes the file for you.
- Looping `for line in f` gives one line at a time, including the trailing `\n`; use `line.rstrip("\n")`.
- `enumerate(f, start=1)` numbers the lines.
- `len(text.split())` counts the words in a line.

### Acceptance checklist

- [ ] The file is opened with `with` and `encoding="utf-8"`.
- [ ] Only 5 lines are printed with numbers.
- [ ] Line endings are not counted as characters.
- [ ] Output matches the expected output.

---

## T03-E02 - Write a text file

**Level:** Easy  |  **Estimated time:** 10 minutes  |  **Practises:** open(..., "w"), f.write, pathlib mkdir

**Data files:** none (all data is given in the exercise)

### Problem

Write `write_squares(path, n)` that creates the file `path` (and its parent folder if needed) containing `n` lines of the form `<i> squared is <i*i>` for `i` from 1 to `n`, and returns `n`. In the main program write 8 lines to `output/squares.txt`, print `Lines written: 8`, then read the file back and print its contents.

### Sample input

No input.

### Expected output

```text
Lines written: 8
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
6 squared is 36
7 squared is 49
8 squared is 64
```

### Hints

- Use mode `"w"`: it creates the file or replaces an existing one.
- `Path("output").mkdir(exist_ok=True)` or `path.parent.mkdir(parents=True, exist_ok=True)`.
- `f.write` does not add a newline; add `"\n"` yourself.
- `path.read_text(encoding="utf-8")` reads the whole file.

### Acceptance checklist

- [ ] The `output` folder is created by the program if missing.
- [ ] Running the program twice gives the same file (no duplicated lines).
- [ ] Each line ends with a newline.
- [ ] Output matches the expected output.

---

## T03-E03 - Append to a journal

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** open(..., "a"), counting lines, unlink

**Data files:** none (all data is given in the exercise)

### Problem

Write `append_entry(path, text)` that adds `text` as a new line at the end of the file (creating it if necessary) and `count_lines(path)` that returns the number of lines (0 for a missing file). In the main program: delete `output/journal.txt` if it exists, print the line count, append the three entries below, print the count, append one more entry, print the count, and print the file contents.

### Sample input

```text
Entries: "Started the course", "Finished file exercises", "Reviewed CSV handling"
Extra entry: "Added one more entry"
```

### Expected output

```text
Lines before: 0
Lines after first run: 3
Lines after append: 4
Started the course
Finished file exercises
Reviewed CSV handling
Added one more entry
```

### Hints

- Mode `"a"` appends and never erases existing content.
- `Path.unlink(missing_ok=True)` deletes a file without an error if it is not there.
- `sum(1 for _ in f)` counts lines without loading the file into memory.
- Call `count_lines` on a missing file: check `path.exists()` first.

### Acceptance checklist

- [ ] Earlier lines are preserved when appending.
- [ ] A missing file counts as 0 lines.
- [ ] Running the program twice gives the same output.
- [ ] Output matches the expected output.

---

## T03-E04 - Sales revenue by region (CSV)

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** csv.DictReader, type conversion, aggregation

**Data files:** `data/sales.csv`

### Problem

Read `data/sales.csv` (columns `date,region,product,units,unit_price`). Write `read_sales(path)`, `revenue_by_region(rows)` (units times unit price, summed per region, rounded to 2 decimals) and `best_product_by_units(rows)` (returns `(product, total_units)`). Print regions from highest to lowest revenue (name left-aligned width 8, revenue right-aligned width 10 with 2 decimals), then a `Total` row in the same format, then `Best seller: <product> (<units> units)`.

### Sample input

`data/sales.csv` (30 rows plus a header).

### Expected output

```text
East       1522.00
South      1458.50
North      1199.50
West        600.00
Total      4780.00
Best seller: Widget (160 units)
```

### Hints

- Open CSV files with `newline=""` and `encoding="utf-8"`.
- Every value from `csv` is a string: use `int(...)` and `float(...)`.
- `sorted(d.items(), key=lambda kv: -kv[1])` sorts by value, highest first.
- `max(units.items(), key=lambda kv: kv[1])` finds the largest value.

### Acceptance checklist

- [ ] Numbers are converted before multiplying.
- [ ] Regions are sorted by revenue, highest first.
- [ ] The total row equals the sum of the region rows.
- [ ] Output matches the expected output.

---

## T03-E05 - Filter and write a CSV

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** csv.DictWriter, computed column

**Data files:** `data/sales.csv`

### Problem

Write `filter_big_orders(src, dst, min_units=10)` that reads `data/sales.csv` and writes a new CSV to `dst` containing only the rows with `units >= min_units`, with an extra last column `total` (units times unit price, two decimals). Keep the original column order, then `total`. Return the number of rows written. In the main program write `output/big_orders.csv`, print `Rows kept: <n>`, then print the first 6 lines of the new file (the header and 5 rows) with the fields joined by `, `.

### Sample input

`data/sales.csv`

### Expected output

```text
Rows kept: 24
date, region, product, units, unit_price, total
2026-03-01, East, Gadget, 14, 12.00, 168.00
2026-03-02, North, Widget, 19, 4.50, 85.50
2026-03-03, North, Gizmo, 20, 7.25, 145.00
2026-03-05, North, Doohickey, 15, 20.00, 300.00
2026-03-07, West, Widget, 20, 4.50, 90.00
```

### Hints

- `csv.DictWriter(f, fieldnames=[...])` then `writer.writeheader()` and `writer.writerow(row)`.
- Open the output with `newline=""` too, otherwise Windows adds blank lines.
- You can open two files in one `with` statement: `with open(a) as fin, open(b, "w") as fout:`.
- `f"{value:.2f}"` formats the total.

### Acceptance checklist

- [ ] The output has a header row and the `total` column last.
- [ ] Only rows with `units >= min_units` are written.
- [ ] No blank lines appear between rows on Windows.
- [ ] Output matches the expected output.

---

## T03-E06 - Folders and files with pathlib

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** Path, mkdir, rglob, suffix, rename

**Data files:** none (all data is given in the exercise)

### Problem

Using only `pathlib`, write:

1. `build_tree(base)` - create under `base` these files (making folders as needed), each containing one line `placeholder for <filename>`: `reports/2026/march/summary.txt`, `reports/2026/march/details.csv`, `reports/2026/april/summary.txt`, `reports/archive/readme.md`. Calling it twice must not fail.
2. `list_files(base)` - sorted list of all files below `base` as paths relative to `base`, written with `/` separators.
3. `count_by_suffix(paths)` - dictionary of file extension to count, sorted by extension.

In the main program use `output/tree` as the base: print the listing, print the suffix counts, then show `name`, `stem`, `suffix` and `parent` (just the folder name) of `reports/2026/march/summary.txt`, rename that file to `summary.bak` with `with_suffix`, and print `renamed to: summary.bak | old exists: False` and the number of `.txt` files left.

### Sample input

No input.

### Expected output

```text
reports/2026/april/summary.txt
reports/2026/march/details.csv
reports/2026/march/summary.txt
reports/archive/readme.md
By suffix: {'.csv': 1, '.md': 1, '.txt': 2}
name: summary.txt
stem: summary
suffix: .txt
parent: march
renamed to: summary.bak | old exists: False
txt files left: 1
```

### Hints

- `Path("a") / "b" / "c.txt"` joins parts with the correct separator on any system.
- `p.parent.mkdir(parents=True, exist_ok=True)` creates all missing folders.
- `base.rglob("*")` walks all subfolders; filter with `p.is_file()`.
- `p.relative_to(base).as_posix()` gives forward slashes, also on Windows.

### Acceptance checklist

- [ ] Works when run twice in a row.
- [ ] Listing is sorted and uses `/` on every operating system.
- [ ] No string concatenation is used to build paths.
- [ ] Output matches the expected output (the renamed file is no longer a `.txt`).

---

## T03-E07 - Large file, one line at a time

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** Streaming, deque, generators, memory

**Data files:** `data/server.log`

### Problem

Never load the whole file with `read()` or `readlines()` in this exercise. Write:

- `count_levels(path)` - dictionary of log level to count, for lines like `2026-03-14 09:03:10 [INFO] Server started`.
- `first_line_with(path, level)` - the 1-based number of the first line of that level, or `None`.
- `tail(path, n)` - the last `n` lines (without newline), using `collections.deque(f, maxlen=n)`.
- `write_big_log(path, lines)` - writes `lines` lines `2026-03-14 00:00:00 [LEVEL] line <i>` where every 10th line is `ERROR` and the others `INFO`.

Main program: for `data/server.log` print each level sorted alphabetically (level left-aligned width 8, count right-aligned width 3), the line number of the first `ERROR`, and the last 3 lines indented by two spaces. Then write `output/big.log` with 200000 lines, print the level counts of that file and its last line, and delete it.

### Sample input

`data/server.log` (40 lines).

### Expected output

```text
DEBUG     7
ERROR     4
INFO     21
WARNING   8
First ERROR on line: 19
Last 3 lines:
  2026-03-14 10:20:24 [DEBUG] Query plan built
  2026-03-14 10:21:15 [INFO] Health check ok
  2026-03-14 10:23:39 [WARNING] Slow query detected
Big file: {'INFO': 180000, 'ERROR': 20000}
Last big line: 2026-03-14 00:00:00 [ERROR] line 200000
```

### Hints

- `for line in f:` reads lazily, one line at a time, so memory use stays small.
- `line.split()[2]` is the `[LEVEL]` word; remove the brackets with `.strip("[]")`.
- `deque(f, maxlen=3)` keeps only the last 3 lines while streaming.
- `Path.unlink()` deletes the big file when you are done.

### Acceptance checklist

- [ ] No call to `.read()` or `.readlines()` on the big file.
- [ ] Level counts add up to the number of lines.
- [ ] `tail` returns lines without trailing newlines.
- [ ] Output matches the expected output.

---

## T03-E08 - Binary basics

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** "rb"/"wb", bytes, chunks, hashlib, struct

**Data files:** none (all data is given in the exercise)

### Problem

Work with binary files in the `output/` folder:

1. Write the 256 byte values `0..255` (`bytes(range(256))`) to `output/bytes.bin` and print the file size.
2. Write `read_in_chunks(path, size)`, a generator that yields chunks of at most `size` bytes. Print the list of chunk lengths for size 100.
3. Print the first 4 bytes as hex.
4. Write `sha256_of_file(path)` (read in chunks) and print the hash.
5. Write `copy_file(src, dst)` using chunks and print whether the hashes of source and copy are equal.
6. With `struct`, write `pack_ints(path, values)` (little-endian unsigned 32-bit) and `unpack_ints(path)`; pack `[1, 256, 65535]`, print the raw bytes and the unpacked list.

### Sample input

No input.

### Expected output

```text
Size: 256
Chunks of 100: [100, 100, 56]
First 4 bytes (hex): 00010203
SHA-256: 40aff2e9d2d8922e47afd4648e6967497158785fbd1da870e7110266bf944880
Copy identical: True
Packed bytes: b'\x01\x00\x00\x00\x00\x01\x00\x00\xff\xff\x00\x00'
Unpacked: [1, 256, 65535]
```

### Hints

- Use modes `"rb"` and `"wb"`; binary mode takes no `encoding`.
- `f.read(size)` returns `b""` at the end of the file: loop until you get that.
- `hashlib.sha256()`, then `.update(chunk)` for every chunk, then `.hexdigest()`.
- `struct.pack("<3I", 1, 256, 65535)` and `struct.unpack("<3I", data)`.

### Acceptance checklist

- [ ] Files are opened in binary mode.
- [ ] The last chunk can be shorter than the others.
- [ ] The copy has the same hash as the original.
- [ ] Output matches the expected output.

---

## T03-E09 - Challenge: clean a messy contact file

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** CSV in and out, validation, reject report

**Data files:** `data/dirty_contacts.csv`

### Problem

`data/dirty_contacts.csv` has columns `name,email,phone,city` and messy data. Write `clean_contacts(src, good_dst, reject_dst)` that reads it and writes two CSV files, returning a summary dictionary `{"read": n, "kept": n, "rejected": {reason: count}}`.

Cleaning rules for a row (row numbers count data rows from 1):

- Name: remove extra spaces and use title case. Empty name: reject with reason `missing name`.
- Email: strip and lower-case. It must contain exactly one `@`, no spaces, a non-empty part before the `@`, and a domain that contains a dot (not at the start or end). Otherwise reject with `invalid email`.
- An email already kept earlier is rejected with `duplicate email`. Check the rules in this order: name, email format, duplicate.
- Phone: keep digits only, but keep a leading `+`. An empty phone is allowed.
- City: remove extra spaces and use title case.

`good_dst` has header `name,email,phone,city`. `reject_dst` has header `row,reason,name,email` and the original (stripped) name and email. In the main program use `output/clean_contacts.csv` and `output/rejects.csv`; print the counts, the full reject file, then the first 4 lines of the clean file.

### Sample input

`data/dirty_contacts.csv` (25 data rows, including blank fields, duplicates and bad emails).

### Expected output

```text
Rows read: 25
Rows kept: 18
Rejected (duplicate email): 2
Rejected (invalid email): 3
Rejected (missing name): 2
--- rejects.csv ---
row,reason,name,email
4,missing name,,nobody@example.com
5,invalid email,Dina Patel,dina.patel@example
7,duplicate email,emil joseph,EMIL.JOSEPH@example.com
10,invalid email,Hugo Dsouza,hugo.dsouza.example.com
13,missing name,,
16,duplicate email,liam brown,Liam.Brown@Example.com
18,invalid email,Nikhil Shah,nikhil shah@example.com
--- first 4 lines of clean_contacts.csv ---
name,email,phone,city
Asha Nair,asha.nair@example.com,9876543210,Pune
Ben Thomas,ben.thomas@example.com,0225550101,Mumbai
Chen Wei,chen.wei@example.com,+919810022334,Delhi
```

### Hints

- One pass over `csv.DictReader` with a `seen` set of emails is enough.
- `" ".join(text.split())` removes extra spaces; `.title()` fixes capitals.
- Build the phone with `"".join(ch for ch in raw if ch.isdigit())`.
- Write helper functions `clean_name`, `clean_phone`, `valid_email` and test them on their own first.

### Acceptance checklist

- [ ] Every input row ends up in exactly one of the two output files.
- [ ] Reject reasons follow the check order in the rules.
- [ ] The clean file has no duplicate emails and all emails are lower case.
- [ ] Output matches the expected output.

---

## T03-E10 - Challenge: rotating log file

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Classes, pathlib rename/replace, file state

**Data files:** none (all data is given in the exercise)

### Problem

Write a class `RotatingLog(path, max_lines=10, backups=3)` with a method `write(line)`:

- Each call appends `line` plus a newline to the log file `path`.
- Before writing, if the file already holds `max_lines` lines, rotate: the current file becomes `<name>.1`, the old `.1` becomes `.2`, and so on. A file that would become `.<backups + 1>` is deleted. Then start a fresh log file.
- When the object is created for an existing file, it must continue counting from the lines already there.

Main program: empty the folder `output/rotation`, create `RotatingLog("output/rotation/app.log", max_lines=10, backups=3)`, write 45 lines `event 01` to `event 45`, then print for each file in the folder (sorted by name): the name (left-aligned width 10), the number of lines, the first line and the last line, in the format shown.

### Sample input

No input.

### Expected output

```text
app.log    lines= 5 first=event 41 last=event 45
app.log.1  lines=10 first=event 31 last=event 40
app.log.2  lines=10 first=event 21 last=event 30
app.log.3  lines=10 first=event 11 last=event 20
```

### Hints

- Rotate from the oldest backup to the newest so no file is overwritten before it is moved.
- `Path.replace(target)` renames and overwrites an existing target (also on Windows, unlike a plain `rename`).
- `path.with_name(f"{path.name}.1")` builds the backup names.
- Keep a `count` attribute and update it in `write` and in `__init__`.

### Acceptance checklist

- [ ] No file ever holds more than `max_lines` lines.
- [ ] At most `backups` old files exist; the oldest content is dropped.
- [ ] A new object continues counting from an existing file.
- [ ] Output matches the expected output.

---
