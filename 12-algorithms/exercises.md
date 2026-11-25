# Topic 12: Algorithms - Exercises

Each exercise asks you to write one Python file. Use the function names given in the problem
statement. The sample input is the script at the bottom of the file, under
`if __name__ == "__main__":`. Your output must match the expected output.

Do not use the built-in shortcuts that would solve the exercise for you. For example, do not use
`sorted()` or `list.sort()` inside your own sort functions, or `list.index()` inside your own
search functions. You may use them to check your answers.

Use only the standard library. Run your file with `python3 my_file.py` on Ubuntu, or `python my_file.py` on Windows.

---

## T12-E01 Linear search and binary search

**Level:** Easy | **Time:** 15 minutes

### Problem statement

Write `linear_search(items, target)` and `binary_search(items, target)`. Both return a tuple
`(index, comparisons)`. The index is `-1` when the target is missing, and `comparisons` counts
how many list items you compared with the target. Binary search may assume that `items` is
sorted. Then write `first_occurrence(items, target)`. It returns the leftmost index of `target`
in a sorted list that may contain duplicates.

### Sample input

```python
numbers = list(range(0, 200, 2))  # 0, 2, 4, ..., 198 (100 items)
print("linear 150:", linear_search(numbers, 150))
print("binary 150:", binary_search(numbers, 150))
print("linear 151:", linear_search(numbers, 151))
print("binary 151:", binary_search(numbers, 151))
print("first 5 in [1,3,5,5,5,8]:", first_occurrence([1, 3, 5, 5, 5, 8], 5))
```

### Expected output

```text
linear 150: (75, 76)
binary 150: (75, 6)
linear 151: (-1, 100)
binary 151: (-1, 7)
first 5 in [1,3,5,5,5,8]: 2
```

### Hints

- Binary search keeps two bounds, `lo` and `hi`. Each step looks at `mid = (lo + hi) // 2` and throws away half of the list.
- The loop condition is `while lo <= hi`. If you get it wrong, the search misses the last item.
- In `first_occurrence`, record a match but keep searching to the left.

### Acceptance checklist

- [ ] Both searches find every item in the list and return `-1` for missing items.
- [ ] Binary search on 100 items never needs more than 7 comparisons.
- [ ] `binary_search([], 5)` returns `(-1, 0)`.

---

## T12-E02 Bubble sort and selection sort

**Level:** Easy | **Time:** 20 minutes

### Problem statement

Write `bubble_sort(items)` and `selection_sort(items)`. Each returns a tuple
`(sorted_copy, swaps)` and leaves the input list unchanged. Bubble sort must stop early if a
whole pass makes no swaps.

### Sample input

```python
data = [64, 25, 12, 22, 11]
print("input:    ", data)
print("bubble:   ", bubble_sort(data))
print("selection:", selection_sort(data))
print("already sorted bubble:", bubble_sort([1, 2, 3, 4]))
print("input unchanged:", data)
```

### Expected output

```text
input:     [64, 25, 12, 22, 11]
bubble:    ([11, 12, 22, 25, 64], 9)
selection: ([11, 12, 22, 25, 64], 3)
already sorted bubble: ([1, 2, 3, 4], 0)
input unchanged: [64, 25, 12, 22, 11]
```

### Hints

- Start with `a = list(items)` so you sort a copy.
- After pass `k` of bubble sort, the last `k` items are already in their final place, so the inner loop can get shorter each time.
- Selection sort finds the smallest remaining item and swaps it into place once per pass, so it makes far fewer swaps.

### Acceptance checklist

- [ ] Sorting an already sorted list with bubble sort reports 0 swaps.
- [ ] The input list is unchanged afterwards.
- [ ] Both functions give the same result as `sorted()` on random lists.

---

## T12-E03 Insertion sort with a trace

**Level:** Easy | **Time:** 15 minutes

### Problem statement

Write `insertion_sort(items, key=lambda x: x, trace=False)`. It returns a new sorted list. When
`trace` is `True`, print the list after each pass as `pass i: [...]`. The `key` function chooses
what to compare, just as with `sorted`. Equal keys must keep their original order, which means
the sort is stable.

### Sample input

```python
result = insertion_sort([5, 2, 4, 6, 1, 3], trace=True)
print("sorted:", result)
people = [("Ana", 31), ("Ben", 25), ("Cy", 31), ("Di", 19)]
print("by age:", insertion_sort(people, key=lambda p: p[1]))
```

### Expected output

```text
pass 1: [2, 5, 4, 6, 1, 3]
pass 2: [2, 4, 5, 6, 1, 3]
pass 3: [2, 4, 5, 6, 1, 3]
pass 4: [1, 2, 4, 5, 6, 3]
pass 5: [1, 2, 3, 4, 5, 6]
sorted: [1, 2, 3, 4, 5, 6]
by age: [('Di', 19), ('Ben', 25), ('Ana', 31), ('Cy', 31)]
```

### Hints

- Take `current = a[i]` and shift every larger item one place to the right. Then drop `current` into the gap.
- Use `>` rather than `>=` when you compare keys. That is what keeps the sort stable.

### Acceptance checklist

- [ ] The trace lines match the expected output exactly.
- [ ] `("Ana", 31)` stays before `("Cy", 31)` when you sort by age.
- [ ] An empty list and a one-item list both work.

---

## T12-E04 Merge sort and quick sort

**Level:** Medium | **Time:** 30 minutes

### Problem statement

Write `merge(left, right)`, which merges two sorted lists, and `merge_sort(items)`, which uses it
recursively. Then write `quick_sort(items)`. It picks the middle element as the pivot and builds
three lists: items less than, equal to and greater than the pivot. Both sorts return new lists.

### Sample input

```python
data = [38, 27, 43, 3, 9, 82, 10, 3]
print("merge([1, 4, 7], [2, 3, 9]):", merge([1, 4, 7], [2, 3, 9]))
print("merge sort:", merge_sort(data))
print("quick sort:", quick_sort(data))
print("words:", merge_sort(["pear", "apple", "fig", "banana"]))
print("empty:", quick_sort([]))
```

### Expected output

```text
merge([1, 4, 7], [2, 3, 9]): [1, 2, 3, 4, 7, 9]
merge sort: [3, 3, 9, 10, 27, 38, 43, 82]
quick sort: [3, 3, 9, 10, 27, 38, 43, 82]
words: ['apple', 'banana', 'fig', 'pear']
empty: []
```

### Hints

- Base case: a list with 0 or 1 items is already sorted.
- `merge` walks both lists with two indexes. When one list runs out, add the rest of the other.
- The "equal" list is what stops quick sort from recursing forever on duplicates.
- Discuss with a partner: what is the Big-O of each sort, and when does quick sort get slow?

### Acceptance checklist

- [ ] Both sorts handle duplicates, negative numbers, strings and empty lists.
- [ ] `merge` takes linear time. It does not call `sorted()`.
- [ ] Both sorts match `sorted()` on 20 random lists.

---

## T12-E05 Two pointers

**Level:** Medium | **Time:** 20 minutes

### Problem statement

Solve four small problems with two indexes that move toward each other or in the same direction:

1. `pair_with_sum(sorted_nums, target)` returns the first pair whose sum is `target`, or `None`.
2. `remove_duplicates(sorted_nums)` removes duplicates **in place** and returns the new length.
3. `reverse_words(sentence)` swaps words from both ends.
4. `merge_sorted(a, b)` merges two sorted lists.

### Sample input

```python
print("pair sum 10:", pair_with_sum([1, 2, 3, 4, 6, 8, 11], 10))
print("pair sum 100:", pair_with_sum([1, 2, 3], 100))
nums = [1, 1, 2, 3, 3, 3, 4]
n = remove_duplicates(nums)
print("unique length:", n, "list:", nums)
print("reverse words:", reverse_words("the quick brown fox"))
print("merge sorted:", merge_sorted([1, 5, 9], [2, 3, 10, 12]))
```

### Expected output

```text
pair sum 10: (2, 8)
pair sum 100: None
unique length: 4 list: [1, 2, 3, 4]
reverse words: fox brown quick the
merge sorted: [1, 2, 3, 5, 9, 10, 12]
```

### Hints

- For a pair sum: if the sum is too small, move the left pointer right. If it is too big, move the right pointer left.
- For duplicates, a "read" pointer scans every item and a "write" pointer marks where the next unique value goes.
- Each solution should make a single pass over the data.

### Acceptance checklist

- [ ] `remove_duplicates` changes the list that was passed in (check it after the call).
- [ ] `pair_with_sum` returns `None` when no pair exists.
- [ ] There are no nested loops.

---

## T12-E06 Sliding window

**Level:** Medium | **Time:** 25 minutes

### Problem statement

Write these functions:

- `max_sum_window(nums, k)` returns `(best_sum, start_index)` for the `k` consecutive numbers with
  the largest sum. It raises `ValueError` when `k` is not between 1 and `len(nums)`.
- `moving_average(nums, k)` returns the averages of each window of size `k`, rounded to 2 decimals.
- `longest_unique_substring(text)` returns the longest substring with no repeated character.
- `shortest_subarray_at_least(nums, target)` returns the length of the shortest run of positive
  numbers whose sum is at least `target`, or 0 if there is none.

### Sample input

```python
temps = [21, 23, 19, 25, 30, 28, 18]
print("best 3-day sum:", max_sum_window(temps, 3))
print("3-day moving average:", moving_average(temps, 3))
for word in ["abcabcbb", "pwwkew", "bbbb"]:
    print(f"longest unique in {word!r}:", longest_unique_substring(word))
print("shortest >= 7 in [2,3,1,2,4,3]:", shortest_subarray_at_least([2, 3, 1, 2, 4, 3], 7))
```

### Expected output

```text
best 3-day sum: (83, 3)
3-day moving average: [21.0, 22.33, 24.67, 27.67, 25.33]
longest unique in 'abcabcbb': abc
longest unique in 'pwwkew': wke
longest unique in 'bbbb': b
shortest >= 7 in [2,3,1,2,4,3]: 2
```

### Hints

- Fixed window: to move the window one step, add the new item and subtract the item that leaves.
- Variable window: grow the right edge, then shrink the left edge while the condition still holds.
- For unique substrings, a dict of the last index where each character was seen lets the left edge jump forward.

### Acceptance checklist

- [ ] Each function makes a single pass, so it runs in O(n) time.
- [ ] `longest_unique_substring("abba")` returns `"ab"`.
- [ ] A bad `k` raises `ValueError`.

---

## T12-E07 Prefix sums

**Level:** Medium | **Time:** 20 minutes

### Problem statement

Write these functions:

- `build_prefix(nums)` returns a list where `prefix[i]` is the sum of `nums[0:i]`. The list has `len(nums) + 1` entries.
- `range_sum(prefix, left, right)` returns the sum of `nums[left..right]`, inclusive, in O(1) time.
- `equilibrium_index(nums)` returns the first index where the sum to its left equals the sum to its right, or `-1`.
- `count_subarrays_with_sum(nums, k)` counts the subarrays that sum to `k`, in one pass, using a dict of prefix sums.

### Sample input

```python
sales = [5, 3, 8, 6, 1, 4]
prefix = build_prefix(sales)
print("prefix:", prefix)
print("sum days 1..3:", range_sum(prefix, 1, 3))
print("sum days 0..5:", range_sum(prefix, 0, 5))
print("equilibrium of [1, 7, 3, 6, 5, 6]:", equilibrium_index([1, 7, 3, 6, 5, 6]))
print("subarrays summing to 3 in [1, 2, 1, 2, 1]:", count_subarrays_with_sum([1, 2, 1, 2, 1], 3))
```

### Expected output

```text
prefix: [0, 5, 8, 16, 22, 23, 27]
sum days 1..3: 17
sum days 0..5: 27
equilibrium of [1, 7, 3, 6, 5, 6]: 3
subarrays summing to 3 in [1, 2, 1, 2, 1]: 4
```

### Hints

- `range_sum` is `prefix[right + 1] - prefix[left]`.
- A subarray ending here sums to `k` when some earlier prefix equals `current - k`. Count how often each prefix value has appeared.
- Start the counting dict as `{0: 1}` so subarrays that start at index 0 are counted.

### Acceptance checklist

- [ ] `range_sum` agrees with `sum(nums[left:right + 1])` for every valid range.
- [ ] `count_subarrays_with_sum` agrees with a brute-force double loop on random data.
- [ ] Negative numbers work.

---

## T12-E08 BFS and DFS

**Level:** Medium | **Time:** 25 minutes

### Problem statement

Use the graph `GRAPH` from the sample, a dict that maps each vertex to a list of neighbours, and write these functions:

- `bfs_order(graph, start)` returns the vertices in breadth-first order.
- `dfs_order(graph, start)` returns the vertices in depth-first order, written recursively.
- `shortest_path(graph, start, goal)` returns the path with the fewest edges, or `None`.
- `count_islands(grid)` takes a list of strings and counts groups of `#` cells that touch up, down, left or right.

### Sample input

```python
GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print("BFS from A:", bfs_order(GRAPH, "A"))
print("DFS from A:", dfs_order(GRAPH, "A"))
print("shortest A->F:", shortest_path(GRAPH, "A", "F"))
print("shortest D->F:", shortest_path(GRAPH, "D", "F"))
grid = [
    "##..#",
    "#...#",
    "..#..",
    "....#",
]
print("islands:", count_islands(grid))
```

### Expected output

```text
BFS from A: ['A', 'B', 'C', 'D', 'E', 'F']
DFS from A: ['A', 'B', 'D', 'E', 'F', 'C']
shortest A->F: ['A', 'C', 'F']
shortest D->F: ['D', 'B', 'E', 'F']
islands: 4
```

### Hints

- BFS uses `collections.deque` as a queue. DFS uses recursion, or a list used as a stack.
- Mark a vertex as seen when you add it to the queue, not when you take it out. That stops duplicates.
- To rebuild a shortest path, store `parent[child] = vertex` and walk backwards from the goal.

### Acceptance checklist

- [ ] The BFS and DFS orders match the expected output, because neighbours are visited in list order.
- [ ] `shortest_path` returns `None` for an unreachable goal.
- [ ] `count_islands` does not count diagonal neighbours as touching.

---

## T12-E09 Greedy algorithms

**Level:** Medium | **Time:** 20 minutes

### Problem statement

Write these functions:

- `make_change(amount, coins=(200, 100, 50, 20, 10, 5, 2, 1))` returns a dict `{coin: count}`, always taking the largest coin first.
- `select_activities(activities)` takes `(name, start, end)` tuples and picks the largest set of
  activities that do not overlap, by always choosing the one that ends first.
- `fractional_knapsack(items, capacity)` takes `(name, weight, value)` tuples, where fractions of
  an item are allowed. It returns `(total_value, [(name, fraction_taken), ...])`.

### Sample input

```python
print("change for 388 cents:", make_change(388))
print("greedy with coins (4, 3, 1) for 6:", make_change(6, (4, 3, 1)))
meetings = [("standup", 9, 10), ("design", 9, 12), ("lunch", 12, 13),
            ("review", 10, 11), ("demo", 11, 13), ("retro", 13, 14)]
print("activities:", select_activities(meetings))
loot = [("gold", 10, 60), ("silver", 20, 100), ("bronze", 30, 120)]
print("fractional knapsack cap 50:", fractional_knapsack(loot, 50))
```

### Expected output

```text
change for 388 cents: {200: 1, 100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1}
greedy with coins (4, 3, 1) for 6: {4: 1, 1: 2}
activities: ['standup', 'review', 'lunch', 'retro']
fractional knapsack cap 50: (240.0, [('gold', 1.0), ('silver', 1.0), ('bronze', 0.67)])
```

### Hints

- `divmod(amount, coin)` gives you the count and the remainder in one step.
- Sort the activities by end time and keep the end time of the last activity you chose.
- Sort the knapsack items by value per unit of weight, highest first.
- Discussion: with coins (4, 3, 1), greedy gives 3 coins for 6, but two 3-coins would be better. Greedy is not always optimal.

### Acceptance checklist

- [ ] `make_change(0)` returns `{}`.
- [ ] An activity that starts exactly when the previous one ends can be chosen.
- [ ] You can explain why greedy fails for coins (4, 3, 1).

---

## T12-E10 Big-O analysis with timing

**Level:** Hard | **Time:** 30 minutes

### Problem statement

You will measure growth in two ways.

1. **Counting operations.** Write `count_sum(n)`, which uses one loop, `count_all_pairs(n)`, which
   uses nested loops over every pair, and `count_halving(n)`, which halves `n` until it reaches 1.
   Each function returns how many times its innermost step ran.
2. **Estimating the growth rate.** `growth_exponent(sizes, costs)` returns
   `log(cost_last / cost_first) / log(size_last / size_first)`. `classify(exponent)` turns that
   number into a label: below 0.5 is sub-linear, below 1.5 is about linear, below 2.5 is quadratic,
   and anything else is cubic or worse.
3. **Timing.** `time_function(func, *args, repeats=5)` returns the fastest of several
   `time.perf_counter()` runs. `membership_experiment(sizes)` times the `in` operator on a list and
   on a set, always searching for a value that is missing.

### Sample input

```python
sizes = [250, 500, 1000, 2000]
print("Operation counts (deterministic)")
print(f"{'n':>6} {'sum':>6} {'pairs':>9} {'halving':>8}")
rows = {"sum": [], "pairs": [], "halving": []}
for n in sizes:
    rows["sum"].append(count_sum(n))
    rows["pairs"].append(count_all_pairs(n))
    rows["halving"].append(count_halving(n))
    print(f"{n:>6} {rows['sum'][-1]:>6} {rows['pairs'][-1]:>9} {rows['halving'][-1]:>8}")
for name, costs in rows.items():
    k = growth_exponent(sizes, costs)
    print(f"{name}: exponent {k:.2f} -> {classify(k)}")

print()
print("Timing list vs set membership (seconds vary by machine)")
t_sizes = [10_000, 20_000, 40_000]
timings = membership_experiment(t_sizes)
for name, secs in timings.items():
    cells = "  ".join(f"{s:.6f}" for s in secs)
    print(f"{name}: {cells} -> {classify(growth_exponent(t_sizes, secs))}")
```

### Expected output

The operation-count part is identical on every machine. The timing numbers below come from one
run on the trainer VM and will differ on your machine, but the labels should be the same.

```text
Operation counts (deterministic)
     n    sum     pairs  halving
   250    250     31125        7
   500    500    124750        8
  1000   1000    499500        9
  2000   2000   1999000       10
sum: exponent 1.00 -> about linear: O(n) or O(n log n)
pairs: exponent 2.00 -> quadratic: O(n^2)
halving: exponent 0.17 -> sub-linear: O(1) or O(log n)

Timing list vs set membership (seconds vary by machine)
list: 0.009090  0.018084  0.036622 -> about linear: O(n) or O(n log n)
set: 0.000002  0.000002  0.000003 -> sub-linear: O(1) or O(log n)
```

### Hints

- If a cost grows like `n ** k`, doubling `n` multiplies the cost by `2 ** k`. The log ratio recovers `k`.
- Take the minimum of several timing runs, because background programs only ever make code slower.
- A logarithmic cost grows so slowly that its exponent is close to 0.

### Acceptance checklist

- [ ] `count_all_pairs(10) == 45` and `count_halving(1024) == 10`.
- [ ] The classification labels match the expected output.
- [ ] You can explain to a partner why a set lookup takes O(1) time on average and a list lookup takes O(n).

---

## T12-E11 Dijkstra's shortest paths (challenge)

**Level:** Hard | **Time:** 30 minutes

### Problem statement

`ROADS` is a dict of dicts that stores road distances in km:
`graph[city][neighbour] = km`. Write these functions:

- `dijkstra(graph, start)` returns `(dist, previous)`. `dist` maps every reachable city to its
  shortest distance, and `previous` stores the city you came from. Use `heapq` as the priority
  queue, and raise `ValueError` on a negative weight.
- `shortest_route(graph, start, goal)` returns `(total_km, [cities...])`, or `(None, [])` if the goal cannot be reached.

### Sample input

```python
ROADS = {
    "Amsterdam": {"Utrecht": 45, "Haarlem": 20, "Leiden": 40},
    "Haarlem": {"Amsterdam": 20, "Leiden": 30},
    "Leiden": {"Haarlem": 30, "Amsterdam": 40, "The Hague": 20, "Utrecht": 60},
    "The Hague": {"Leiden": 20, "Rotterdam": 25},
    "Utrecht": {"Amsterdam": 45, "Leiden": 60, "Rotterdam": 55},
    "Rotterdam": {"The Hague": 25, "Utrecht": 55},
}

dist, _ = dijkstra(ROADS, "Amsterdam")
for city in sorted(dist, key=dist.get):
    print(f"{city:<10} {dist[city]:>3} km")
print("route:", shortest_route(ROADS, "Amsterdam", "Rotterdam"))
print("route:", shortest_route(ROADS, "Haarlem", "Utrecht"))
print("unreachable:", shortest_route({"X": {}, "Y": {}}, "X", "Y"))
```

### Expected output

```text
Amsterdam    0 km
Haarlem     20 km
Leiden      40 km
Utrecht     45 km
The Hague   60 km
Rotterdam   85 km
route: (85, ['Amsterdam', 'Leiden', 'The Hague', 'Rotterdam'])
route: (65, ['Haarlem', 'Amsterdam', 'Utrecht'])
unreachable: (None, [])
```

### Hints

- Push `(distance, city)` tuples, so the heap always pops the closest city it has not finished yet.
- The heap can hold old entries for a city. Skip any entry whose distance is larger than the best one already known.
- Rebuild the route by following `previous` back from the goal, then reverse it.

### Acceptance checklist

- [ ] The route from Amsterdam to Rotterdam is 85 km via Leiden and The Hague.
- [ ] The start city has distance 0, and its route is just `[start]`.
- [ ] A negative weight raises `ValueError`.

---

## T12-E12 Dynamic programming: knapsack and LCS (challenge)

**Level:** Hard | **Time:** 30 minutes

### Problem statement

Write these functions:

1. `climb_stairs(n)` counts the ways to climb `n` steps when you can take 1 or 2 steps at a time. This is the warm-up.
2. `knapsack(items, capacity)` solves the 0/1 knapsack problem for `(name, weight, value)` items.
   It returns `(best_value, chosen_names)`, using a bottom-up table and then walking back through
   the table to find which items were chosen.
3. `knapsack_memo(items, capacity)` solves the same problem top-down with `functools.lru_cache`
   and returns only the best value. Pass the items as a tuple.
4. `lcs(a, b)` returns one longest common subsequence of two strings.

### Sample input

```python
print("stairs 5:", climb_stairs(5), "stairs 10:", climb_stairs(10))
gear = [("tent", 5, 60), ("stove", 3, 50), ("camera", 4, 70), ("book", 2, 30)]
print("knapsack cap 8:", knapsack(gear, 8))
print("memo version:", knapsack_memo(tuple(gear), 8))
print("lcs:", repr(lcs("ABCBDAB", "BDCABA")))
print("lcs:", repr(lcs("python", "typhoon")))
```

### Expected output

```text
stairs 5: 8 stairs 10: 89
knapsack cap 8: (120, ['stove', 'camera'])
memo version: 120
lcs: 'BCBA'
lcs: 'phon'
```

### Hints

- Knapsack: `best[i][c]` is the best value using the first `i` items with capacity `c`. For each
  item, either skip it, giving `best[i-1][c]`, or take it, giving `best[i-1][c-w] + v`.
- If `best[i][c] != best[i-1][c]`, item `i` was taken.
- LCS: when the characters match, the answer is the diagonal value plus 1. Otherwise it is the
  larger of the value above and the value to the left. Walk back from the bottom-right corner.
- Several strings can be valid answers for LCS. Your length must match, and `'BCBA'` is the one this table walk produces.

### Acceptance checklist

- [ ] `knapsack` and `knapsack_memo` agree.
- [ ] The total weight of the chosen items is never more than the capacity.
- [ ] `lcs("abc", "xyz")` returns `""`.
