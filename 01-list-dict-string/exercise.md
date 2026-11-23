# Topic 01: Lists, dicts, sets, tuples and strings: exercises

Work from the topic folder (the one that contains `data/`). Put your own scripts in a folder of your choice, open data files as `data/<name>` when you run from the topic folder, and write any output files into an `output/` folder (create it with `pathlib`), never into `data/`.

Expected output below was produced by running the trainer solutions with Python 3.12.

## T01-E01 - Lists: max, min, sum, sorting and stepping

**Level:** Easy  |  **Estimated time:** 10 minutes  |  **Practises:** Lists and built-in functions

**Data files:** none (all data is given in the exercise)

### Problem

Given the list `numbers`, write a function `list_stats(nums)` that returns a dictionary with the keys `max`, `min`, `total`, `average`, `descending` (a new list sorted from largest to smallest) and `every_second` (elements at index 0, 2, 4, ...). Then print the results exactly as shown. Do not change the original list.

### Sample input

```python
numbers = [14, 3, 9, 27, 8, 21, 5, 18]
```

### Expected output

```text
max: 27
min: 3
total: 105
average: 13.12
descending: [27, 21, 18, 14, 9, 8, 5, 3]
every second: [14, 9, 8, 5]
```

### Hints

- `max`, `min`, `sum`, `len` and `sorted(..., reverse=True)` do most of the work.
- `sorted()` returns a new list; `list.sort()` changes the list in place.
- Slicing with a step: `nums[::2]`.
- Format the average with an f-string: `f"{value:.2f}"`.

### Acceptance checklist

- [ ] `list_stats` returns a dict with the six keys.
- [ ] The original list is unchanged after the call.
- [ ] Average is printed with two decimals.
- [ ] Output matches the expected output exactly.

---

## T01-E02 - Cleaning names with string methods

**Level:** Easy  |  **Estimated time:** 10 minutes  |  **Practises:** String methods

**Data files:** none (all data is given in the exercise)

### Problem

Names typed by users are messy. Write `clean_name(raw)` that removes leading and trailing spaces, collapses repeated inner spaces to one space, and converts to title case. Write `initials(name)` that returns the initials separated by dots, for example `"Anna Maria Smith"` gives `"A.M.S."`. For each raw name print the cleaned name (with `repr`, so quotes are visible) and its initials.

### Sample input

```python
names = ["  aNNa   maRIA  smith ", "o'brien   john", "MARY-JANE watson", "li   wei"]
```

### Expected output

```text
'Anna Maria Smith' -> A.M.S.
"O'Brien John" -> O.J.
'Mary-Jane Watson' -> M.W.
'Li Wei' -> L.W.
```

### Hints

- `str.split()` with no arguments splits on any run of whitespace and drops empty parts.
- `" ".join(list_of_words)` glues them back with single spaces.
- `str.title()` handles `o'brien` and `mary-jane` the way we want here.
- `f"{name!r}"` prints with quotes.

### Acceptance checklist

- [ ] Extra spaces at the ends and in the middle are gone.
- [ ] Each word starts with a capital letter and the rest is lower case.
- [ ] Initials end with a dot after the last letter.
- [ ] Output matches the expected output.

---

## T01-E03 - Slicing toolkit

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** Slicing and indexing

**Data files:** none (all data is given in the exercise)

### Problem

Write four small functions using only slicing and basic string operations:

1. `mask_card(number)` - replace all but the last four characters with `*`.
2. `reverse_words(sentence)` - reverse the order of the words.
3. `middle(text)` - the middle character of odd-length text, or the middle two characters of even-length text.
4. `every_other(text)` - characters at positions 0, 2, 4, ...

Also print `"Programming"` reversed using a slice. Print the results in the order shown.

### Sample input

```python
mask_card("4111111111111111")
reverse_words("learning python is fun")
middle("python"), middle("slicing")
every_other("abcdefghij")
"Programming"
```

### Expected output

```text
************1111
fun is python learning
th c
acegi
gnimmargorP
```

### Hints

- Negative indexes count from the end: `s[-4:]` is the last four characters.
- `"*" * 3` gives `"***"`.
- `[::-1]` reverses any sequence.
- For `middle`, use `len(text) // 2` and check whether the length is odd with `% 2`.

### Acceptance checklist

- [ ] `mask_card` keeps the card length the same.
- [ ] `middle` works for both odd and even lengths.
- [ ] No loops are needed in your solution.
- [ ] Output matches the expected output.

---

## T01-E04 - Sets for attendance, tuples for pairs

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** Sets, tuples and unpacking

**Data files:** none (all data is given in the exercise)

### Problem

Two training days have attendance lists. Write `compare_attendance(day1, day2)` returning a dictionary with sorted lists for: `both`, `either`, `only_day1`, `only_day2` and `one_day_only` (people who came on exactly one of the days). Write `dedupe_keep_order(items)` that removes duplicates but keeps the first occurrence order. Write `min_max(nums)` that returns a tuple `(smallest, largest)`; unpack it when printing. Print in the order shown.

### Sample input

```python
day1 = ["asha", "ben", "chen", "dina", "emil", "farah"]
day2 = ["ben", "dina", "gita", "hugo", "asha"]
signups = ["asha", "ben", "asha", "chen", "ben", "dina"]
min_max([7, 2, 9, 4])
```

### Expected output

```text
both: ['asha', 'ben', 'dina']
either: ['asha', 'ben', 'chen', 'dina', 'emil', 'farah', 'gita', 'hugo']
only_day1: ['chen', 'emil', 'farah']
only_day2: ['gita', 'hugo']
one_day_only: ['chen', 'emil', 'farah', 'gita', 'hugo']
unique signups: ['asha', 'ben', 'chen', 'dina']
min=2 max=9
```

### Hints

- Set operators: `&` (both), `|` (either), `-` (difference), `^` (symmetric difference).
- Sets have no order, so wrap results in `sorted()`.
- For `dedupe_keep_order`, keep a `seen` set and a result list.
- `low, high = min_max(...)` unpacks a tuple.

### Acceptance checklist

- [ ] All five keys are present and each value is a sorted list.
- [ ] `dedupe_keep_order` keeps the original order.
- [ ] `min_max` returns a tuple.
- [ ] Output matches the expected output.

---

## T01-E05 - Letter frequency with a dictionary

**Level:** Medium  |  **Estimated time:** 15 minutes  |  **Practises:** Dict counting and sorting items

**Data files:** none (all data is given in the exercise)

### Problem

Write `letter_frequency(text)` that counts each letter ignoring case and ignoring anything that is not a letter, returning a dictionary such as `{"t": 3, ...}`. Write `top_n(freq, n)` that returns the `n` most common letters as `(letter, count)` pairs, highest count first and alphabetical order when counts are equal. Print the number of distinct letters and the top 5 as `letter: count`.

### Sample input

```python
text = "The quick brown fox jumps over the lazy dog and the cat"
```

### Expected output

```text
distinct letters: 26
e: 4
o: 4
t: 4
a: 3
h: 3
```

### Hints

- `freq[ch] = freq.get(ch, 0) + 1` counts without a `KeyError`.
- `ch.isalpha()` filters letters; `text.lower()` removes case differences.
- `sorted(freq.items(), key=...)` can sort by a tuple such as `(-count, letter)`.
- Slice the sorted list with `[:n]`.

### Acceptance checklist

- [ ] Spaces and punctuation are not counted.
- [ ] `T` and `t` are counted together.
- [ ] Ties are broken alphabetically.
- [ ] Output matches the expected output.

---

## T01-E06 - Group words by length

**Level:** Medium  |  **Estimated time:** 15 minutes  |  **Practises:** dict of lists, setdefault

**Data files:** `data/words.txt`

### Problem

Read `data/words.txt` (one word per line). Write `group_by_length(words)` that returns a dictionary mapping word length to a sorted list of the unique words of that length. Print one line per length in increasing order: `length: word1, word2, ...`.

### Sample input

`data/words.txt` (30 words, one per line).

### Expected output

```text
3: act, cat, dog, god, tac
4: acre, care, leap, pale, peal, pear, plea, race
5: apple, level, notes, onset, rotor, stone, tones
6: banana, cherry, enlist, google, inlets, listen, python, silent, tinsel, typhon
```

### Hints

- `Path("data/words.txt").read_text().split()` gives a list of words.
- `groups.setdefault(length, []).append(word)` creates the list when missing.
- Use `set(words)` first to drop duplicates, `sorted()` for each list.
- `", ".join(list_of_words)` builds the printed line.

### Acceptance checklist

- [ ] Every word appears under its own length.
- [ ] Lists are sorted alphabetically.
- [ ] Lengths are printed in increasing order.
- [ ] Output matches the expected output.

---

## T01-E07 - Department salary summary

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** Reading CSV rows into dicts, aggregating

**Data files:** `data/employees.csv`

### Problem

Read `data/employees.csv` (columns `id,name,department,city,salary`). Write `summarize(rows)` that returns, for each department, a dictionary with `count`, `average` (rounded to 2 decimals) and `top` (name of the best paid person). Print a table with departments in alphabetical order. Columns: department left-aligned (width 12), count right-aligned (width 6), average right-aligned (width 12, two decimals), then two spaces and the top earner.

### Sample input

`data/employees.csv` (25 rows). Remember that CSV values are strings: convert `salary` to `int`.

### Expected output

```text
Department   Count     Average  Top earner
Engineering      6    85166.67  Priya Singh
Finance          5    69000.00  Sanjay Gupta
HR               4    49250.00  Xena Paul
Sales            5    56200.00  Vera Lopez
Support          5    40200.00  Tara Bose
```

### Hints

- `csv.DictReader` gives each row as a dictionary.
- Build `{dept: {"count": 0, "total": 0, ...}}` while looping over the rows.
- `f"{value:<12}"` left-aligns, `f"{value:>6}"` right-aligns, `f"{value:>12.2f}"` aligns a float.
- Keep track of the highest salary seen so far to find the top earner.

### Acceptance checklist

- [ ] `salary` is converted to `int` before summing.
- [ ] Averages are rounded to 2 decimals.
- [ ] The header and each row line up in columns.
- [ ] Output matches the expected output.

---

## T01-E08 - Five comprehensions

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** List, dict and set comprehensions

**Data files:** none (all data is given in the exercise)

### Problem

Implement these functions, each as a single comprehension:

1. `even_squares(nums)` - squares of the even numbers.
2. `word_lengths(words)` - dict mapping each word to its length.
3. `first_letters(words)` - the set of first letters.
4. `flatten(matrix)` - one flat list from a list of rows.
5. `transpose(matrix)` - swap rows and columns.

Print the results in the order shown (for the set, print it sorted as a list).

### Sample input

```python
even_squares(range(1, 11))
word_lengths(["apple", "kiwi", "banana", "fig"])
first_letters(["apple", "avocado", "banana", "blueberry", "cherry"])
flatten([[1, 2, 3], [4, 5, 6]])
transpose([[1, 2, 3], [4, 5, 6]])
```

### Expected output

```text
[4, 16, 36, 64, 100]
{'apple': 5, 'kiwi': 4, 'banana': 6, 'fig': 3}
['a', 'b', 'c']
[1, 2, 3, 4, 5, 6]
[[1, 4], [2, 5], [3, 6]]
```

### Hints

- `[expr for x in items if condition]`
- `{key: value for ...}` builds a dict and `{expr for ...}` builds a set.
- Nested loops in a comprehension read left to right: `[x for row in matrix for x in row]`.
- For `transpose`, loop over column indexes `range(len(matrix[0]))` and collect `row[i]` from each row.

### Acceptance checklist

- [ ] Each function body is one comprehension (plus `return`).
- [ ] `even_squares` works with a `range`, not only a list.
- [ ] `transpose` works for non-square matrices.
- [ ] Output matches the expected output.

---

## T01-E09 - Sorting with key functions

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** sorted(), key, tuple keys, reverse

**Data files:** `data/employees.csv`, `data/words.txt`

### Problem

Write three functions:

1. `sort_employees(rows)` - sort employee dictionaries by department (A to Z), then salary (highest first), then name (A to Z).
2. `sort_words(words)` - sort by length, then alphabetically.
3. `sort_by_value(d)` - list of `(key, value)` pairs sorted by value descending, ties by key ascending.

Using `data/employees.csv` and `data/words.txt`, print the first 8 sorted employees as `department` (width 12), `name` (width 14), `salary` (right-aligned, width 7); then the first 8 sorted words as a list; then `sort_by_value(stock)`.

### Sample input

```python
stock = {"apples": 12, "pears": 5, "plums": 12, "figs": 30, "dates": 5}
```
Plus `data/employees.csv` and `data/words.txt`.

### Expected output

```text
Engineering Priya Singh     95000
Engineering Chen Wei        91000
Engineering Kavya Iyer      88000
Engineering Asha Nair       82000
Engineering Uday Verma      79000
Engineering Gita Rao        76000
Finance     Sanjay Gupta    73000
Finance     Indu Menon      71000
['act', 'cat', 'dog', 'god', 'tac', 'acre', 'care', 'leap']
[('figs', 30), ('apples', 12), ('plums', 12), ('dates', 5), ('pears', 5)]
```

### Hints

- `sorted(items, key=lambda r: (r["department"], -r["salary"], r["name"]))` - a minus sign flips the order of a number.
- `sorted(d.items(), key=...)` sorts the pairs of a dictionary.
- Convert `salary` to `int` before sorting; otherwise "9" sorts after "10".
- `sorted()` does not change the original list.

### Acceptance checklist

- [ ] Salary is sorted numerically, not as text.
- [ ] Ties are resolved exactly as described.
- [ ] The original lists are not modified.
- [ ] Output matches the expected output.

---

## T01-E10 - Challenge: anagram groups

**Level:** Hard  |  **Estimated time:** 25 minutes  |  **Practises:** Dict of lists, sorted keys, multi-key sorting

**Data files:** `data/words.txt`

### Problem

Read `data/words.txt`. Write `group_anagrams(words)` that returns a list of groups, where each group is a sorted list of words that are anagrams of each other. Only keep groups with at least two words. Order the groups by size (largest first) and then alphabetically by their first word. Print the number of groups, then one line per group formatted `size: word1 word2 ...`, then a final line `largest: <first word> ... <size> words`.

### Sample input

`data/words.txt`

### Expected output

```text
groups: 7
5: enlist inlets listen silent tinsel
4: leap pale peal plea
4: notes onset stone tones
3: acre care race
3: act cat tac
2: dog god
2: python typhon
largest: enlist ... 5 words
```

### Hints

- Two words are anagrams when their sorted letters are the same: `"".join(sorted("listen"))` equals `"".join(sorted("silent"))`.
- Use that sorted-letters string as the dictionary key.
- Sort with `key=lambda g: (-len(g), g[0])`.
- Use `set(words)` so a duplicated word is not counted twice.

### Acceptance checklist

- [ ] Words with no anagram partner (for example `google`) are not shown.
- [ ] Every group is internally sorted.
- [ ] Group order follows the size then alphabet rule.
- [ ] Output matches the expected output.

---

## T01-E11 - Challenge: merge two nested inventories

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Nested dicts, copying, aggregation

**Data files:** none (all data is given in the exercise)

### Problem

Two warehouses keep stock as nested dictionaries `{item: {"qty": int, "price": float}}`. Write:

1. `merge_inventories(a, b)` - returns a new inventory. For items in both, add the quantities and keep the higher price. Items in only one warehouse are copied. The input dictionaries must not be modified and the result must not share inner dictionaries with them.
2. `low_stock(inventory, threshold=50)` - sorted list of item names with quantity below the threshold.
3. `total_value(inventory)` - sum of `qty * price`, rounded to 2 decimals.

Print each merged item sorted by name as `name` (width 8), `qty` (width 4, right-aligned) and `price` (two decimals), then the low-stock list, the total value, and whether warehouse A is unchanged (`A unchanged: True`).

### Sample input

```python
warehouse_a = {
    "bolts": {"qty": 120, "price": 0.25},
    "nuts": {"qty": 80, "price": 0.10},
    "screws": {"qty": 15, "price": 0.05},
}
warehouse_b = {
    "nuts": {"qty": 40, "price": 0.12},
    "washers": {"qty": 200, "price": 0.02},
    "screws": {"qty": 5, "price": 0.06},
}
```

### Expected output

```text
bolts    qty= 120 price=0.25
nuts     qty= 120 price=0.12
screws   qty=  20 price=0.06
washers  qty= 200 price=0.02
low stock: ['screws']
total value: 49.6
A unchanged: True
```

### Hints

- `copy.deepcopy(a)` gives an independent copy of nested dictionaries.
- `item in merged` checks for a key.
- A generator expression inside `sum(...)` computes the value without a temporary list.
- Check "A unchanged" by comparing `warehouse_a["nuts"]["qty"]` with its original value, 80.

### Acceptance checklist

- [ ] Quantities are added and the higher price is kept for shared items.
- [ ] Neither input dictionary is changed.
- [ ] Changing the result does not change the inputs (no shared inner dicts).
- [ ] Output matches the expected output.

---
