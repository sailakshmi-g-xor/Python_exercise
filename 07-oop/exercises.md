# Topic 07: Object-Oriented Programming - Exercises

Write your solution in a file such as `t07_e01.py` and paste the driver code from "Sample input" at the
bottom, inside `if __name__ == "__main__":`. Run it with `python t07_e01.py` (Windows: `py t07_e01.py`).
Your output must match "Expected output" exactly. Use only the standard library.

---

## T07-E01: Book with progress tracking

**Level:** Easy | **Estimated time:** 10 minutes | **Practises:** Classes, `__init__`, instance attributes, simple methods

### Problem

Write a class `Book` that is created with `title`, `author` and `pages`. It must also have an attribute
`current_page` that starts at `0`.

- `describe()` returns a string like `'Dune' by Frank Herbert (412 pages)` (title in single quotes).
- `read(count)` moves `current_page` forward by `count` pages but never past the last page.
- `progress()` returns the percentage read, rounded to one decimal place (`current_page / pages * 100`).

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
book = Book("Dune", "Frank Herbert", 412)
print(book.describe())
print(book.progress())
book.read(103)
print(book.current_page)
print(book.progress())
book.read(500)
print(book.current_page)
print(book.progress())
```

### Expected output

```text
'Dune' by Frank Herbert (412 pages)
0.0
103
25.0
412
100.0
```

### Hints

- Store every constructor argument on `self`, for example `self.title = title`.
- `min(a, b)` is a neat way to cap a value.
- `round(value, 1)` rounds to one decimal place.

### Acceptance checklist

- [ ] `Book` is created with three arguments and `current_page` starts at 0
- [ ] `describe()` returns the exact format shown
- [ ] Reading past the end stops at the last page
- [ ] `progress()` returns a float rounded to one decimal
- [ ] Output matches the expected output exactly

---

## T07-E02: Bank account with validation

**Level:** Easy | **Estimated time:** 15 minutes | **Practises:** Methods that change state, raising exceptions, custom exception class

### Problem

Write a custom exception `InsufficientFundsError` that inherits from `ValueError`, and a class `BankAccount`
created with `owner` and an optional starting `balance` (default `0`).

- `deposit(amount)` adds to the balance. If `amount <= 0` raise `ValueError("Deposit must be positive")`.
- `withdraw(amount)` subtracts from the balance. If `amount <= 0` raise `ValueError("Withdrawal must be positive")`.
  If `amount` is more than the balance raise `InsufficientFundsError(f"Cannot withdraw {amount}, balance is {balance}")`.
- Every successful operation is recorded in `self.history` as a tuple `("deposit", amount)` or `("withdraw", amount)`.
- `statement()` returns a multi-line string: a header `Statement for <owner>`, one line per history entry
  (kind left-aligned in 10 characters, amount right-aligned in 8 characters), and a final `Balance: <n>` line.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
acc = BankAccount("Maria")
acc.deposit(200)
acc.withdraw(75)
try:
    acc.withdraw(500)
except InsufficientFundsError as err:
    print("Error:", err)
try:
    acc.deposit(-5)
except ValueError as err:
    print("Error:", err)
print(acc.statement())
```

### Expected output

```text
Error: Cannot withdraw 500, balance is 125
Error: Deposit must be positive
Statement for Maria
deposit        200
withdraw        75
Balance: 125
```

### Hints

- A failed operation must leave the balance and the history unchanged, so validate before you modify.
- `class InsufficientFundsError(ValueError): pass` is all the exception needs.
- Format specs: `f"{kind:<10}{amount:>8}"`.
- Join lines with `"\n".join(lines)`.

### Acceptance checklist

- [ ] Invalid amounts raise `ValueError` with the given message
- [ ] Overdrawing raises `InsufficientFundsError`, which can also be caught as `ValueError`
- [ ] Failed operations do not change the balance or history
- [ ] `statement()` lines are aligned as specified
- [ ] Output matches the expected output exactly

---

## T07-E03: Employee class and static methods

**Level:** Easy | **Estimated time:** 15 minutes | **Practises:** Class attributes, `@classmethod` alternative constructors, `@staticmethod`

### Problem

Write a class `Employee` with:

- a class attribute `company = "Acme"`;
- a class attribute `headcount = 0` that increases by one every time an employee is created;
- an `__init__(name, role, salary)` that stores the three values;
- a class method `from_string(text)` that builds an employee from text like `"Ben, Tester, 4200"`
  (strip spaces, convert salary to `int`) and must work with subclasses (use `cls`);
- a static method `is_working_day(day)` that takes a `datetime.date` and returns `True` for Monday to Friday.

The driver (which uses `from datetime import date`) also shows what happens when you assign `company` on the class versus on one instance.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
e1 = Employee("Ana", "Developer", 5000)
e2 = Employee.from_string("Ben, Tester, 4200")
print(e2.name, e2.role, e2.salary)
print(Employee.headcount)
print(e1.company, e2.company)
Employee.company = "Globex"
print(e1.company, e2.company)
e2.company = "Initech"
print(e1.company, e2.company, Employee.company)
print(Employee.is_working_day(date(2026, 11, 23)))
print(Employee.is_working_day(date(2026, 11, 28)))
```

### Expected output

```text
Ben Tester 4200
2
Acme Acme
Globex Globex
Globex Initech Globex
True
False
```

### Hints

- Update the counter with `Employee.headcount += 1` inside `__init__`.
- `text.split(",")` gives the parts; `.strip()` removes spaces.
- `date.weekday()` returns 0 for Monday and 6 for Sunday.
- Assigning `e2.company = ...` creates an instance attribute that shadows the class attribute.

### Acceptance checklist

- [ ] `headcount` counts employees created by both `__init__` and `from_string`
- [ ] `from_string` is a `@classmethod` that returns `cls(...)`
- [ ] `is_working_day` is a `@staticmethod` and needs no `self`
- [ ] You can explain why `e2.company` changed but `Employee.company` did not
- [ ] Output matches the expected output exactly

---

## T07-E04: Vector2D with dunder methods

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** `__repr__`, `__str__`, operator overloading, `__eq__`, `__iter__`, `__bool__`

### Problem

Write a class `Vector2D(x, y)` that behaves like a number-ish value:

- `repr(v)` gives `Vector2D(3, 4)`; `str(v)` gives `(3, 4)`.
- `v1 + v2` and `v1 - v2` return new vectors. Adding anything that is not a `Vector2D` must raise
  the normal `TypeError` (return `NotImplemented` rather than raising yourself).
- `v * number` and `number * v` scale the vector.
- `v1 == v2` compares coordinates.
- `abs(v)` returns the length (`math.hypot`).
- `bool(v)` is `False` only for the zero vector.
- Iterating over a vector yields `x` then `y`, so `x, y = v` works.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
a = Vector2D(3, 4)
b = Vector2D(1, 2)
print(repr(a))
print(a)
print(a + b)
print(a - b)
print(a * 2)
print(2 * a)
print(abs(a))
print(a == Vector2D(3, 4))
print(a == b)
print(bool(Vector2D(0, 0)))
x, y = a
print(x, y)
try:
    a + 5
except TypeError as err:
    print("TypeError:", err)
```

### Expected output

```text
Vector2D(3, 4)
(3, 4)
(4, 6)
(2, 2)
(6, 8)
(6, 8)
5.0
True
False
False
3 4
TypeError: unsupported operand type(s) for +: 'Vector2D' and 'int'
```

### Hints

- For `3 * v` Python calls `v.__rmul__(3)`; you can reuse your `__mul__`.
- Return `NotImplemented` (not raise) when the other operand is the wrong type.
- A generator method with two `yield` statements is enough for `__iter__`.

### Acceptance checklist

- [ ] `repr` and `str` differ as shown
- [ ] Addition, subtraction and scaling return new objects and do not modify the originals
- [ ] Both `v * 2` and `2 * v` work
- [ ] `a + 5` raises `TypeError`
- [ ] Unpacking `x, y = a` works
- [ ] Output matches the expected output exactly

---

## T07-E05: Thermometer with properties

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** `@property`, setters, validation, read-only attributes, name mangling

### Problem

Write a class `Thermometer(celsius=20.0)` that stores its temperature in a protected attribute `_celsius`.

- `celsius` is a property. Its setter raises `ValueError("Temperature below absolute zero")` for values
  below `-273.15`. The constructor must go through the same setter.
- `fahrenheit` is a property with a setter (setting it updates the Celsius value).
- `kelvin` is a **read-only** property rounded to 2 decimals. Assigning to it raises `AttributeError`.
- A private counter `self.__reading_count` counts how many times the temperature has been set (including the
  constructor). Expose it through a read-only property `reading_count`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
t = Thermometer(25)
print(t.celsius, t.fahrenheit, t.kelvin)
t.fahrenheit = 212
print(t.celsius)
try:
    t.celsius = -300
except ValueError as err:
    print("Error:", err)
try:
    t.kelvin = 10
except AttributeError:
    print("kelvin is read-only")
print(t.reading_count)
print(hasattr(t, "__reading_count"))
```

### Expected output

```text
25 77.0 298.15
100.0
Error: Temperature below absolute zero
kelvin is read-only
2
False
```

### Hints

- Define the getter with `@property`, then the setter with `@celsius.setter`.
- In `__init__` write `self.celsius = celsius` (not `self._celsius = ...`) so validation runs.
- Create `self.__reading_count = 0` before the first assignment to `self.celsius`.
- Name mangling turns `__reading_count` into `_Thermometer__reading_count`; this is why `hasattr(t, "__reading_count")` is `False`.

### Acceptance checklist

- [ ] Invalid temperatures are rejected in the constructor as well as later
- [ ] Fahrenheit and Kelvin values are derived, not stored separately
- [ ] `kelvin` cannot be assigned
- [ ] `reading_count` counts the constructor assignment too
- [ ] Output matches the expected output exactly

---

## T07-E06: Shapes: inheritance and polymorphism

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** Inheritance, `super()`, method overriding, polymorphism, `isinstance`

### Problem

Build a small hierarchy:

- `Shape(name)` with an `area()` method that raises `NotImplementedError("Subclasses must implement area()")`
  and a `describe()` method returning `"<name> with area <area to 2 decimals>"`. `describe()` must call `self.area()`.
- `Circle(radius)` named `"Circle"`.
- `Rectangle(width, height, name="Rectangle")`.
- `Square(side)` that **inherits from `Rectangle`** and is named `"Square"`; it must call `super().__init__`.

Then use the shapes polymorphically: describe each one, find the biggest by area, and sort them.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
shapes = [Circle(1.5), Rectangle(3, 4), Square(2)]
for shape in shapes:
    print(shape.describe())
biggest = max(shapes, key=lambda s: s.area())
print("Biggest:", biggest.name)
print([s.name for s in sorted(shapes, key=lambda s: s.area())])
print(isinstance(shapes[2], Rectangle), isinstance(shapes[2], Shape))
print(issubclass(Circle, Rectangle))
try:
    Shape("Blob").describe()
except NotImplementedError as err:
    print("NotImplementedError:", err)
```

### Expected output

```text
Circle with area 7.07
Rectangle with area 12.00
Square with area 4.00
Biggest: Rectangle
['Square', 'Circle', 'Rectangle']
True True
False
NotImplementedError: Subclasses must implement area()
```

### Hints

- `describe()` is written once in `Shape` and works for every subclass thanks to polymorphism.
- `Square.__init__` can call `super().__init__(side, side, name="Square")`.
- `max(shapes, key=lambda s: s.area())` finds the biggest shape.
- `math.pi * r ** 2` for the circle.

### Acceptance checklist

- [ ] `Square` has no `area()` of its own
- [ ] `Shape("Blob").describe()` raises `NotImplementedError`
- [ ] `isinstance` and `issubclass` give the answers shown
- [ ] Output matches the expected output exactly

---

## T07-E07: Inventory records with dataclasses

**Level:** Medium | **Estimated time:** 20 minutes | **Practises:** `@dataclass`, `field(default_factory=...)`, `__post_init__`, `frozen`, `order`, `asdict`, `replace`

### Problem

Use the `dataclasses` module.

1. `Product` with fields `name: str`, `price: float`, `quantity: int = 0` and `tags: list` (default must be a
   new empty list per object). Use `__post_init__` to raise `ValueError("price cannot be negative")`. Add a
   method `total_value()` returning `round(price * quantity, 2)`.
2. `Version` with `major`, `minor=0`, `patch=0`. It must be **frozen** (immutable) and **orderable**, and
   `str(v)` returns `"1.2.3"`.

The driver also uses `dataclasses.asdict` and `dataclasses.replace`, so import them too.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
p1 = Product("Pen", 1.5, 10)
p2 = Product("Pen", 1.5, 10)
p3 = Product("Notebook", 3.25)
print(p1)
print(p1 == p2, p1 is p2)
print(p1.total_value(), p3.total_value())
p1.tags.append("office")
print(p2.tags)
print(asdict(p1))
print(replace(p3, quantity=4))
try:
    Product("Broken", -1)
except ValueError as err:
    print("Error:", err)

versions = [Version(1, 2, 3), Version(1, 10), Version(0, 9, 9)]
print([str(v) for v in sorted(versions)])
try:
    versions[0].major = 2
except Exception as err:
    print(type(err).__name__)
```

### Expected output

```text
Product(name='Pen', price=1.5, quantity=10, tags=[])
True False
15.0 0.0
[]
{'name': 'Pen', 'price': 1.5, 'quantity': 10, 'tags': ['office']}
Product(name='Notebook', price=3.25, quantity=4, tags=[])
Error: price cannot be negative
['0.9.9', '1.2.3', '1.10.0']
FrozenInstanceError
```

### Hints

- A mutable default such as `tags: list = []` is an error; use `field(default_factory=list)`.
- `@dataclass(frozen=True, order=True)` generates comparison methods based on field order.
- Version sorting is numeric (1.10.0 comes after 1.2.3), because fields are integers, not strings.
- `replace(obj, quantity=4)` returns a modified copy.

### Acceptance checklist

- [ ] Two products with the same field values are equal but not the same object
- [ ] Changing `p1.tags` does not affect `p2.tags`
- [ ] Negative prices are rejected
- [ ] Assigning to a frozen `Version` field raises `FrozenInstanceError`
- [ ] Output matches the expected output exactly

---

## T07-E08: Composition: cars and stacks

**Level:** Medium | **Estimated time:** 25 minutes | **Practises:** Composition over inheritance, delegation, encapsulating a list

### Problem

Part A. Write `PetrolEngine` and `ElectricEngine`, each with `start()` and `refuel()` methods returning
different strings (`"Petrol engine roars"` / `"Filling the tank"` and `"Electric motor hums"` / `"Charging the battery"`).
Write `Car(model, engine)` which **has an** engine: `start()` and `refuel()` return `"<model>: <engine text>"`,
and `swap_engine(new_engine)` replaces the engine at run time.

Part B. Write `Stack` that stores items in a private list `_items` (composition) and offers only `push`, `pop`
(raising `IndexError("pop from empty stack")` when empty), `peek` and `len()`. Also write `LeakyStack(list)`
(inheritance) with a `push` method to see the difference: the leaky version exposes list methods such as `insert`.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
car = Car("Golf", PetrolEngine())
print(car.start())
print(car.refuel())
car.swap_engine(ElectricEngine())
print(car.start())
print(car.refuel())

s = Stack()
s.push(1)
s.push(2)
print(len(s), s.peek(), s.pop(), len(s))
print(hasattr(s, "insert"))
leaky = LeakyStack()
leaky.push(1)
print(hasattr(leaky, "insert"))
```

### Expected output

```text
Golf: Petrol engine roars
Golf: Filling the tank
Golf: Electric motor hums
Golf: Charging the battery
2 2 2 1
False
True
```

### Hints

- `Car` never checks the engine's type; it just calls `self.engine.start()` (duck typing).
- Use `__len__` so that `len(stack)` works.
- Ask yourself: is a stack a list, or does it use a list?

### Acceptance checklist

- [ ] Swapping the engine changes the car's behaviour without a new `Car`
- [ ] `Stack` does not have an `insert` attribute but `LeakyStack` does
- [ ] Popping an empty `Stack` raises `IndexError`
- [ ] You can state one advantage of composition over inheritance
- [ ] Output matches the expected output exactly

---

## T07-E09: Payroll with abstract base classes

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** `abc.ABC`, `@abstractmethod`, abstract properties, polymorphic processing

### Problem

Model a payroll system.

- `Employee(ABC)` created with `name`. It declares an abstract property `kind` and an abstract method
  `monthly_pay()`, and has a concrete `payslip()` returning `"<name> (<kind>): <pay to 2 decimals>"`.
- `SalariedEmployee(name, annual_salary)`: kind `"salaried"`, pay is `annual_salary / 12`.
- `HourlyEmployee(name, rate, hours)`: kind `"hourly"`. The first 160 hours are paid at `rate`; hours above 160
  are paid at 1.5 times `rate`.
- `CommissionEmployee(name, base, sales, rate)`: kind `"commission"`, pay is `base + sales * rate`.
- `Payroll(employees)` with `total()` and `report()` (one payslip per line, then `TOTAL: <total to 2 decimals>`).

Trying to instantiate `Employee` directly must raise `TypeError`; the driver prints a fixed message when it does.

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
try:
    Employee("Nobody")
except TypeError:
    print("TypeError: Employee is abstract")

staff = [
    SalariedEmployee("Ana", 48000),
    HourlyEmployee("Ben", 20, 170),
    CommissionEmployee("Chloe", 1500, 20000, 0.05),
]
print(Payroll(staff).report())
```

### Expected output

```text
TypeError: Employee is abstract
Ana (salaried): 4000.00
Ben (hourly): 3500.00
Chloe (commission): 2500.00
TOTAL: 10000.00
```

### Hints

- Stack `@property` above `@abstractmethod` for an abstract property.
- A class attribute such as `kind = "salaried"` satisfies an abstract property in a subclass.
- `min(hours, 160)` and `max(hours - 160, 0)` split regular and overtime hours.
- `Payroll` only relies on `monthly_pay()`; it needs no `isinstance` checks.

### Acceptance checklist

- [ ] `Employee("x")` raises `TypeError`
- [ ] A subclass missing `monthly_pay` could not be instantiated (try it)
- [ ] Overtime is calculated correctly (170 hours at rate 20 gives 3500)
- [ ] `Payroll` works with any future employee subclass without changes
- [ ] Output matches the expected output exactly

---

## T07-E10: Money value object

**Level:** Hard (Challenge) | **Estimated time:** 30 minutes | **Practises:** Value objects, `functools.total_ordering`, `__hash__`, `__radd__`, `__slots__`, safe arithmetic

### Problem

Write an immutable `Money` class that stores whole **cents** (an integer) and a currency code (default `"EUR"`).

- `Money(cents, currency="EUR")`, read-only properties `cents` and `currency`, and `Money.from_str("12.50")`
  (also accept `"2.5"` meaning 2.50 and negative values such as `"-3.05"`).
- `repr` gives `Money(250, 'EUR')`; `str` gives `12.50 EUR` (negative: `-12.50 EUR`).
- `+` and `-` between two `Money` values; mixing currencies raises `ValueError("Currency mismatch: EUR vs USD")`.
- `*` with an `int` (both `m * 3` and `3 * m`); unary minus.
- Equality, hashing (equal values must hash equal, so sets work), and ordering with all of `<, <=, >, >=`
  (use `functools.total_ordering`; comparing different currencies raises `ValueError`).
- `sum([...])` must work, so `0 + money` has to be supported.
- `bool(Money(0))` is `False`.
- `split(parts)` returns a list of `parts` shares that add up exactly to the original amount; leftover cents go
  to the first shares (10.00 split 3 ways is 3.34, 3.33, 3.33).

### Sample input

Your solution must work with this driver code, placed at the bottom of your file:

```python
price = Money.from_str("12.50")
tip = Money.from_str("2.5")
print(price, repr(tip))
print(price + tip)
print(price - tip * 2)
print(3 * price)
print(sum([price, tip, Money(99)]))
print(sorted([price, tip, Money(99)]))
print(max(price, tip), price >= tip, price == Money(1250))
print(len({price, Money(1250), tip}))
print([str(m) for m in Money.from_str("10.00").split(3)])
print(-price, bool(Money(0)))
try:
    price + Money(100, "USD")
except ValueError as err:
    print("Error:", err)
```

### Expected output

```text
12.50 EUR Money(250, 'EUR')
15.00 EUR
7.50 EUR
37.50 EUR
15.99 EUR
[Money(99, 'EUR'), Money(250, 'EUR'), Money(1250, 'EUR')]
12.50 EUR True True
2
['3.34 EUR', '3.33 EUR', '3.33 EUR']
-12.50 EUR False
Error: Currency mismatch: EUR vs USD
```

### Hints

- Never use floats for money; `divmod(cents, 100)` gives whole and fractional parts.
- `sum()` starts with `0`, so `__radd__` can return `self` when the other operand is `0`.
- If you define `__eq__` you must define `__hash__` yourself, or the class becomes unhashable.
- `divmod(total_cents, parts)` gives the base share and the number of shares that get one extra cent.
- `__slots__ = ("_cents", "_currency")` prevents accidental new attributes.

### Acceptance checklist

- [ ] No floats are used for amounts
- [ ] Currency mismatches are rejected for `+`, `-` and comparisons
- [ ] `sum()`, `sorted()` and `max()` work on a list of `Money`
- [ ] Equal values collapse in a `set`
- [ ] The shares from `split` always add up to the original amount
- [ ] Output matches the expected output exactly
