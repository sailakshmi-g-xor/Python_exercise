# Topic 10: Design Patterns in Python - Exercises

Write your solution in a file such as `t10_e01.py` and paste the driver code from "Sample input" at the
bottom, inside `if __name__ == "__main__":`. Everything the driver uses (classes, functions, imports) must be
defined above it. Run it with `python t10_e01.py` (Windows: `py t10_e01.py`). Your output must match "Expected
output" exactly. Use only the standard library. Read the matching section of `worked-examples.md` first.

---

## T10-E01: Singleton: application configuration

**Level:** Easy | **Estimated time:** 15 minutes | **Practises:** Singleton pattern with a class decorator and a reset hook

### Problem

**Pattern: Singleton.** Write a class decorator `singleton(cls)` so that calling a decorated class always returns the
same instance (the first call creates it; arguments of later calls are ignored). The decorator must also add a function
attribute `reset()` that forgets the instance, which is useful in tests.

Then write `AppConfig` decorated with `@singleton`:

- `__init__(self, env="dev")` stores `env` and an empty dictionary `values`.
- `set(key, value)` and `get(key, default=None)` read and write `values`.

The driver shows two "different" constructions returning the same object, shared state, and what `reset()` does.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
a = AppConfig(env="prod")
b = AppConfig(env="test")
print(a is b)
print(b.env)
a.set("debug", False)
print(b.get("debug"))
print(b.get("missing", "n/a"))
AppConfig.reset()
c = AppConfig(env="test")
print(c is a, c.env, c.get("debug", "gone"))
print(type(c).__name__)
```

### Expected output

```text
True
prod
False
n/a
False test gone
AppConfig
```

### Hints

- Keep instances in a dictionary inside the decorator, keyed by class, and return a function `get_instance(*args, **kwargs)`.
- Use `functools.wraps(cls)` so that the decorated name keeps its `__name__`.
- A function is an object, so `get_instance.reset = ...` is allowed.
- After decoration `AppConfig` is a function, not a class: `isinstance(x, AppConfig)` would fail. Discuss this trade-off.

### Acceptance checklist

- [ ] Two calls with different arguments return the identical object
- [ ] State set through one reference is visible through the other
- [ ] `reset()` makes the next call create a fresh instance
- [ ] Output matches the expected output exactly

---

## T10-E02: Factory: notification senders

**Level:** Easy | **Estimated time:** 20 minutes | **Practises:** Factory pattern with a registry filled by a decorator

### Problem

**Pattern: Factory.** Build a small notification service.

- An abstract base class `Notifier` with an abstract method `send(recipient, message)` returning a string.
- A dictionary `NOTIFIERS = {}` and a decorator factory `register(kind)` that stores a class in it.
- Three concrete notifiers, registered as `"email"`, `"sms"` and `"push"`:
  - `EmailNotifier.send` returns `EMAIL to <recipient>@example.com: <message>`
  - `SmsNotifier.send` returns `SMS to <recipient>: <first 20 characters of the message>`
  - `PushNotifier.send` returns `PUSH to <recipient>: <message in upper case>`
- `create_notifier(kind)` returns a new notifier instance. An unknown kind raises
  `ValueError(f"Unknown notifier: {kind} (choose from ...)")`, where the choices are the sorted registered names
  separated by `, `.

Adding a fourth notifier must need no change to `create_notifier`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
for kind in ["email", "sms", "push"]:
    print(create_notifier(kind).send("ana", "Your order has shipped today"))
print(sorted(NOTIFIERS))
try:
    create_notifier("fax")
except ValueError as err:
    print("Error:", err)
```

### Expected output

```text
EMAIL to ana@example.com: Your order has shipped today
SMS to ana: Your order has shipp
PUSH to ana: YOUR ORDER HAS SHIPPED TODAY
['email', 'push', 'sms']
Error: Unknown notifier: fax (choose from email, push, sms)
```

### Hints

- `@register("email")` calls `register("email")` first and then applies the result to the class (see topic 08).
- Store the class, not an instance: `NOTIFIERS[kind] = cls`; instantiate in `create_notifier`.
- Catch `KeyError` and raise your own `ValueError`.

### Acceptance checklist

- [ ] No if/elif chain on the kind
- [ ] Each call to `create_notifier` returns a new object
- [ ] The error message lists the available kinds
- [ ] Output matches the expected output exactly

---

## T10-E03: Strategy: report export formats

**Level:** Easy | **Estimated time:** 20 minutes | **Practises:** Strategy pattern with plain functions, runtime switching and lookup by name

### Problem

**Pattern: Strategy.** Export rows (a list of dictionaries sharing the same keys) in different formats.

- `export_csv(rows)`: header line of keys followed by one line per row, joined with `\n`, no trailing newline.
- `export_json(rows)`: `json.dumps(rows)`.
- `export_markdown(rows)`: a Markdown table with a header row, a `| --- | --- |` separator row and one line per row.
- `STRATEGIES`: dictionary mapping `"csv"`, `"json"`, `"markdown"` to those functions.
- `ReportExporter(strategy)` with a public attribute `strategy`, an `export(rows)` method that returns `""` for an empty
  list and otherwise calls the strategy, and a class method `by_name(name)` that builds an exporter from `STRATEGIES`
  (unknown names raise `ValueError(f"Unknown format: {name}")`).

The driver switches strategy at run time and even passes a `lambda` as a strategy.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
rows = [{"name": "Ana", "sales": 120}, {"name": "Ben", "sales": 95}]
exporter = ReportExporter(export_csv)
print(exporter.export(rows))
exporter.strategy = export_json
print(exporter.export(rows))
print(ReportExporter.by_name("markdown").export(rows))
print(repr(exporter.export([])))
try:
    ReportExporter.by_name("xml")
except ValueError as err:
    print("Error:", err)
print(ReportExporter(lambda r: f"{len(r)} rows").export(rows))
```

### Expected output

```text
name,sales
Ana,120
Ben,95
[{"name": "Ana", "sales": 120}, {"name": "Ben", "sales": 95}]
| name | sales |
| --- | --- |
| Ana | 120 |
| Ben | 95 |
''
Error: Unknown format: xml
2 rows
```

### Hints

- Use the `csv` module with `io.StringIO` and `lineterminator="\n"` for CSV, or build the lines yourself.
- The exporter does not care what the strategy is, as long as it is callable with `rows`.
- Markdown rows look like `| Ana | 120 |`.

### Acceptance checklist

- [ ] Changing `exporter.strategy` changes the output without creating a new exporter
- [ ] `ReportExporter` contains no format-specific code
- [ ] An empty list returns an empty string
- [ ] Output matches the expected output exactly

---

## T10-E04: Builder: logging setup

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Builder pattern with a fluent interface, validation in `build()`, the `logging` module

### Problem

**Pattern: Builder.** Write `LoggerBuilder`, which produces a real `logging.Logger`:

- `name(name)`: logger name (required).
- `level(level_name)`: case-insensitive level name such as `"info"` or `"DEBUG"`; default is INFO. An unknown name
  raises `ValueError(f"Unknown level: {level_name}")` immediately.
- `stream(stream, fmt="%(levelname)s: %(message)s")`: add a handler that writes to a file-like object using the
  given format. It can be called several times.
- `build()`: raises `ValueError("logger needs a name")` or `ValueError("logger needs at least one handler")` when
  incomplete; otherwise configures and returns the logger. It must remove any existing handlers (the `logging` module caches
  loggers by name, so building twice would otherwise duplicate output) and set `propagate = False`.

Every step method returns `self` so the calls can be chained.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
buf1, buf2 = io.StringIO(), io.StringIO()
logger = (
    LoggerBuilder()
    .name("shop")
    .level("info")
    .stream(buf1)
    .stream(buf2, "%(name)s|%(message)s")
    .build()
)
logger.debug("hidden")
logger.info("order placed")
logger.error("payment failed")
print(buf1.getvalue(), end="")
print(buf2.getvalue(), end="")
print(logger.name, logger.level == logging.INFO, len(logger.handlers))
try:
    LoggerBuilder().build()
except ValueError as err:
    print("Error:", err)
try:
    LoggerBuilder().name("x").level("loud")
except ValueError as err:
    print("Error:", err)
```

### Expected output

```text
INFO: order placed
ERROR: payment failed
shop|order placed
shop|payment failed
shop True 2
Error: logger needs a name
Error: Unknown level: loud
```

### Hints

- `getattr(logging, "INFO")` gives the numeric level; check that the result is an `int`.
- `logging.StreamHandler(stream)` and `logging.Formatter(fmt)` build a handler.
- `logger.handlers.clear()` removes old handlers.
- Use `io.StringIO()` as a stream to capture output in the driver.

### Acceptance checklist

- [ ] All step methods return `self`
- [ ] Messages below the chosen level are not written
- [ ] Two handlers with different formats both receive each message
- [ ] Incomplete builders raise the specified errors
- [ ] Output matches the expected output exactly

---

## T10-E05: Adapter: payment gateways

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Adapter pattern: one target interface over two incompatible third-party clients

### Problem

**Pattern: Adapter.** Your shop code expects every payment provider to look like this:

```python
class PaymentProcessor(ABC):
    """The interface our shop code expects."""

    @abstractmethod
    def pay(self, amount_cents, currency="EUR"):
        """Return a receipt string such as 'PAID FP-1001' or raise PaymentDeclined."""
```

Two third-party clients cannot be changed and have incompatible methods:

```python
class FastPayClient:
    def __init__(self):
        self._next = 1001

    def charge(self, amount, card_token):
        ref = f"FP-{self._next}"
        self._next += 1
        status = "approved" if amount <= 1000 else "declined"
        return {"status": status, "id": ref}


class GlobalPayClient:
    def __init__(self):
        self._next = 2001

    def send(self, amount_cents, currency):
        ref = f"GP-{self._next}"
        self._next += 1
        return (0 if amount_cents <= 500000 else 5, ref)
```

Write `FastPayAdapter(client, card_token)` and `GlobalPayAdapter(client)`; both must be `PaymentProcessor` subclasses.

- `FastPayAdapter.pay` converts cents to a decimal amount, calls `charge`, and returns `PAID <id>` when the status is
  `"approved"`. Otherwise it raises `PaymentDeclined(f"FastPay declined {amount}")` where `amount` is the decimal
  amount (for example `1500.0`).
- `GlobalPayAdapter.pay` calls `send`; a code of `0` means success and returns `PAID <reference>`. Any other code
  raises `PaymentDeclined(f"GlobalPay error code {code}")`.

Also write the exception `PaymentDeclined(Exception)` and the interface above exactly as shown.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
processors = [
    FastPayAdapter(FastPayClient(), "tok_123"),
    GlobalPayAdapter(GlobalPayClient()),
]
for processor in processors:
    print(processor.pay(2500))
try:
    processors[0].pay(150000)
except PaymentDeclined as err:
    print("Declined:", err)
try:
    processors[1].pay(900000, "USD")
except PaymentDeclined as err:
    print("Declined:", err)
print(all(isinstance(p, PaymentProcessor) for p in processors))
```

### Expected output

```text
PAID FP-1001
PAID GP-2001
Declined: FastPay declined 1500.0
Declined: GlobalPay error code 5
True
```

### Hints

- An adapter holds the adaptee in an attribute and translates both the arguments and the results.
- Do not modify the third-party classes; the whole point is that you cannot.
- `amount_cents / 100` gives the decimal amount.

### Acceptance checklist

- [ ] Both adapters can be used in the same loop through the `pay(amount_cents)` interface
- [ ] Declines from either provider become `PaymentDeclined`
- [ ] The third-party client code is unchanged
- [ ] Output matches the expected output exactly

---

## T10-E06: Template Method: report job

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Template Method pattern with abstract steps and optional hooks

### Problem

**Pattern: Template Method.** Write an abstract class `ReportJob` whose `run()` method is the template:

1. record `"load"` in the list `self.steps` and call `self.load()`;
2. record `"validate"` and call `self.validate(rows)`;
3. record `"format"` and call `self.format_rows(rows)`;
4. return the three parts joined by newlines: `self.header()`, the formatted body, `self.footer(rows)`.

`run()` also clears `self.steps` when it starts. `load()` and `format_rows(rows)` are abstract. The hooks have defaults:
`validate(rows)` returns the rows unchanged, `header()` returns `== <ClassName> ==`, and `footer(rows)` returns
`(<n> rows)`.

Subclasses:

- `SalesReport`: loads `[("north", 120), ("south", -5), ("east", 80)]`; `validate` drops negative amounts;
  `format_rows` gives one line per row with the region left-aligned in 6 characters and the amount right-aligned in 5;
  `footer` returns `Total: <sum>`.
- `UserReport`: loads `[("Ana", "ana@example.com"), ("Ben", "ben@example.com")]`; lines look like `Ana <ana@example.com>`;
  `header` returns `-- Registered users --`; keeps the default `footer`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
sales = SalesReport()
print(sales.run())
print(sales.steps)
print(UserReport().run())
try:
    ReportJob()
except TypeError:
    print("ReportJob is abstract")
```

### Expected output

```text
== SalesReport ==
north   120
east     80
Total: 200
['load', 'validate', 'format']
-- Registered users --
Ana <ana@example.com>
Ben <ben@example.com>
(2 rows)
ReportJob is abstract
```

### Hints

- Instantiating a class with unimplemented abstract methods raises `TypeError` (use `abc.ABC`).
- Subclasses override steps, never `run()`.
- `f"{region:<6}{amount:>5}"` aligns columns.

### Acceptance checklist

- [ ] `run()` is defined only in the base class
- [ ] Overriding a hook changes the output without touching `run()`
- [ ] `steps` records the order `load, validate, format`
- [ ] `ReportJob()` cannot be instantiated
- [ ] Output matches the expected output exactly

---

## T10-E07: Observer: order events

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Observer pattern as an event bus with subscribe, unsubscribe and error isolation

### Problem

**Pattern: Observer.** Write a class `EventBus` for a shop:

- `subscribe(event, handler)` registers a callable for an event name.
- `unsubscribe(event, handler)` removes it; removing a handler that is not registered does nothing.
- `publish(event, **data)` calls every handler of that event with `**data`, in subscription order, and returns the number
  of handlers that **completed without raising**. If a handler raises, record `f"{handler.__name__}: {error}"` in the
  list `bus.errors` and carry on with the remaining handlers. Publishing an event nobody listens to returns `0`.

Also write the module-level list `audit` and these handlers, all taking `(order_id, customer)`:

- `send_email` prints `EMAIL <customer>: order <order_id> update`
- `send_sms` prints `SMS <customer>: order <order_id> update`
- `audit_log` appends `order_id` to `audit`
- `broken_handler` raises `RuntimeError("service down")`

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
bus = EventBus()
bus.subscribe("order.created", send_email)
bus.subscribe("order.created", audit_log)
bus.subscribe("order.shipped", send_sms)
bus.subscribe("order.shipped", broken_handler)
bus.subscribe("order.shipped", audit_log)
print(bus.publish("order.created", order_id=1, customer="ana"))
print(bus.publish("order.shipped", order_id=1, customer="ana"))
bus.unsubscribe("order.created", send_email)
print(bus.publish("order.created", order_id=2, customer="ben"))
print(bus.publish("order.cancelled", order_id=3, customer="cy"))
print(audit)
print(bus.errors)
```

### Expected output

```text
EMAIL ana: order 1 update
2
SMS ana: order 1 update
2
1
0
[1, 1, 2]
['broken_handler: service down']
```

### Hints

- Keep a dictionary from event name to a list of handlers; `dict.setdefault(event, [])` helps.
- Iterate over a copy (`list(handlers)`) so a handler can unsubscribe itself safely.
- Wrap each call in `try/except Exception`.

### Acceptance checklist

- [ ] Handlers run in the order they subscribed
- [ ] A failing handler does not stop the others and is recorded in `errors`
- [ ] Unsubscribing stops further calls
- [ ] Events with no subscribers return `0`
- [ ] Output matches the expected output exactly

---

## T10-E08: Decorator pattern: notifier wrappers

**Level:** Medium | **Estimated time:** 30 minutes | **Practises:** Decorator pattern: stackable wrappers sharing one interface

### Problem

**Pattern: Decorator (object wrapping, not the `@` syntax).** Write:

- `Notifier` base class with `send(message)` (raises `NotImplementedError`).
- `ConsoleNotifier(Notifier)`: `send` returns `CONSOLE: <message>`.
- `NotifierDecorator(Notifier)`: stores the wrapped notifier and by default forwards `send` to it. All decorators below
  inherit from it.
- `PrefixDecorator(inner, prefix)`: puts `prefix` in front of the message, then forwards.
- `TruncateDecorator(inner, max_len)`: if the message is longer than `max_len`, cut it to `max_len - 3` characters and
  add `...`, then forward.
- `LoggingDecorator(inner, log)`: appends `sending: <message>` (the message it received) to the list `log`, then forwards.
- `CountingDecorator(inner)`: counts calls in `self.count`, then forwards.

All of them return the result of the innermost `send`. The driver stacks four of them around a `ConsoleNotifier`; notice that the order of
wrapping changes what each layer sees.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
log = []
notifier = CountingDecorator(
    LoggingDecorator(
        PrefixDecorator(TruncateDecorator(ConsoleNotifier(), 30), "[ALERT] "),
        log,
    )
)
print(notifier.send("Server CPU usage is above ninety percent"))
print(notifier.send("Disk ok"))
print(notifier.count)
print(log)
print(isinstance(notifier, Notifier))
```

### Expected output

```text
CONSOLE: [ALERT] Server CPU usage is...
CONSOLE: [ALERT] Disk ok
2
['sending: Server CPU usage is above ninety percent', 'sending: Disk ok']
True
```

### Hints

- Each decorator calls `super().send(...)` with a possibly modified message.
- The outermost wrapper sees the original message first; the innermost sees the message after all other wrappers have changed it.
- Because every wrapper is a `Notifier`, wrappers can wrap other wrappers.

### Acceptance checklist

- [ ] Every decorator has the same `send(message)` interface as the base notifier
- [ ] Wrappers can be stacked in any order
- [ ] `isinstance(wrapped, Notifier)` is `True` for the whole stack
- [ ] You can explain why the log shows the original message while the console output is truncated
- [ ] Output matches the expected output exactly

---

## T10-E09: Command: text editor with undo and redo

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Command pattern with undo/redo stacks and a macro (composite) command

### Problem

**Pattern: Command.** Build the core of a text editor.

- `Editor` with a string attribute `text`, initially empty.
- `InsertCommand(editor, position, text)` and `DeleteCommand(editor, start, end)` (deletes `text[start:end]`). Each has
  `execute()` and `undo()`. A delete must remember the text it removed.
- `MacroCommand(commands)` runs several commands as one; its `undo()` undoes them in reverse order.
- `History` with:
  - `run(command)`: executes the command, stores it, and **clears the redo stack**;
  - `undo()`: undoes the most recent command; returns `True`, or `False` if there was nothing to undo;
  - `redo()`: re-executes the most recently undone command; returns `True`, or `False` if nothing can be redone.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
ed = Editor()
history = History()
history.run(InsertCommand(ed, 0, "Hello"))
history.run(InsertCommand(ed, 5, " World"))
print(ed.text)
history.undo()
print(ed.text)
history.redo()
print(ed.text)
history.undo()
history.undo()
print(repr(ed.text))
print(history.undo())
history.run(InsertCommand(ed, 0, "New"))
print(history.redo())
macro = MacroCommand([InsertCommand(ed, 3, " text"), DeleteCommand(ed, 0, 1)])
history.run(macro)
print(ed.text)
history.undo()
print(ed.text)
```

### Expected output

```text
Hello World
Hello
Hello World
''
False
False
ew text
New
```

### Hints

- Use two lists as stacks: commands done and commands undone.
- A new command after an undo makes the old redo history meaningless, so clear it.
- `DeleteCommand.execute` must save `text[start:end]` in an attribute so that `undo` can put it back.
- `reversed(self.commands)` undoes a macro in the right order.

### Acceptance checklist

- [ ] Undo restores the exact previous text for insert, delete and macro commands
- [ ] Redo works after undo, and fails after a new command is run
- [ ] `undo()` and `redo()` return booleans
- [ ] The macro is a single entry in the history
- [ ] Output matches the expected output exactly

---

## T10-E10: Iterator: lazy pages and tree traversal

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Iterator protocol (`__iter__`, `__next__`), generators, `yield from`, laziness

### Problem

**Pattern: Iterator.** Write three things.

1. `PageIterator(fetch_page)`: an iterator over a paginated source. `fetch_page(n)` returns the list of items on page `n`
   (starting at 0); an empty list means there are no more pages. The iterator must be **lazy**: a page is requested only
   when all items of the previous page have been consumed. Implement `__iter__` (returns `self`) and `__next__`
   (raises `StopIteration` at the end, and must not call `fetch_page` again after the end was reached).
2. `BinaryTree`: a binary search tree with `insert(value)` (smaller values go left, others right). Iterating it yields the
   values in sorted order (in-order traversal) using a recursive generator and `yield from`. `reversed(tree)` yields them
   in descending order (implement `__reversed__`). `value in tree` works through iteration.
3. `chunked(iterable, size)`: a generator that yields lists of at most `size` items without consuming more of the input
   than needed (`itertools.islice` helps).

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
PAGES = [[1, 2, 3], [4, 5, 6], [7]]
fetched = []

def fetch_page(n):
    fetched.append(n)
    return PAGES[n] if n < len(PAGES) else []

it = PageIterator(fetch_page)
print(next(it), next(it), next(it), fetched)
print(next(it), fetched)
print(list(it), fetched)

tree = BinaryTree()
for value in [5, 3, 8, 1, 4, 9]:
    tree.insert(value)
print(list(tree))
print(list(reversed(tree)))
print(8 in tree, 7 in tree)
print(list(chunked(tree, 4)))
print(next(iter(tree)))
```

### Expected output

```text
1 2 3 [0]
4 [0, 1]
[5, 6, 7] [0, 1, 2, 3]
[1, 3, 4, 5, 8, 9]
[9, 8, 5, 4, 3, 1]
True False
[[1, 3, 4, 5], [8, 9]]
1
```

### Hints

- Keep a buffer (the current page) and a position inside it; fetch a new page only when the buffer is used up.
- An in-order traversal is: left subtree, the node's value, right subtree.
- `yield from sub_generator` re-yields everything from the sub-generator.
- `while chunk := list(islice(it, size)):` is a compact loop for `chunked`.

### Acceptance checklist

- [ ] Pages are fetched on demand (the `fetched` list in the driver proves it)
- [ ] No extra `fetch_page` call happens after the iterator is exhausted
- [ ] Tree iteration is sorted and `reversed()` is descending
- [ ] `chunked` works with any iterable, including the tree
- [ ] Output matches the expected output exactly
# Topic 10: Design Patterns in Python - Exercises

Write your solution in a file such as `t10_e01.py` and paste the driver code from "Sample input" at the
bottom, inside `if __name__ == "__main__":`. Everything the driver uses (classes, functions, imports) must be
defined above it. Run it with `python t10_e01.py` (Windows: `py t10_e01.py`). Your output must match "Expected
output" exactly. Use only the standard library. Read the matching section of `worked-examples.md` first.

---

## T10-E01: Singleton: application configuration

**Level:** Easy | **Estimated time:** 15 minutes | **Practises:** Singleton pattern with a class decorator and a reset hook

### Problem

**Pattern: Singleton.** Write a class decorator `singleton(cls)` so that calling a decorated class always returns the
same instance (the first call creates it; arguments of later calls are ignored). The decorator must also add a function
attribute `reset()` that forgets the instance, which is useful in tests.

Then write `AppConfig` decorated with `@singleton`:

- `__init__(self, env="dev")` stores `env` and an empty dictionary `values`.
- `set(key, value)` and `get(key, default=None)` read and write `values`.

The driver shows two "different" constructions returning the same object, shared state, and what `reset()` does.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
a = AppConfig(env="prod")
b = AppConfig(env="test")
print(a is b)
print(b.env)
a.set("debug", False)
print(b.get("debug"))
print(b.get("missing", "n/a"))
AppConfig.reset()
c = AppConfig(env="test")
print(c is a, c.env, c.get("debug", "gone"))
print(type(c).__name__)
```

### Expected output

```text
True
prod
False
n/a
False test gone
AppConfig
```

### Hints

- Keep instances in a dictionary inside the decorator, keyed by class, and return a function `get_instance(*args, **kwargs)`.
- Use `functools.wraps(cls)` so that the decorated name keeps its `__name__`.
- A function is an object, so `get_instance.reset = ...` is allowed.
- After decoration `AppConfig` is a function, not a class: `isinstance(x, AppConfig)` would fail. Discuss this trade-off.

### Acceptance checklist

- [ ] Two calls with different arguments return the identical object
- [ ] State set through one reference is visible through the other
- [ ] `reset()` makes the next call create a fresh instance
- [ ] Output matches the expected output exactly

---

## T10-E02: Factory: notification senders

**Level:** Easy | **Estimated time:** 20 minutes | **Practises:** Factory pattern with a registry filled by a decorator

### Problem

**Pattern: Factory.** Build a small notification service.

- An abstract base class `Notifier` with an abstract method `send(recipient, message)` returning a string.
- A dictionary `NOTIFIERS = {}` and a decorator factory `register(kind)` that stores a class in it.
- Three concrete notifiers, registered as `"email"`, `"sms"` and `"push"`:
  - `EmailNotifier.send` returns `EMAIL to <recipient>@example.com: <message>`
  - `SmsNotifier.send` returns `SMS to <recipient>: <first 20 characters of the message>`
  - `PushNotifier.send` returns `PUSH to <recipient>: <message in upper case>`
- `create_notifier(kind)` returns a new notifier instance. An unknown kind raises
  `ValueError(f"Unknown notifier: {kind} (choose from ...)")`, where the choices are the sorted registered names
  separated by `, `.

Adding a fourth notifier must need no change to `create_notifier`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
for kind in ["email", "sms", "push"]:
    print(create_notifier(kind).send("ana", "Your order has shipped today"))
print(sorted(NOTIFIERS))
try:
    create_notifier("fax")
except ValueError as err:
    print("Error:", err)
```

### Expected output

```text
EMAIL to ana@example.com: Your order has shipped today
SMS to ana: Your order has shipp
PUSH to ana: YOUR ORDER HAS SHIPPED TODAY
['email', 'push', 'sms']
Error: Unknown notifier: fax (choose from email, push, sms)
```

### Hints

- `@register("email")` calls `register("email")` first and then applies the result to the class (see topic 08).
- Store the class, not an instance: `NOTIFIERS[kind] = cls`; instantiate in `create_notifier`.
- Catch `KeyError` and raise your own `ValueError`.

### Acceptance checklist

- [ ] No if/elif chain on the kind
- [ ] Each call to `create_notifier` returns a new object
- [ ] The error message lists the available kinds
- [ ] Output matches the expected output exactly

---

## T10-E03: Strategy: report export formats

**Level:** Easy | **Estimated time:** 20 minutes | **Practises:** Strategy pattern with plain functions, runtime switching and lookup by name

### Problem

**Pattern: Strategy.** Export rows (a list of dictionaries sharing the same keys) in different formats.

- `export_csv(rows)`: header line of keys followed by one line per row, joined with `\n`, no trailing newline.
- `export_json(rows)`: `json.dumps(rows)`.
- `export_markdown(rows)`: a Markdown table with a header row, a `| --- | --- |` separator row and one line per row.
- `STRATEGIES`: dictionary mapping `"csv"`, `"json"`, `"markdown"` to those functions.
- `ReportExporter(strategy)` with a public attribute `strategy`, an `export(rows)` method that returns `""` for an empty
  list and otherwise calls the strategy, and a class method `by_name(name)` that builds an exporter from `STRATEGIES`
  (unknown names raise `ValueError(f"Unknown format: {name}")`).

The driver switches strategy at run time and even passes a `lambda` as a strategy.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
rows = [{"name": "Ana", "sales": 120}, {"name": "Ben", "sales": 95}]
exporter = ReportExporter(export_csv)
print(exporter.export(rows))
exporter.strategy = export_json
print(exporter.export(rows))
print(ReportExporter.by_name("markdown").export(rows))
print(repr(exporter.export([])))
try:
    ReportExporter.by_name("xml")
except ValueError as err:
    print("Error:", err)
print(ReportExporter(lambda r: f"{len(r)} rows").export(rows))
```

### Expected output

```text
name,sales
Ana,120
Ben,95
[{"name": "Ana", "sales": 120}, {"name": "Ben", "sales": 95}]
| name | sales |
| --- | --- |
| Ana | 120 |
| Ben | 95 |
''
Error: Unknown format: xml
2 rows
```

### Hints

- Use the `csv` module with `io.StringIO` and `lineterminator="\n"` for CSV, or build the lines yourself.
- The exporter does not care what the strategy is, as long as it is callable with `rows`.
- Markdown rows look like `| Ana | 120 |`.

### Acceptance checklist

- [ ] Changing `exporter.strategy` changes the output without creating a new exporter
- [ ] `ReportExporter` contains no format-specific code
- [ ] An empty list returns an empty string
- [ ] Output matches the expected output exactly

---

## T10-E04: Builder: logging setup

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Builder pattern with a fluent interface, validation in `build()`, the `logging` module

### Problem

**Pattern: Builder.** Write `LoggerBuilder`, which produces a real `logging.Logger`:

- `name(name)`: logger name (required).
- `level(level_name)`: case-insensitive level name such as `"info"` or `"DEBUG"`; default is INFO. An unknown name
  raises `ValueError(f"Unknown level: {level_name}")` immediately.
- `stream(stream, fmt="%(levelname)s: %(message)s")`: add a handler that writes to a file-like object using the
  given format. It can be called several times.
- `build()`: raises `ValueError("logger needs a name")` or `ValueError("logger needs at least one handler")` when
  incomplete; otherwise configures and returns the logger. It must remove any existing handlers (the `logging` module caches
  loggers by name, so building twice would otherwise duplicate output) and set `propagate = False`.

Every step method returns `self` so the calls can be chained.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
buf1, buf2 = io.StringIO(), io.StringIO()
logger = (
    LoggerBuilder()
    .name("shop")
    .level("info")
    .stream(buf1)
    .stream(buf2, "%(name)s|%(message)s")
    .build()
)
logger.debug("hidden")
logger.info("order placed")
logger.error("payment failed")
print(buf1.getvalue(), end="")
print(buf2.getvalue(), end="")
print(logger.name, logger.level == logging.INFO, len(logger.handlers))
try:
    LoggerBuilder().build()
except ValueError as err:
    print("Error:", err)
try:
    LoggerBuilder().name("x").level("loud")
except ValueError as err:
    print("Error:", err)
```

### Expected output

```text
INFO: order placed
ERROR: payment failed
shop|order placed
shop|payment failed
shop True 2
Error: logger needs a name
Error: Unknown level: loud
```

### Hints

- `getattr(logging, "INFO")` gives the numeric level; check that the result is an `int`.
- `logging.StreamHandler(stream)` and `logging.Formatter(fmt)` build a handler.
- `logger.handlers.clear()` removes old handlers.
- Use `io.StringIO()` as a stream to capture output in the driver.

### Acceptance checklist

- [ ] All step methods return `self`
- [ ] Messages below the chosen level are not written
- [ ] Two handlers with different formats both receive each message
- [ ] Incomplete builders raise the specified errors
- [ ] Output matches the expected output exactly

---

## T10-E05: Adapter: payment gateways

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Adapter pattern: one target interface over two incompatible third-party clients

### Problem

**Pattern: Adapter.** Your shop code expects every payment provider to look like this:

```python
class PaymentProcessor(ABC):
    """The interface our shop code expects."""

    @abstractmethod
    def pay(self, amount_cents, currency="EUR"):
        """Return a receipt string such as 'PAID FP-1001' or raise PaymentDeclined."""
```

Two third-party clients cannot be changed and have incompatible methods:

```python
class FastPayClient:
    def __init__(self):
        self._next = 1001

    def charge(self, amount, card_token):
        ref = f"FP-{self._next}"
        self._next += 1
        status = "approved" if amount <= 1000 else "declined"
        return {"status": status, "id": ref}


class GlobalPayClient:
    def __init__(self):
        self._next = 2001

    def send(self, amount_cents, currency):
        ref = f"GP-{self._next}"
        self._next += 1
        return (0 if amount_cents <= 500000 else 5, ref)
```

Write `FastPayAdapter(client, card_token)` and `GlobalPayAdapter(client)`; both must be `PaymentProcessor` subclasses.

- `FastPayAdapter.pay` converts cents to a decimal amount, calls `charge`, and returns `PAID <id>` when the status is
  `"approved"`. Otherwise it raises `PaymentDeclined(f"FastPay declined {amount}")` where `amount` is the decimal
  amount (for example `1500.0`).
- `GlobalPayAdapter.pay` calls `send`; a code of `0` means success and returns `PAID <reference>`. Any other code
  raises `PaymentDeclined(f"GlobalPay error code {code}")`.

Also write the exception `PaymentDeclined(Exception)` and the interface above exactly as shown.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
processors = [
    FastPayAdapter(FastPayClient(), "tok_123"),
    GlobalPayAdapter(GlobalPayClient()),
]
for processor in processors:
    print(processor.pay(2500))
try:
    processors[0].pay(150000)
except PaymentDeclined as err:
    print("Declined:", err)
try:
    processors[1].pay(900000, "USD")
except PaymentDeclined as err:
    print("Declined:", err)
print(all(isinstance(p, PaymentProcessor) for p in processors))
```

### Expected output

```text
PAID FP-1001
PAID GP-2001
Declined: FastPay declined 1500.0
Declined: GlobalPay error code 5
True
```

### Hints

- An adapter holds the adaptee in an attribute and translates both the arguments and the results.
- Do not modify the third-party classes; the whole point is that you cannot.
- `amount_cents / 100` gives the decimal amount.

### Acceptance checklist

- [ ] Both adapters can be used in the same loop through the `pay(amount_cents)` interface
- [ ] Declines from either provider become `PaymentDeclined`
- [ ] The third-party client code is unchanged
- [ ] Output matches the expected output exactly

---

## T10-E06: Template Method: report job

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Template Method pattern with abstract steps and optional hooks

### Problem

**Pattern: Template Method.** Write an abstract class `ReportJob` whose `run()` method is the template:

1. record `"load"` in the list `self.steps` and call `self.load()`;
2. record `"validate"` and call `self.validate(rows)`;
3. record `"format"` and call `self.format_rows(rows)`;
4. return the three parts joined by newlines: `self.header()`, the formatted body, `self.footer(rows)`.

`run()` also clears `self.steps` when it starts. `load()` and `format_rows(rows)` are abstract. The hooks have defaults:
`validate(rows)` returns the rows unchanged, `header()` returns `== <ClassName> ==`, and `footer(rows)` returns
`(<n> rows)`.

Subclasses:

- `SalesReport`: loads `[("north", 120), ("south", -5), ("east", 80)]`; `validate` drops negative amounts;
  `format_rows` gives one line per row with the region left-aligned in 6 characters and the amount right-aligned in 5;
  `footer` returns `Total: <sum>`.
- `UserReport`: loads `[("Ana", "ana@example.com"), ("Ben", "ben@example.com")]`; lines look like `Ana <ana@example.com>`;
  `header` returns `-- Registered users --`; keeps the default `footer`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
sales = SalesReport()
print(sales.run())
print(sales.steps)
print(UserReport().run())
try:
    ReportJob()
except TypeError:
    print("ReportJob is abstract")
```

### Expected output

```text
== SalesReport ==
north   120
east     80
Total: 200
['load', 'validate', 'format']
-- Registered users --
Ana <ana@example.com>
Ben <ben@example.com>
(2 rows)
ReportJob is abstract
```

### Hints

- Instantiating a class with unimplemented abstract methods raises `TypeError` (use `abc.ABC`).
- Subclasses override steps, never `run()`.
- `f"{region:<6}{amount:>5}"` aligns columns.

### Acceptance checklist

- [ ] `run()` is defined only in the base class
- [ ] Overriding a hook changes the output without touching `run()`
- [ ] `steps` records the order `load, validate, format`
- [ ] `ReportJob()` cannot be instantiated
- [ ] Output matches the expected output exactly

---

## T10-E07: Observer: order events

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Observer pattern as an event bus with subscribe, unsubscribe and error isolation

### Problem

**Pattern: Observer.** Write a class `EventBus` for a shop:

- `subscribe(event, handler)` registers a callable for an event name.
- `unsubscribe(event, handler)` removes it; removing a handler that is not registered does nothing.
- `publish(event, **data)` calls every handler of that event with `**data`, in subscription order, and returns the number
  of handlers that **completed without raising**. If a handler raises, record `f"{handler.__name__}: {error}"` in the
  list `bus.errors` and carry on with the remaining handlers. Publishing an event nobody listens to returns `0`.

Also write the module-level list `audit` and these handlers, all taking `(order_id, customer)`:

- `send_email` prints `EMAIL <customer>: order <order_id> update`
- `send_sms` prints `SMS <customer>: order <order_id> update`
- `audit_log` appends `order_id` to `audit`
- `broken_handler` raises `RuntimeError("service down")`

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
bus = EventBus()
bus.subscribe("order.created", send_email)
bus.subscribe("order.created", audit_log)
bus.subscribe("order.shipped", send_sms)
bus.subscribe("order.shipped", broken_handler)
bus.subscribe("order.shipped", audit_log)
print(bus.publish("order.created", order_id=1, customer="ana"))
print(bus.publish("order.shipped", order_id=1, customer="ana"))
bus.unsubscribe("order.created", send_email)
print(bus.publish("order.created", order_id=2, customer="ben"))
print(bus.publish("order.cancelled", order_id=3, customer="cy"))
print(audit)
print(bus.errors)
```

### Expected output

```text
EMAIL ana: order 1 update
2
SMS ana: order 1 update
2
1
0
[1, 1, 2]
['broken_handler: service down']
```

### Hints

- Keep a dictionary from event name to a list of handlers; `dict.setdefault(event, [])` helps.
- Iterate over a copy (`list(handlers)`) so a handler can unsubscribe itself safely.
- Wrap each call in `try/except Exception`.

### Acceptance checklist

- [ ] Handlers run in the order they subscribed
- [ ] A failing handler does not stop the others and is recorded in `errors`
- [ ] Unsubscribing stops further calls
- [ ] Events with no subscribers return `0`
- [ ] Output matches the expected output exactly

---

## T10-E08: Decorator pattern: notifier wrappers

**Level:** Medium | **Estimated time:** 30 minutes | **Practises:** Decorator pattern: stackable wrappers sharing one interface

### Problem

**Pattern: Decorator (object wrapping, not the `@` syntax).** Write:

- `Notifier` base class with `send(message)` (raises `NotImplementedError`).
- `ConsoleNotifier(Notifier)`: `send` returns `CONSOLE: <message>`.
- `NotifierDecorator(Notifier)`: stores the wrapped notifier and by default forwards `send` to it. All decorators below
  inherit from it.
- `PrefixDecorator(inner, prefix)`: puts `prefix` in front of the message, then forwards.
- `TruncateDecorator(inner, max_len)`: if the message is longer than `max_len`, cut it to `max_len - 3` characters and
  add `...`, then forward.
- `LoggingDecorator(inner, log)`: appends `sending: <message>` (the message it received) to the list `log`, then forwards.
- `CountingDecorator(inner)`: counts calls in `self.count`, then forwards.

All of them return the result of the innermost `send`. The driver stacks four of them around a `ConsoleNotifier`; notice that the order of
wrapping changes what each layer sees.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
log = []
notifier = CountingDecorator(
    LoggingDecorator(
        PrefixDecorator(TruncateDecorator(ConsoleNotifier(), 30), "[ALERT] "),
        log,
    )
)
print(notifier.send("Server CPU usage is above ninety percent"))
print(notifier.send("Disk ok"))
print(notifier.count)
print(log)
print(isinstance(notifier, Notifier))
```

### Expected output

```text
CONSOLE: [ALERT] Server CPU usage is...
CONSOLE: [ALERT] Disk ok
2
['sending: Server CPU usage is above ninety percent', 'sending: Disk ok']
True
```

### Hints

- Each decorator calls `super().send(...)` with a possibly modified message.
- The outermost wrapper sees the original message first; the innermost sees the message after all other wrappers have changed it.
- Because every wrapper is a `Notifier`, wrappers can wrap other wrappers.

### Acceptance checklist

- [ ] Every decorator has the same `send(message)` interface as the base notifier
- [ ] Wrappers can be stacked in any order
- [ ] `isinstance(wrapped, Notifier)` is `True` for the whole stack
- [ ] You can explain why the log shows the original message while the console output is truncated
- [ ] Output matches the expected output exactly

---

## T10-E09: Command: text editor with undo and redo

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Command pattern with undo/redo stacks and a macro (composite) command

### Problem

**Pattern: Command.** Build the core of a text editor.

- `Editor` with a string attribute `text`, initially empty.
- `InsertCommand(editor, position, text)` and `DeleteCommand(editor, start, end)` (deletes `text[start:end]`). Each has
  `execute()` and `undo()`. A delete must remember the text it removed.
- `MacroCommand(commands)` runs several commands as one; its `undo()` undoes them in reverse order.
- `History` with:
  - `run(command)`: executes the command, stores it, and **clears the redo stack**;
  - `undo()`: undoes the most recent command; returns `True`, or `False` if there was nothing to undo;
  - `redo()`: re-executes the most recently undone command; returns `True`, or `False` if nothing can be redone.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
ed = Editor()
history = History()
history.run(InsertCommand(ed, 0, "Hello"))
history.run(InsertCommand(ed, 5, " World"))
print(ed.text)
history.undo()
print(ed.text)
history.redo()
print(ed.text)
history.undo()
history.undo()
print(repr(ed.text))
print(history.undo())
history.run(InsertCommand(ed, 0, "New"))
print(history.redo())
macro = MacroCommand([InsertCommand(ed, 3, " text"), DeleteCommand(ed, 0, 1)])
history.run(macro)
print(ed.text)
history.undo()
print(ed.text)
```

### Expected output

```text
Hello World
Hello
Hello World
''
False
False
ew text
New
```

### Hints

- Use two lists as stacks: commands done and commands undone.
- A new command after an undo makes the old redo history meaningless, so clear it.
- `DeleteCommand.execute` must save `text[start:end]` in an attribute so that `undo` can put it back.
- `reversed(self.commands)` undoes a macro in the right order.

### Acceptance checklist

- [ ] Undo restores the exact previous text for insert, delete and macro commands
- [ ] Redo works after undo, and fails after a new command is run
- [ ] `undo()` and `redo()` return booleans
- [ ] The macro is a single entry in the history
- [ ] Output matches the expected output exactly

---

## T10-E10: Iterator: lazy pages and tree traversal

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Iterator protocol (`__iter__`, `__next__`), generators, `yield from`, laziness

### Problem

**Pattern: Iterator.** Write three things.

1. `PageIterator(fetch_page)`: an iterator over a paginated source. `fetch_page(n)` returns the list of items on page `n`
   (starting at 0); an empty list means there are no more pages. The iterator must be **lazy**: a page is requested only
   when all items of the previous page have been consumed. Implement `__iter__` (returns `self`) and `__next__`
   (raises `StopIteration` at the end, and must not call `fetch_page` again after the end was reached).
2. `BinaryTree`: a binary search tree with `insert(value)` (smaller values go left, others right). Iterating it yields the
   values in sorted order (in-order traversal) using a recursive generator and `yield from`. `reversed(tree)` yields them
   in descending order (implement `__reversed__`). `value in tree` works through iteration.
3. `chunked(iterable, size)`: a generator that yields lists of at most `size` items without consuming more of the input
   than needed (`itertools.islice` helps).

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
PAGES = [[1, 2, 3], [4, 5, 6], [7]]
fetched = []

def fetch_page(n):
    fetched.append(n)
    return PAGES[n] if n < len(PAGES) else []

it = PageIterator(fetch_page)
print(next(it), next(it), next(it), fetched)
print(next(it), fetched)
print(list(it), fetched)

tree = BinaryTree()
for value in [5, 3, 8, 1, 4, 9]:
    tree.insert(value)
print(list(tree))
print(list(reversed(tree)))
print(8 in tree, 7 in tree)
print(list(chunked(tree, 4)))
print(next(iter(tree)))
```

### Expected output

```text
1 2 3 [0]
4 [0, 1]
[5, 6, 7] [0, 1, 2, 3]
[1, 3, 4, 5, 8, 9]
[9, 8, 5, 4, 3, 1]
True False
[[1, 3, 4, 5], [8, 9]]
1
```

### Hints

- Keep a buffer (the current page) and a position inside it; fetch a new page only when the buffer is used up.
- An in-order traversal is: left subtree, the node's value, right subtree.
- `yield from sub_generator` re-yields everything from the sub-generator.
- `while chunk := list(islice(it, size)):` is a compact loop for `chunked`.

### Acceptance checklist

- [ ] Pages are fetched on demand (the `fetched` list in the driver proves it)
- [ ] No extra `fetch_page` call happens after the iterator is exhausted
- [ ] Tree iteration is sorted and `reversed()` is descending
- [ ] `chunked` works with any iterable, including the tree
- [ ] Output matches the expected output exactly
