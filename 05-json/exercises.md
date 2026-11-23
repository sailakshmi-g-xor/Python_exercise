# Topic 05: JSON: exercises

Work from the topic folder (the one that contains `data/`). Put your own scripts in a folder of your choice, open data files as `data/<name>` when you run from the topic folder, and write any output files into an `output/` folder (create it with `pathlib`), never into `data/`.

Expected output below was produced by running the trainer solutions with Python 3.12.

## T05-E01 - JSON basics: dumps and loads

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** json.dumps, json.loads, type mapping

**Data files:** none (all data is given in the exercise)

### Problem

Using `json.dumps` and `json.loads` on the dictionary below:

1. Print the compact JSON text (`compact: ...`).
2. Print an indented version (2 spaces) with sorted keys.
3. Write `roundtrip(obj)` that converts an object to JSON text and back. Show how the type of `scores` changes, what `married` and `nickname` become, and whether the round trip gives an equal object.
4. Show what happens to integer dictionary keys: print `roundtrip({1: "a", 2: "b"})`.
5. Try to dump a dictionary containing a `set`, catch the `TypeError` and print its message.

### Sample input

```python
sample = {
    "name": "Asha",
    "age": 30,
    "married": False,
    "scores": (90, 85),
    "nickname": None,
    "height": 1.68,
}
```

### Expected output

```text
compact: {"name": "Asha", "age": 30, "married": false, "scores": [90, 85], "nickname": null, "height": 1.68}
indented:
{
  "age": 30,
  "height": 1.68,
  "married": false,
  "name": "Asha",
  "nickname": null,
  "scores": [
    90,
    85
  ]
}
scores type before: tuple | after: list
married after: False | nickname after: None
equal after round trip: False
int keys: {'1': 'a', '2': 'b'}
TypeError: Object of type set is not JSON serializable
```

### Hints

- `json.dumps(obj)` returns a string; `json.loads(text)` returns Python objects.
- `indent=2` and `sort_keys=True` are keyword arguments of `dumps`.
- JSON has arrays (Python lists), not tuples; `true`/`false`/`null` become `True`/`False`/`None`.
- JSON object keys are always strings.

### Acceptance checklist

- [ ] You can say which Python types JSON can represent directly.
- [ ] The tuple comes back as a list, so the round trip is not equal.
- [ ] The `TypeError` for the set is caught, not left to crash the program.
- [ ] Output matches the expected output.

---

## T05-E02 - Read a config file

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** json.load, nested dicts, safe lookup with defaults

**Data files:** `data/config.json`

### Problem

Load `data/config.json` with `json.load`. Write `get_nested(data, path, default=None)` that follows a dotted path such as `"server.timeouts.read"` and returns the value, or `default` when any step of the path is missing (also when a step is not a dictionary). A value of `False` or `0` is a real value and must be returned, not the default. Print each path in the list below as `<path> = <repr of value>`, using the default shown, then print the admins joined with `, ` and their count.

### Sample input

```text
app.name
server.port
server.timeouts.read
database.pool.max
features.beta_dashboard
cache.ttl            (default 60)
server.host.name     (default "n/a")
```
Data: `data/config.json`.

### Expected output

```text
app.name = 'TrainingPortal'
server.port = 8080
server.timeouts.read = 30
database.pool.max = 10
features.beta_dashboard = False
cache.ttl = 60
server.host.name = 'n/a'
admins: asha, ben (2)
```

### Hints

- `with open(path, encoding="utf-8") as f: config = json.load(f)`.
- `path.split(".")` gives the list of keys to follow.
- Check `isinstance(current, dict) and key in current` before indexing.
- Compare with `is None`-style checks carefully: do not write `value or default`.

### Acceptance checklist

- [ ] Nested values at three levels are found.
- [ ] A missing key returns the default instead of raising `KeyError`.
- [ ] `False` values are returned correctly.
- [ ] Output matches the expected output.

---

## T05-E03 - Write JSON to a file

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** json.dump, indent, ensure_ascii, UTF-8

**Data files:** none (all data is given in the exercise)

### Problem

Write `save_json(path, obj)` (creates the parent folder, writes with `indent=2` and `ensure_ascii=False`, UTF-8, and a final newline) and `load_json(path)`. Save the list below to `output/students.json`, print the file content, print whether loading it back gives an equal list (`Round trip equal: True`), then show the difference between `ensure_ascii` settings for the text `"Zoë"` (`ASCII-escaped:` and `Readable:` lines).

### Sample input

```python
students = [
    {"id": 1, "name": "Zoë Martin", "marks": [78, 82, 91], "passed": True},
    {"id": 2, "name": "José Alvarez", "marks": [55, 48, 60], "passed": True},
    {"id": 3, "name": "Li Wei", "marks": [30, 41, 25], "passed": False},
]
```

### Expected output

```text
[
  {
    "id": 1,
    "name": "Zoë Martin",
    "marks": [
      78,
      82,
      91
    ],
    "passed": true
  },
  {
    "id": 2,
    "name": "José Alvarez",
    "marks": [
      55,
      48,
      60
    ],
    "passed": true
  },
  {
    "id": 3,
    "name": "Li Wei",
    "marks": [
      30,
      41,
      25
    ],
    "passed": false
  }
]
Round trip equal: True
ASCII-escaped: "Zo\u00eb"
Readable: "Zoë"
```

### Hints

- `json.dump(obj, f, indent=2, ensure_ascii=False)` writes straight to an open file.
- Open the file with `encoding="utf-8"` on both writing and reading.
- `json.dump` does not add a final newline; write one yourself.
- `json.dumps("Zoë")` gives `"Zo\u00eb"` by default.

### Acceptance checklist

- [ ] The file is readable and shows `Zoë`, not `Zo\u00eb`.
- [ ] Loading the file gives back an equal list.
- [ ] The `output` folder is created by the program.
- [ ] Output matches the expected output.

---

## T05-E04 - Analyse nested product data

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** Lists of dicts inside dicts, aggregation

**Data files:** `data/products.json`

### Problem

`data/products.json` is an object with `shop`, `currency` and a list `products`. Each product has `id`, `name`, `price`, `tags` (list), `stock` (dict of warehouse to quantity) and `dimensions`. Write:

- `stock_by_warehouse(products)` - total quantity per warehouse.
- `names_with_tag(products, tag)` - names of products that have the tag, in file order.
- `most_expensive(products)` - the product dictionary with the highest price.
- `out_of_stock(products)` - list of `(product name, warehouse)` pairs where the stock is 0, in file order.

Print: the header `Shop: <shop> (<currency>), <n> products`; the warehouse totals sorted by name (name left-aligned width 8, quantity right-aligned width 5); `On sale:` with the names joined by `, `; `Most expensive: <name> (<price with 2 decimals>)`; `Out of stock locations: <count>`; and `First three:` followed by the first three pairs.

### Sample input

`data/products.json` (20 products).

### Expected output

```text
Shop: Demo Office Supplies (EUR), 20 products
chennai   242
delhi     312
pune      132
On sale: Desk Lamp, Ballpoint Pen Set, Water Bottle, Sticky Notes, Webcam, Phone Holder
Most expensive: Mechanical Keyboard (89.00)
Out of stock locations: 21
First three: [('Notebook A5', 'pune'), ('Water Bottle', 'pune'), ('Laptop Stand', 'pune')]
```

### Hints

- `shop = json.load(f)`, then `products = shop["products"]`.
- `p["stock"].items()` gives warehouse and quantity pairs.
- `max(products, key=lambda p: p["price"])`.
- A list comprehension with two `for` clauses works for `out_of_stock`.

### Acceptance checklist

- [ ] All three warehouses are totalled.
- [ ] Products without the `sale` tag are not listed.
- [ ] The result of `most_expensive` is a whole product dict, not just a price.
- [ ] Output matches the expected output.

---

## T05-E05 - Read an API-style response

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** Status checking, optional fields, flattening records

**Data files:** `data/users_api.json`, `data/users_api_error.json`

### Problem

`data/users_api.json` imitates the response of a web API: `status`, paging fields and a `data` list of users. Some users have no `address` key, some have `address.city` set to `null`, `last_login` can be `null`, and one user has a `null` email. `data/users_api_error.json` imitates an error response.

Write `extract_users(response)` that returns `response["data"]` when `status` is `"ok"` and otherwise raises `ValueError("API error: <message>")` (use `unknown error` when there is no message). Write `users_table(users)` returning one flat dictionary per user with `id`, `name`, `city` (`"unknown"` when the address or city is missing or null), `domain` (the part of the email after `@`, or `"unknown"` when the email is missing or `null`) and `active`.

Print: `status: <status>, page <page>, total <total>`; the first 8 users as `id` (width 3, right-aligned), a space, `name` (left-aligned width 8), a space, `city`; `Active: <n> of <total>`; `Without a city: <n>`; the e-mail domains with counts (most common first, ties alphabetical) as `  <domain>: <n>`; and finally what happens with the error response (`Error response -> <message>`).

### Sample input

`data/users_api.json` and `data/users_api_error.json`.

### Expected output

```text
status: ok, page 1, total 25
  1 Asha     Pune
  2 Ben      Lyon
  3 Chen     Chennai
  4 Dina     unknown
  5 Emil     Lyon
  6 Farah    Pune
  7 Gita     Berlin
  8 Hugo     Pune
Active: 17 of 25
Without a city: 5
  example.com: 9
  mail.test: 9
  example.org: 6
  unknown: 1
Error response -> API error: rate limit exceeded
```

### Hints

- `u.get("address") or {}` copes with both a missing key and `null`.
- `address.get("city") or "unknown"` handles a `null` city.
- `collections.Counter` counts the domains.
- Catch the `ValueError` in the main program and print its message.

### Acceptance checklist

- [ ] Users with a missing address and users with a null city both show `unknown`.
- [ ] The error response raises `ValueError`, it does not crash with `KeyError`.
- [ ] The table rows are flat dictionaries.
- [ ] Output matches the expected output.

---

## T05-E06 - Update data and write it back

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** Deep copy, modifying nested data, round trip to file

**Data files:** `data/products.json`

### Problem

Write `apply_discount(products, tag, percent)` that returns a new list of product dictionaries (the input must not change). Products carrying the tag get their `price` reduced by `percent` percent, rounded to 2 decimals, and a new field `original_price` holding the old price. Other products stay as they are.

Main program: load `data/products.json`, apply a 10 percent discount to the tag `sale`, save the whole shop object (all other fields preserved) to `output/products_discounted.json` with `indent=2`, load that file again and print: `Discounted: <n>`, one line per discounted product as `name` (left-aligned width 20), old price (right-aligned width 7, two decimals), ` -> `, new price (right-aligned width 6, two decimals), then `Original data untouched: True` and `Other fields kept: <shop> <currency>`.

### Sample input

`data/products.json`

### Expected output

```text
Discounted: 6
Desk Lamp             24.99 ->  22.49
Ballpoint Pen Set      6.80 ->   6.12
Water Bottle          12.00 ->  10.80
Sticky Notes           2.99 ->   2.69
Webcam                34.25 ->  30.82
Phone Holder           9.99 ->   8.99
Original data untouched: True
Other fields kept: Demo Office Supplies EUR
```

### Hints

- `copy.deepcopy(products)` copies nested dictionaries and lists.
- `round(price * (100 - percent) / 100, 2)`.
- `dict(shop, products=new_list)` makes a copy of the shop dictionary with the products replaced.
- Check that the original list has no `original_price` keys to prove it was not modified.

### Acceptance checklist

- [ ] The input list is not modified.
- [ ] Prices are rounded to 2 decimals.
- [ ] The saved file contains the whole shop object, not only the products.
- [ ] Output matches the expected output.

---

## T05-E07 - Custom JSON encoder and decoder

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** JSONEncoder.default, object_hook, dates and decimals

**Data files:** none (all data is given in the exercise)

### Problem

`json.dumps` cannot handle `datetime`, `Decimal`, `set` or dataclass objects. Create:

- a dataclass `Customer(name: str, vip: bool)`;
- `class AppEncoder(json.JSONEncoder)` with a `default` method that converts `datetime` to its ISO text, `Decimal` to a string (so no precision is lost), a `set` to a sorted list, and a dataclass to a dictionary (`dataclasses.asdict`); everything else must still raise `TypeError` (call `super().default(o)`);
- `encode(obj)` that dumps with this encoder and `sort_keys=True`;
- `decode(text)` that uses `object_hook` to turn the `created` key back into a `datetime` and the `total` key back into a `Decimal`.

Encode the record below, print the JSON text, decode it and print the type and value of `created`, `total`, `tags` and `customer`, and finally show that plain `json.dumps` fails (`Default encoder fails: <message>`).

### Sample input

```python
record = {
    "id": 7,
    "created": datetime(2026, 3, 14, 9, 30, 15),
    "total": Decimal("19.99"),
    "tags": {"gift", "express"},
    "customer": Customer("Asha", True),
}
```

### Expected output

```text
{"created": "2026-03-14T09:30:15", "customer": {"name": "Asha", "vip": true}, "id": 7, "tags": ["express", "gift"], "total": "19.99"}
created: datetime 2026-03-14 09:30:15
total: Decimal 19.99
tags: list ['express', 'gift']
customer: dict {'name': 'Asha', 'vip': True}
Default encoder fails: Object of type datetime is not JSON serializable
```

### Hints

- Override `default(self, o)`: return a serialisable replacement, or call `super().default(o)` for unknown types.
- `datetime.isoformat()` and `datetime.fromisoformat(text)` convert both ways.
- `json.dumps(obj, cls=AppEncoder)` and `json.loads(text, object_hook=func)`.
- The hook receives every decoded JSON object as a dictionary; change what you need and return it.

### Acceptance checklist

- [ ] Dates round trip to real `datetime` objects and totals to `Decimal`.
- [ ] Sets and dataclasses are encoded; unknown types still raise `TypeError`.
- [ ] Decoded sets are lists and decoded dataclasses are plain dicts (JSON has no such types).
- [ ] Output matches the expected output.

---

## T05-E08 - JSON Lines event log

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** One JSON object per line, bad-line handling, streaming write

**Data files:** `data/events.jsonl`

### Problem

`data/events.jsonl` has one JSON object per line (an event log), but a few lines are damaged. Write:

- `read_events(path)` - returns `(events, bad_line_numbers)`; skips blank lines silently and records the 1-based number of every line that is not valid JSON (catch `json.JSONDecodeError`).
- `write_jsonl(path, records)` - one `json.dumps` per line; creates the parent folder; returns the number of records.
- `revenue_by_user(events)` - sum of `amount` of the `purchase` events per user, rounded to 2 decimals.

Print: `Valid events: <n>`, `Bad lines: <list>`, the count of each event type sorted by name (name left-aligned width 9, count right-aligned width 3), revenue per user from highest to lowest (user left-aligned width 6, amount right-aligned width 8 with 2 decimals), then write only the purchase events to `output/purchases.jsonl` and print `Purchases written: <n>`, and read the file back: `Read back: <n> bad: <list> equal: <True/False>`.

### Sample input

`data/events.jsonl` (32 lines, 2 of them not valid JSON).

### Expected output

```text
Valid events: 30
Bad lines: [12, 25]
login      3
logout     7
purchase  14
view       6
emil    285.21
asha    248.39
chen    185.84
dina    113.29
Purchases written: 14
Read back: 14 bad: [] equal: True
```

### Hints

- Read the file line by line; call `json.loads(line)` on each.
- A line cut off in the middle raises `json.JSONDecodeError`.
- Do not use `json.load` on the whole file: it is not one JSON document.
- `Counter(e["event"] for e in events)` counts event types.

### Acceptance checklist

- [ ] Bad lines are reported by number and do not stop the program.
- [ ] Each output line is a complete JSON object.
- [ ] The file written can be read back to an equal list.
- [ ] Output matches the expected output.

---

## T05-E09 - Challenge: validate JSON against a hand-written schema

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Recursion, isinstance, error paths

**Data files:** `data/users_api.json`

### Problem

Write `validate(data, schema, path="")` that returns a list of error strings (empty when valid). A schema is built from:

- a Python type (`str`, `int`, `bool`, `float`) - the value must be of that type; a `bool` is not accepted where `int` is expected;
- a dictionary of `key: schema` - the value must be an object; every key is required unless wrapped in `Optional`; extra keys are allowed;
- a list with one element, `[schema]` - the value must be an array and every item must match;
- `Optional(schema)` (a small class you write) - the key may be missing or `null`.

Error format: `<path>: missing`, `<path>: expected <type>, got <type>` (type names such as `str`, `int`, `NoneType`), `<path>: expected object, got <type>`, `<path>: expected array, got <type>`. Paths look like `data[6].address.city`; for the root use `(root)`.

Validate `data/users_api.json` against the schema below, print `Errors found: <n>` and each error as ` - <error>`, then print the result for one good user document and for the non-object value `[1, 2]`.

### Sample input

```python
USER_SCHEMA = {
    "id": int, "name": str, "email": str, "active": bool,
    "roles": [str],
    "last_login": Optional(str),
    "address": Optional({"city": str, "country": str}),
}
RESPONSE_SCHEMA = {"status": str, "page": int, "total": int, "data": [USER_SCHEMA]}
```
Good user document: `{"id": 1, "name": "A", "email": "a@x.org", "active": True, "roles": []}`.

### Expected output

```text
Errors found: 5
 - data[6].id: expected int, got str
 - data[9].active: expected bool, got str
 - data[14].roles[1]: expected str, got int
 - data[19].address.city: expected str, got NoneType
 - data[21].email: expected str, got NoneType
Good document: []
Not an object: ['(root): expected object, got list']
```

### Hints

- Make `validate` recursive: for a dict schema call `validate` on every value with an extended path.
- Check `Optional` first, because it wraps another schema.
- `type(value).__name__` gives names such as `str` and `NoneType`.
- `isinstance(True, int)` is `True` in Python, so test for `bool` separately.

### Acceptance checklist

- [ ] Errors in nested lists show the item index, e.g. `data[14].roles[1]`.
- [ ] `null` is accepted only where `Optional` is used.
- [ ] A bool is rejected where an int is expected.
- [ ] Output matches the expected output.

---

## T05-E10 - Challenge: flatten, diff and deep-merge configuration files

**Level:** Hard  |  **Estimated time:** 30 minutes  |  **Practises:** Recursion, dict algorithms, set operations on keys

**Data files:** `data/config.json`, `data/config_v2.json`

### Problem

Write four functions for nested dictionaries (lists and empty dictionaries are treated as plain values):

- `flatten(data)` - one-level dictionary with dotted keys, for example `{"a": {"b": 1}}` becomes `{"a.b": 1}`.
- `unflatten(flat)` - the reverse.
- `diff(old, new)` - compare two nested dictionaries through their flattened form and return `{"added": {key: value}, "removed": {key: old_value}, "changed": {key: (old, new)}}` with keys sorted.
- `deep_merge(base, override)` - new dictionary; nested dictionaries are merged recursively, any other value in `override` replaces the one in `base`; neither input may be changed.

Main program with `data/config.json` (v1) and `data/config_v2.json` (v2): print `Flat keys: <n>`, the flat value of `server.timeouts.read`, `Round trip ok: <bool>` (`unflatten(flatten(v1)) == v1`), the diff as lines `added   <key> = <json value>`, `removed <key> (was <json value>)` and `changed <key>: <old json> -> <new json>` (added first, then removed, then changed), then merge `{"server": {"port": 9090, "timeouts": {"read": 60}}, "features": {"signup": False}}` into v1 and print `merged server:` and `merged features:` as JSON with sorted keys, and `v1 unchanged: <bool>`.

### Sample input

`data/config.json` and `data/config_v2.json`.

### Expected output

```text
Flat keys: 15
server.timeouts.read -> 30
Round trip ok: True
added   cache.backend = "redis"
added   cache.ttl = 300
added   features.dark_mode = true
added   server.workers = 4
removed database.pool.min (was 2)
removed server.host (was "0.0.0.0")
changed admins: ["asha", "ben"] -> ["asha", "ben", "chen"]
changed app.debug: false -> true
changed app.version: "1.4.2" -> "1.5.0"
changed server.timeouts.read: 30 -> 45
merged server: {"host": "0.0.0.0", "port": 9090, "timeouts": {"connect": 5, "read": 60}}
merged features: {"beta_dashboard": false, "signup": false}
v1 unchanged: True
```

### Hints

- `flatten`: recurse when the value is a non-empty dict, otherwise store it under the dotted key.
- `unflatten`: split the key on `.` and walk down with `node.setdefault(part, {})`.
- Dictionary key views support set operations: `a.keys() - b.keys()`, `a.keys() & b.keys()`.
- `json.dumps(value)` prints a value the JSON way (strings in double quotes, `true`/`false`).

### Acceptance checklist

- [ ] `unflatten(flatten(x)) == x` for the sample configuration.
- [ ] Added, removed and changed keys are all reported.
- [ ] `deep_merge` leaves its inputs unchanged.
- [ ] Output matches the expected output.

---
