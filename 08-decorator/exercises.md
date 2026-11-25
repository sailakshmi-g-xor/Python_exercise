"""# Topic 08: Decorators - Exercises

Write your solution in a file such as `t08_e01.py` and paste the driver code from "Sample input" at the
bottom, inside `if __name__ == "__main__":`. Everything the driver uses (functions, decorated functions,
imports such as `sys` or `time`) must be defined above it. Run it with `python t08_e01.py` (Windows:
`py t08_e01.py`). Your output must match "Expected output" exactly. Use only the standard library.

---

## T08-E01: Functions as objects

**Level:** Easy | **Estimated time:** 15 minutes | **Practises:** First-class functions, dispatch dictionary, higher-order functions

### Problem

Functions can be stored in variables and dictionaries, passed to other functions and returned from them.

Write:

- `add(a, b)`, `sub(a, b)` and `mul(a, b)`.
- A dictionary `OPERATIONS` mapping `"add"`, `"sub"` and `"mul"` to those functions (no `if/elif` chain).
- `calculate(op_name, a, b)` that looks the operation up and calls it. For an unknown name raise
  `ValueError(f"Unknown operation: {op_name}")`.
- `apply_twice(func, value)` returning `func(func(value))`.
- `compose(f, g)` returning a **new function** `h` such that `h(x) == f(g(x))`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(calculate("add", 2, 3))
print(calculate("mul", 4, 5))
print(apply_twice(lambda s: s + "!", "hey"))
shout = compose(str.upper, lambda s: s + "!")
print(shout("hello"))
print(add.__name__, callable(add), type(add).__name__)
print(sorted(OPERATIONS))
try:
    calculate("pow", 2, 3)
except ValueError as err:
    print("Error:", err)
```

### Expected output

```text
5
20
hey!!
HELLO!
add True function
['add', 'mul', 'sub']
Error: Unknown operation: pow
```

### Hints

- Store the function itself, not the result: `{"add": add}`, not `{"add": add(1, 2)}`.
- `dict[key]` raises `KeyError`; catch it and raise your own `ValueError`.
- A `lambda` or an inner `def` can be returned from `compose`.
- Built-in methods are objects too: `str.upper` is a function you can pass around.

### Acceptance checklist

- [ ] `calculate` uses the dictionary and has no if/elif chain
- [ ] Unknown operations raise `ValueError` with the given message
- [ ] `compose` returns a function rather than calling `f` and `g` immediately
- [ ] Output matches the expected output exactly

---

## T08-E02: Closures: counters and multipliers

**Level:** Easy | **Estimated time:** 15 minutes | **Practises:** Closures, `nonlocal`, late-binding pitfall

### Problem

A closure is an inner function that remembers variables from the function that created it.

- `make_counter(start=0, step=1)` returns a function. The first call returns `start`, the next `start + step`,
  and so on. Each counter keeps its own state (use `nonlocal`).
- `make_multiplier(n)` returns a function that multiplies its argument by `n`.
- `build_multipliers(factors)` returns a list of multiplier functions, one per factor.

The driver also prints a "broken" list built with lambdas in a loop; study the output and explain why every
function multiplies by 4.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
c1 = make_counter()
c2 = make_counter(start=10, step=5)
print(c1(), c1(), c1())
print(c2(), c2())
double = make_multiplier(2)
print(double(21))
print([f(10) for f in build_multipliers([2, 3, 4])])
print(double.__closure__[0].cell_contents)
broken = [lambda x: x * factor for factor in [2, 3, 4]]
print([f(10) for f in broken])
```

### Expected output

```text
0 1 2
10 15
42
[20, 30, 40]
2
[40, 40, 40]
```

### Hints

- Without `nonlocal`, `count += 1` would try to create a new local variable and fail.
- To start the first call at `start`, begin the stored count one step earlier.
- Closures capture the **variable**, not its value at creation time. Calling a factory function such as `make_multiplier` gives every closure its own variable.
- `f.__closure__[0].cell_contents` lets you peek at a captured value.

### Acceptance checklist

- [ ] Two counters do not interfere with each other
- [ ] `build_multipliers` returns `[20, 30, 40]` when called on 10
- [ ] You can explain the `[40, 40, 40]` result of the broken list
- [ ] Output matches the expected output exactly

---

## T08-E03: Your first decorators

**Level:** Easy | **Estimated time:** 15 minutes | **Practises:** Writing a decorator, `*args` and `**kwargs`, `@` syntax

### Problem

Write two decorators that work on functions with any signature:

- `announce` prints `Calling <function name>` before the call and `Finished <function name>` afterwards, and
  returns the original result.
- `shout` upper-cases the (string) result of the function.

Then define `add(a, b)` decorated with `@announce`, and `greet(name, punctuation="!")` decorated with `@shout`
returning `f"hello {name}{punctuation}"`. The driver also applies `announce` manually (`sub = announce(sub)`)
to show that `@announce` is only shorthand, and prints `add.__name__`. Notice that it is `wrapper`; the next
exercise fixes that.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(add(2, 3))
print(greet("ana"))
print(greet("ben", punctuation="?"))

def sub(a, b):
    return a - b

# Same as writing @announce above the def
sub = announce(sub)
print(sub(10, 4))
print(add.__name__)
```

### Expected output

```text
Calling add
Finished add
5
HELLO ANA!
HELLO BEN?
Calling sub
Finished sub
6
wrapper
```

### Hints

- The pattern is: define `wrapper(*args, **kwargs)` inside the decorator, call the original function, return `wrapper`.
- Do not forget to `return` the result of the original function from `wrapper`.
- A decorator returns the wrapper itself; it does not call it.

### Acceptance checklist

- [ ] Decorated functions accept positional and keyword arguments
- [ ] Return values are passed through
- [ ] `sub = announce(sub)` works exactly like `@announce`
- [ ] Output matches the expected output exactly

---

## T08-E04: Logging decorator with functools.wraps

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** `functools.wraps`, the `logging` module, exceptions inside wrappers

### Problem

Write a decorator `log_calls` that uses a logger named `"calls"` (`logging.getLogger("calls")`):

- Before the call log at INFO: `Calling add(2, 3)` (positional args shown with `repr`, keyword args as `name=value`).
- After a successful call log at INFO: `add returned 5`.
- If the function raises, log at ERROR: `fail raised ZeroDivisionError: nope` and **re-raise** the exception.
- Use `functools.wraps` so the wrapper keeps the original `__name__` and `__doc__`.

Define `add(a, b)` with docstring `"Add two numbers."` and `fail()` raising `ZeroDivisionError("nope")`, both
decorated. The driver configures logging with `basicConfig`; it needs `import sys` and `import logging`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(levelname)s %(message)s")
add(2, 3)
add(a=1, b=2)
print(add.__name__, "-", add.__doc__)
print(add.__wrapped__(10, 20))
try:
    fail()
except ZeroDivisionError:
    print("caught")
```

### Expected output

```text
INFO Calling add(2, 3)
INFO add returned 5
INFO Calling add(a=1, b=2)
INFO add returned 3
add - Add two numbers.
30
INFO Calling fail()
ERROR fail raised ZeroDivisionError: nope
caught
```

### Hints

- Build the argument text with `", ".join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])`.
- Use lazy logging style: `logger.info("Calling %s(%s)", name, text)`.
- A bare `raise` inside `except` re-raises the same exception.
- `wrapper.__wrapped__` is added by `functools.wraps` and points to the original function.

### Acceptance checklist

- [ ] Exceptions still reach the caller after being logged
- [ ] `add.__name__` is `add` and `add.__doc__` is kept
- [ ] Log lines use the format of the expected output
- [ ] Output matches the expected output exactly

---

## T08-E05: Decorators with arguments

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** Decorator factories (three nested functions), validation at decoration time

### Problem

A decorator that takes arguments is a function that **returns** a decorator.

- `repeat(times)` runs the decorated function `times` times and returns the list of all results. `repeat(0)`
  (or less) must raise `ValueError("times must be at least 1")` immediately, when the decorator is created.
- `clamp_result(low, high)` forces the numeric result of the decorated function into the range `low..high`.

Use `functools.wraps` in both. Define `hello(name)` decorated with `@repeat(3)`; it prints `Hello, <name>` and
returns the upper-cased name. Define `score(raw)` decorated with `@clamp_result(0, 100)` returning `raw * 2`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(hello("Ana"))
print(score(10), score(70), score(-5))
print(score.__name__)
try:
    repeat(0)
except ValueError as err:
    print("Error:", err)
```

### Expected output

```text
Hello, Ana
Hello, Ana
Hello, Ana
['ANA', 'ANA', 'ANA']
20 100 0
score
Error: times must be at least 1
```

### Hints

- Structure: `def repeat(times): def decorator(func): def wrapper(...): ...; return wrapper; return decorator; `.
- `@repeat(3)` first calls `repeat(3)`, then applies the returned decorator to the function.
- `max(low, min(high, value))` clamps a value.

### Acceptance checklist

- [ ] `hello` prints three times and returns a list of three results
- [ ] Invalid `times` fails when the decorator is created, not when the function is called
- [ ] `score.__name__` is still `score`
- [ ] Output matches the expected output exactly

---

## T08-E06: Timing decorator

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** Wrapper attributes, `time.perf_counter`, `try/finally`

### Problem

Write a decorator `timer` that measures how long each call takes with `time.perf_counter()` and stores
statistics as attributes on the wrapper function:

- `calls`: number of calls so far,
- `last_duration`: seconds taken by the latest call,
- `total_time`: sum of all durations.

Failed calls must be timed and counted too, and the exception must still propagate. Keep the original name
with `functools.wraps`.

Define `slow(n)` (sleeps 0.05 seconds, returns `n * 2`) and `boom()` (raises `RuntimeError("failed")`), both
decorated. The driver uses `time`, so import it.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(slow(4))
print(slow(5))
print(slow.calls)
print(slow.last_duration >= 0.04)
print(slow.total_time >= 0.08)
print(slow.total_time < 1)
try:
    boom()
except RuntimeError:
    print(boom.calls)
print(slow.__name__)
```

### Expected output

```text
8
10
2
True
True
True
1
slow
```

### Hints

- Functions are objects, so `wrapper.calls = 0` is legal; set the initial values before returning `wrapper`.
- Put the bookkeeping in a `finally:` block so it runs on success and on failure.
- Timings differ on every run, so the driver only prints comparisons such as `last_duration >= 0.04`.

### Acceptance checklist

- [ ] `calls`, `last_duration` and `total_time` update on every call
- [ ] An exception inside the function is still counted and still raised
- [ ] The decorated function keeps its name
- [ ] Output matches the expected output exactly

---

## T08-E07: Caching: memoize and lru_cache

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Memoization, `functools.lru_cache`, `cache_info()`, `cache_clear()`, cache eviction

### Problem

Compare three versions of a recursive Fibonacci function.

1. `fib_plain(n)`: plain recursion.
2. `fib_memo(n)`: decorated with your own `memoize` decorator (store results in a dict keyed by the argument
   tuple; expose the dict as `wrapper.cache`).
3. `fib_lru(n)`: decorated with `functools.lru_cache(maxsize=None)`.

Each version increments its own counter in the dictionary `calls` (`"plain"`, `"memo"`, `"lru"`) every time the
body actually runs. Also define `square(n)` with `@lru_cache(maxsize=2)` and observe `cache_info()` after calling it
with 1, 2, 1, 3, 2.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(fib_plain(20), calls["plain"])
print(fib_memo(20), calls["memo"], len(fib_memo.cache))
print(fib_lru(20), calls["lru"])
print(fib_lru.cache_info())
fib_lru.cache_clear()
print(fib_lru.cache_info().currsize)

for n in (1, 2, 1, 3, 2):
    square(n)
print(square.cache_info())
```

### Expected output

```text
6765 21891
6765 21 21
6765 21
CacheInfo(hits=18, misses=21, maxsize=None, currsize=21)
0
CacheInfo(hits=1, misses=4, maxsize=2, currsize=2)
```

### Hints

- The counter lives inside the function body, so a cache hit does not increase it.
- Cache keys must be hashable; a tuple of positional arguments works.
- `cache_info()` shows hits, misses, maxsize and currsize.
- With `maxsize=2` the least recently used entry is evicted when a third value arrives.

### Acceptance checklist

- [ ] `fib_plain(20)` runs its body 21891 times; the cached versions only 21 times
- [ ] `fib_memo.cache` holds 21 entries
- [ ] You can explain why `square.cache_info()` shows 4 misses
- [ ] Output matches the expected output exactly

---

## T08-E08: Stacking decorators

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** Decorator order, nested wrapping, execution order

### Problem

When decorators are stacked, the one closest to the function is applied first.

- `bold` wraps the result in `<b>...</b>`; `italic` wraps it in `<i>...</i>`.
- `trace(label)` prints `enter <label>` before and `exit <label>` after the call.

Define `hello()` returning `"hello"` decorated with `@bold` above `@italic`, and `hello_reversed()` with the
order swapped. Define `work()` that prints `working` and returns `"done"`, decorated with `@trace("A")`,
`@trace("B")`, `@trace("C")` from top to bottom. The driver also builds the first stack manually with function
calls: `bold(italic(...))`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(hello())
print(hello_reversed())
print(work())
# The stacked syntax is shorthand for nested calls
manual = bold(italic(lambda: "hello"))
print(manual())
```

### Expected output

```text
<b><i>hello</i></b>
<i><b>hello</b></i>
enter A
enter B
enter C
working
exit C
exit B
exit A
done
<b><i>hello</i></b>
```

### Hints

- `@a` above `@b` above `def f` means `f = a(b(f))`.
- The outermost decorator runs its 'before' code first and its 'after' code last.
- Use `functools.wraps` in each decorator.

### Acceptance checklist

- [ ] `hello()` gives `<b><i>hello</i></b>` and the reversed version gives the opposite nesting
- [ ] The trace order is A, B, C on the way in and C, B, A on the way out
- [ ] You can rewrite a stacked decorator as nested calls
- [ ] Output matches the expected output exactly

---

## T08-E09: Retry decorator

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Configurable decorator, selective exception handling, backoff, callbacks

### Problem

Write `retry(attempts=3, delay=0.0, backoff=1.0, exceptions=(Exception,), on_retry=None)`.

- Call the function; if it raises one of `exceptions`, try again, up to `attempts` calls in total.
- After the last failed attempt the **original exception** propagates.
- Exceptions that are not in `exceptions` propagate immediately without any retry.
- Between attempts call `time.sleep(wait)` when `wait` is not zero. `wait` starts at `delay` and is multiplied by
  `backoff` after every sleep (so `delay=1, backoff=2` waits 1, 2, 4 seconds).
- If `on_retry` is given, call `on_retry(attempt_number, exception)` before sleeping.
- `attempts < 1` raises `ValueError("attempts must be at least 1")` when the decorator is created.
- Keep metadata with `functools.wraps`.

The driver uses three functions, with a shared dictionary `state = {"fetch": 0, "other": 0}`:
`fetch()` fails twice with `ConnectionError(f"attempt {n} failed")` then returns `"payload"`
(decorated with `attempts=3, delay=0, exceptions=(ConnectionError,)` and an `on_retry` that prints
`retry <n>: <error>`); `always_fails()` raises `ValueError("bad input")` (decorated with `attempts=2`);
`wrong_error()` raises `KeyError("not retried")` and counts its calls in `state["other"]`
(decorated with `attempts=3, exceptions=(ConnectionError,)`).

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(fetch(), state["fetch"])
try:
    always_fails()
except ValueError as err:
    print("gave up:", err)
try:
    wrong_error()
except KeyError:
    print("KeyError raised after", state["other"], "call")
try:
    retry(attempts=0)
except ValueError as err:
    print("Error:", err)
```

### Expected output

```text
retry 1: attempt 1 failed
retry 2: attempt 2 failed
payload 3
gave up: bad input
KeyError raised after 1 call
Error: attempts must be at least 1
```

### Hints

- Use `for attempt in range(1, attempts + 1)` and re-raise with a bare `raise` on the last attempt.
- Call `time.sleep` as `time.sleep(...)` (not `from time import sleep`) so tests can replace it.
- `except exceptions as exc:` accepts a tuple of exception classes.
- Use `delay=0` in your own tests so they run instantly.

### Acceptance checklist

- [ ] `fetch()` succeeds on the third call and `on_retry` fires twice
- [ ] After the final attempt the original exception reaches the caller
- [ ] An exception type not listed in `exceptions` is not retried
- [ ] Sleep times follow `delay` and `backoff`
- [ ] Output matches the expected output exactly

---

## T08-E10: Class decorators and class-based decorators

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Decorating classes, registries, `__call__`, `functools.update_wrapper`

### Problem

Decorators can receive and return classes, and a class with `__call__` can itself act as a decorator.

- `REGISTRY = {}` and a class decorator `register(cls)` that stores the class under `cls.__name__` and returns it
  unchanged.
- A class decorator `add_repr(cls)` that gives the class a `__repr__` listing its instance attributes, such as
  `Point(x=1, y=2)` (use `vars(self)` and `repr` of the values).
- A class `CountCalls` used as a function decorator: it counts calls in `self.count`, forwards the call to the original
  function, has a `reset()` method, and copies the function's `__name__` and `__doc__` with
  `functools.update_wrapper(self, func)`.

Define `Dog(name)` with `@register`, `Point(x, y)` with `@register` stacked above `@add_repr`, and
`greet(name)` (docstring `"Say hi."`, returns `f"hi {name}"`) with `@CountCalls`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
print(sorted(REGISTRY))
print(REGISTRY["Dog"] is Dog)
print(Point(1, 2))
print(repr(Point(x="a", y=None)))
print(greet("Ana"), greet("Ben"))
print(greet.count, greet.__name__, greet.__doc__)
greet.reset()
print(greet.count)
```

### Expected output

```text
['Dog', 'Point']
True
Point(x=1, y=2)
Point(x='a', y=None)
hi Ana hi Ben
2 greet Say hi.
0
```

### Hints

- A class decorator is just a function that takes a class and returns a class; you can set attributes on the class inside it.
- `cls.__repr__ = some_function` adds a method to an existing class.
- When `@CountCalls` is applied, `greet` becomes an instance of `CountCalls`; its `__call__` runs when you call `greet(...)`.
- `functools.update_wrapper(self, func)` is the non-decorator form of `wraps`.

### Acceptance checklist

- [ ] `register` leaves the class usable and returns it
- [ ] `Point(1, 2)` prints as `Point(x=1, y=2)`
- [ ] `greet.count` increases per call and `reset()` sets it to 0
- [ ] `greet.__name__` and `greet.__doc__` match the original function
- [ ] Output matches the expected output exactly
"""
