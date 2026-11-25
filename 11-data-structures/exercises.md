# Topic 11: Data Structures - Exercises

Each exercise asks you to write one Python file. Use the class and function names given in the
problem statement so the trainer's tests can check your work. The sample input is a short script
that uses your code. Put it at the bottom of your file under `if __name__ == "__main__":` and run
the file. You should see exactly the expected output.

Use only the standard library. Run your file with `python3 my_file.py` on Ubuntu, or `python my_file.py` on Windows.

---

## T11-E01 Stack

**Level:** Easy | **Time:** 15 minutes

### Problem statement

A stack is last in, first out (LIFO): the last item you push is the first one you pop. Write a
class `Stack` that stores its items in a Python list, with these methods:

- `push(item)` adds an item to the top.
- `pop()` removes and returns the top item. It raises `IndexError` if the stack is empty.
- `peek()` returns the top item without removing it. It raises `IndexError` if the stack is empty.
- `is_empty()` returns `True` or `False`.
- `len(stack)` works, because you implement `__len__`.

Then write `is_balanced(text)`. It uses your `Stack` to check that every `(`, `[` and `{` in
`text` is closed by the matching bracket in the right order. Other characters are ignored.

### Sample input

```python
s = Stack()
for n in [10, 20, 30]:
    s.push(n)
print("size:", len(s))
print("peek:", s.peek())
print("pop:", s.pop())
print("size after pop:", len(s))
for text in ["(a + b) * [c]", "{[()]}", "(]", "((x)"]:
    print(f"{text!r} balanced: {is_balanced(text)}")
```

### Expected output

```text
size: 3
peek: 30
pop: 30
size after pop: 2
'(a + b) * [c]' balanced: True
'{[()]}' balanced: True
'(]' balanced: False
'((x)' balanced: False
```

### Hints

- The top of the stack is the end of the list, so `append` and `pop` are both fast.
- In `is_balanced`, push each opening bracket. When you meet a closing bracket, pop and compare.
- A dictionary such as `{")": "(", "]": "[", "}": "{"}` maps each closer to its opener.
- If the text ends while the stack still holds brackets, it is not balanced.

### Acceptance checklist

- [ ] `pop()` and `peek()` on an empty stack raise `IndexError`, not a different error.
- [ ] `is_balanced("")` is `True` and `is_balanced(")(")` is `False`.
- [ ] The output matches the expected output exactly.

---

## T11-E02 Queue from two stacks

**Level:** Easy | **Time:** 20 minutes

### Problem statement

A queue is first in, first out (FIFO). Write a class `Queue` that uses **two Python lists** as
stacks, an inbox and an outbox, instead of `list.pop(0)`. It needs these methods:

- `enqueue(item)` adds an item at the back.
- `dequeue()` removes and returns the front item. It raises `IndexError` if the queue is empty.
- `front()` returns the front item without removing it.
- `is_empty()` and `__len__`.

Also write `process_jobs(jobs)`. It puts every job into a `Queue` and returns the list of jobs
in the order they come out.

### Sample input

```python
q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print("front:", q.front())
print("dequeue:", q.dequeue())
q.enqueue("d")
print("size:", len(q))
print("remaining:", [q.dequeue() for _ in range(len(q))])
print("jobs:", process_jobs(["report.pdf", "photo.png", "notes.txt"]))
```

### Expected output

```text
front: a
dequeue: a
size: 3
remaining: ['b', 'c', 'd']
jobs: ['report.pdf', 'photo.png', 'notes.txt']
```

### Hints

- `enqueue` always appends to the inbox.
- `dequeue` pops from the outbox. If the outbox is empty, first move everything from the inbox to
  the outbox. Reversing the inbox this way puts the oldest item on top.
- Explain to a partner why each item is moved at most once.

### Acceptance checklist

- [ ] The order is correct when `enqueue` and `dequeue` calls are mixed.
- [ ] `list.pop(0)` and `collections.deque` are not used.
- [ ] `dequeue()` on an empty queue raises `IndexError`.

---

## T11-E03 Deque toolbox

**Level:** Easy | **Time:** 15 minutes

### Problem statement

Use `collections.deque` to write three small tools:

1. `is_palindrome(text)` ignores case and every character that is not a letter or a digit. It
   compares characters from both ends with `popleft()` and `pop()`.
2. `rotate_list(items, k)` returns a new list rotated `k` places to the right. A negative `k`
   rotates to the left.
3. A class `RecentItems(limit)` with `add(item)` and `latest_first()`. It keeps only the last
   `limit` items, for example a browser's recently visited pages.

### Sample input

```python
for text in ["Racecar", "Never odd or even", "Python"]:
    print(f"{text!r} palindrome: {is_palindrome(text)}")
print("rotate right 2:", rotate_list([1, 2, 3, 4, 5], 2))
print("rotate left 1:", rotate_list([1, 2, 3, 4, 5], -1))
recent = RecentItems(3)
for page in ["home", "about", "blog", "contact", "shop"]:
    recent.add(page)
print("recent pages:", recent.latest_first())
```

### Expected output

```text
'Racecar' palindrome: True
'Never odd or even' palindrome: True
'Python' palindrome: False
rotate right 2: [4, 5, 1, 2, 3]
rotate left 1: [2, 3, 4, 5, 1]
recent pages: ['shop', 'contact', 'blog']
```

### Hints

- `deque(maxlen=3)` drops the oldest item automatically when a fourth one is appended.
- `deque.rotate(k)` already does the rotation.
- `str.isalnum()` tells you whether a character is a letter or a digit.

### Acceptance checklist

- [ ] `is_palindrome("A man, a plan, a canal: Panama")` is `True`.
- [ ] `rotate_list` does not change the list that was passed in.
- [ ] `RecentItems` never holds more than `limit` items.

---

## T11-E04 Singly linked list

**Level:** Medium | **Time:** 25 minutes

### Problem statement

Write a class `Node` with `value` and `next`, and a class `LinkedList` that keeps a `head`. The
constructor takes an optional sequence of starting values. Implement these methods:

- `append(value)` adds at the end and `prepend(value)` adds at the front.
- `find(value)` returns the index of the first match, or `-1`.
- `remove(value)` removes the first match and returns `True`, or returns `False` if there is no match.
- `reverse()` reverses the list in place, without building a new list.
- `__iter__`, `__len__`, and `__str__`. `__str__` prints `1 -> 2 -> 3`, or `(empty)` for an empty list.

### Sample input

```python
ll = LinkedList([3, 5, 7])
ll.prepend(1)
ll.append(9)
print("list:", ll)
print("length:", len(ll))
print("find 7:", ll.find(7))
print("find 4:", ll.find(4))
print("remove 5:", ll.remove(5))
print("after remove:", ll)
ll.reverse()
print("reversed:", ll)
```

### Expected output

```text
list: 1 -> 3 -> 5 -> 7 -> 9
length: 5
find 7: 3
find 4: -1
remove 5: True
after remove: 1 -> 3 -> 7 -> 9
reversed: 9 -> 7 -> 3 -> 1
```

### Hints

- Keep a `_size` counter so `len()` does not have to walk the list.
- When you remove a node, track the previous node as well as the current one. Removing the head is a special case.
- To reverse, walk the list once and point each node's `next` back at the previous node.
- Once `__iter__` works, `find` and `__str__` become one-liners.

### Acceptance checklist

- [ ] Removing the head, a middle node and the last node all work.
- [ ] `reverse()` works on an empty list and on a one-item list.
- [ ] No Python list is used to store the nodes.

---

## T11-E05 Doubly linked list

**Level:** Medium | **Time:** 25 minutes

### Problem statement

Write a class `DoublyLinkedList` whose nodes have `prev` and `next` links. Keep both `head` and
`tail`. Implement `push_front`, `push_back`, `pop_front`, `pop_back`, `remove(value)`, `to_list()`,
`to_list_reversed()` and `__len__`. The two pop methods raise `IndexError` when the list is empty.
Each operation at either end must take constant time.

### Sample input

```python
dll = DoublyLinkedList()
for v in ["b", "c", "d"]:
    dll.push_back(v)
dll.push_front("a")
print("forward:", dll.to_list())
print("backward:", dll.to_list_reversed())
print("pop_front:", dll.pop_front())
print("pop_back:", dll.pop_back())
print("remove 'c':", dll.remove("c"))
print("now:", dll.to_list(), "length", len(dll))
```

### Expected output

```text
forward: ['a', 'b', 'c', 'd']
backward: ['d', 'c', 'b', 'a']
pop_front: a
pop_back: d
remove 'c': True
now: ['b'] length 1
```

### Hints

- Write one helper, `_unlink(node)`, that fixes the neighbours' links and `head` and `tail`. Then
  `pop_front`, `pop_back` and `remove` can all call it.
- `to_list_reversed()` should walk the `prev` links from `tail`. It must not reverse the output of `to_list()`.
- Draw the boxes and arrows on paper before you code the special cases.

### Acceptance checklist

- [ ] After removing the last remaining item, both `head` and `tail` are `None`.
- [ ] `to_list_reversed()` uses the `prev` links.
- [ ] Popping from an empty list raises `IndexError`.

---

## T11-E06 Hash map from scratch

**Level:** Medium | **Time:** 30 minutes

### Problem statement

Write a class `HashMap` without using a `dict` for storage. Use a list of buckets, where each
bucket is a list of `(key, value)` pairs (separate chaining). Implement these methods:

- `put(key, value)` inserts a new pair or replaces the value of an existing key.
- `get(key, default=None)` returns the value, or `default` if the key is missing.
- `remove(key)` returns `True` if the key was removed and `False` otherwise.
- `keys()`, `capacity()`, `__contains__` and `__len__`.

When `size / capacity` goes above 0.75, double the number of buckets and re-insert every pair.
Finally, write `word_count(text)`. It counts words with your `HashMap` and returns an ordinary
dict sorted by word.

### Sample input

```python
m = HashMap(capacity=4)
m.put("apple", 3)
m.put("pear", 5)
m.put("apple", 4)
print("apple:", m.get("apple"))
print("missing:", m.get("kiwi", "not found"))
print("'pear' in map:", "pear" in m)
for i, fruit in enumerate(["fig", "lime", "plum", "date"]):
    m.put(fruit, i)
print("size:", len(m), "capacity:", m.capacity())
print("remove pear:", m.remove("pear"), "size:", len(m))
print("word count:", word_count("the cat and the hat and the bat"))
```

### Expected output

```text
apple: 4
missing: not found
'pear' in map: True
size: 6 capacity: 8
remove pear: True size: 5
word count: {'and': 2, 'bat': 1, 'cat': 1, 'hat': 1, 'the': 3}
```

### Hints

- The bucket for a key is `hash(key) % len(self._buckets)`.
- Updating an existing key must not increase the size.
- When you resize, rebuild the buckets and call `put` for every old pair.

### Acceptance checklist

- [ ] Replacing an existing key leaves `len()` unchanged.
- [ ] The capacity doubles once the load factor goes above 0.75.
- [ ] No `dict` or `set` is used inside `HashMap`. `word_count` may return a dict.

---

## T11-E07 Binary tree traversals

**Level:** Medium | **Time:** 25 minutes

### Problem statement

Use a `TreeNode(value, left=None, right=None)` class and write these functions:

- `preorder(node)`, `inorder(node)` and `postorder(node)`, each written recursively.
- `level_order(root)`, which visits the tree level by level using a queue.
- `height(node)`. An empty tree has height 0 and a single node has height 1.
- `count_leaves(node)`.

Write `sample_tree()` that builds this tree:

```text
       A
     /   \
    B     C
   / \     \
  D   E     F
```

### Sample input

```python
root = sample_tree()
print("preorder:   ", preorder(root))
print("inorder:    ", inorder(root))
print("postorder:  ", postorder(root))
print("level order:", level_order(root))
print("height:", height(root))
print("leaves:", count_leaves(root))
```

### Expected output

```text
preorder:    ['A', 'B', 'D', 'E', 'C', 'F']
inorder:     ['D', 'B', 'E', 'A', 'C', 'F']
postorder:   ['D', 'E', 'B', 'F', 'C', 'A']
level order: ['A', 'B', 'C', 'D', 'E', 'F']
height: 3
leaves: 3
```

### Hints

- Every recursive function starts with the same base case: `if node is None`.
- Preorder visits the node, then the left subtree, then the right. Inorder visits left, node, right. Postorder visits left, right, node.
- For level order, use `collections.deque` and `popleft()`.

### Acceptance checklist

- [ ] All four traversals match the expected output.
- [ ] `height(None)` is 0 and `level_order(None)` is `[]`.
- [ ] `level_order` uses a queue, not recursion.

---

## T11-E08 Binary search tree

**Level:** Medium | **Time:** 30 minutes

### Problem statement

Write a class `BST` that stores unique, comparable keys. The constructor takes optional starting
keys. Implement these methods:

- `insert(key)` returns `False` when the key is a duplicate.
- `contains(key)`, `min()` and `max()`.
- `delete(key)` returns `True` if the key was deleted. It must handle a node with no children,
  one child or two children.
- `inorder()` returns the keys in sorted order.
- `__len__`.

### Sample input

```python
tree = BST([50, 30, 70, 20, 40, 60, 80, 30])
print("sorted:", tree.inorder())
print("size:", len(tree))
print("contains 60:", tree.contains(60))
print("contains 65:", tree.contains(65))
print("min:", tree.min(), "max:", tree.max())
print("delete 30:", tree.delete(30))
print("delete 99:", tree.delete(99))
print("after delete:", tree.inorder())
```

### Expected output

```text
sorted: [20, 30, 40, 50, 60, 70, 80]
size: 7
contains 60: True
contains 65: False
min: 20 max: 80
delete 30: True
delete 99: False
after delete: [20, 40, 50, 60, 70, 80]
```

### Hints

- Smaller keys go left and larger keys go right.
- To delete a node with two children, copy its in-order successor (the smallest key in its right
  subtree) into it, then delete the successor from the right subtree.
- A recursive `_delete(node, key)` that returns the new root of each subtree keeps the code short.

### Acceptance checklist

- [ ] Inserting a duplicate does not change the size.
- [ ] Deleting a leaf, a node with one child and a node with two children all leave `inorder()` sorted.
- [ ] Deleting a missing key returns `False`.

---

## T11-E09 Heaps and priority queues with heapq

**Level:** Medium | **Time:** 20 minutes

### Problem statement

Use the `heapq` module to write these tools:

1. `k_smallest(numbers, k)` uses `heapify` and `heappop`.
2. `k_largest(numbers, k)` keeps a min-heap of size `k` while it scans the numbers. It returns
   the result in descending order.
3. Use `heapq.merge` to merge several sorted lists.
4. A class `TaskQueue` with `add(task, priority)`, `pop()` and `__len__`. `pop()` returns a
   `(task, priority)` pair. The lowest priority number comes out first, and tasks with the same
   priority come out in the order they were added.

### Sample input

```python
data = [42, 7, 19, 3, 88, 25, 61, 3]
print("3 smallest:", k_smallest(data, 3))
print("3 largest:", k_largest(data, 3))
print("merged:", list(heapq.merge([1, 4, 9], [2, 3, 10], [5])))
tq = TaskQueue()
tq.add("write report", 2)
tq.add("fix outage", 0)
tq.add("reply to email", 3)
tq.add("review PR", 2)
while len(tq):
    task, priority = tq.pop()
    print(f"run [{priority}] {task}")
```

### Expected output

```text
3 smallest: [3, 3, 7]
3 largest: [88, 61, 42]
merged: [1, 2, 3, 4, 5, 9, 10]
run [0] fix outage
run [2] write report
run [2] review PR
run [3] reply to email
```

### Hints

- `heapq` always gives you a min-heap, so `heap[0]` is the smallest item.
- In `k_largest`, replace the root with `heapreplace` when a bigger number arrives.
- Store `(priority, counter, task)` tuples. The counter, from `itertools.count()`, breaks ties
  in insertion order and stops Python from ever comparing two tasks.

### Acceptance checklist

- [ ] `k_smallest` with a `k` larger than the list returns the whole list, sorted.
- [ ] Tasks with equal priority come out first in, first out.
- [ ] `pop()` on an empty `TaskQueue` raises `IndexError`.

---

## T11-E10 Graph with an adjacency list

**Level:** Medium | **Time:** 25 minutes

### Problem statement

Write a class `Graph` for an undirected graph, stored as a dict that maps each vertex to a set of
neighbours. Implement these methods:

- `add_vertex(v)` and `add_edge(a, b)`. `add_edge` creates any missing vertex.
- `neighbours(v)` returns the neighbours as a sorted list. `degree(v)` returns how many there are.
- `edge_count()`.
- `has_path(start, goal)`, written with breadth-first search.
- `components()` returns the connected groups, each one a sorted list.

### Sample input

```python
g = Graph()
for a, b in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("E", "F")]:
    g.add_edge(a, b)
g.add_vertex("G")
print("neighbours of A:", g.neighbours("A"))
print("degree of D:", g.degree("D"))
print("edges:", g.edge_count())
print("path A->D:", g.has_path("A", "D"))
print("path A->F:", g.has_path("A", "F"))
print("components:", g.components())
```

### Expected output

```text
neighbours of A: ['B', 'C']
degree of D: 2
edges: 5
path A->D: True
path A->F: False
components: [['A', 'B', 'C', 'D'], ['E', 'F'], ['G']]
```

### Hints

- In an undirected graph, `add_edge(a, b)` adds `b` to `a`'s set and `a` to `b`'s set.
- Each edge is stored twice, so `edge_count()` is the sum of all degrees divided by 2.
- For `components()`, start a search from every vertex you have not seen yet. Each search finds one component.

### Acceptance checklist

- [ ] A vertex with no edges forms its own component.
- [ ] `has_path` returns `False` for unknown vertices instead of crashing.
- [ ] `components()` returns the same result on every run (sort it).

---

## T11-E11 Trie (challenge)

**Level:** Hard | **Time:** 30 minutes

### Problem statement

Write a class `Trie`, also called a prefix tree, for lowercase words. Implement these methods:

- `insert(word)`. Inserting a duplicate changes nothing.
- `search(word)` is `True` only for complete words.
- `starts_with(prefix)` is `True` when some stored word begins with the prefix.
- `count_prefix(prefix)` returns how many stored words begin with the prefix.
- `words_with_prefix(prefix)` returns the matching words in alphabetical order.
- `delete(word)` returns `True` if the word was removed, and also removes branches that no other
  word uses.

### Sample input

```python
t = Trie(["car", "card", "care", "cart", "cat", "dog", "do"])
print("search 'car':", t.search("car"))
print("search 'ca':", t.search("ca"))
print("starts_with 'ca':", t.starts_with("ca"))
print("count 'car':", t.count_prefix("car"))
print("words 'car':", t.words_with_prefix("car"))
print("words 'do':", t.words_with_prefix("do"))
print("delete 'card':", t.delete("card"))
print("words 'car':", t.words_with_prefix("car"))
```

### Expected output

```text
search 'car': True
search 'ca': False
starts_with 'ca': True
count 'car': 4
words 'car': ['car', 'card', 'care', 'cart']
words 'do': ['do', 'dog']
delete 'card': True
words 'car': ['car', 'care', 'cart']
```

### Hints

- Each node holds a `children` dict, an `is_word` flag, and a `pass_count` of how many words go
  through it. With the count, `count_prefix` takes time proportional to the prefix length.
- Collect the words with a recursive helper that visits the children in sorted order.
- When you delete, lower the `pass_count` along the path. As soon as a child's count reaches 0,
  remove that child and stop.

### Acceptance checklist

- [ ] `search("ca")` is `False` while `starts_with("ca")` is `True`.
- [ ] Inserting a duplicate word does not change `count_prefix`.
- [ ] Deleting a word that is a prefix of another word, such as `do` and `dog`, keeps the longer word.

---

## T11-E12 LRU cache (challenge)

**Level:** Hard | **Time:** 30 minutes

### Problem statement

Write a class `LRUCache(capacity)` that keeps at most `capacity` entries. When it is full, it
evicts the least recently used entry. You must not use `OrderedDict` or `functools.lru_cache`.
Combine a dict, which maps each key to a node, with your own doubly linked list, which keeps the
usage order. Implement these methods:

- `get(key, default=None)` marks the entry as most recently used and counts a hit or a miss.
- `put(key, value)` inserts or updates an entry. It returns the evicted key, or `None`.
- `keys()` returns the keys from most to least recently used.
- `__len__`, plus the attributes `hits` and `misses`.

A capacity below 1 raises `ValueError`.

### Sample input

```python
cache = LRUCache(3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print("order:", cache.keys())
print("get a:", cache.get("a"))
print("order:", cache.keys())
print("put d evicts:", cache.put("d", 4))
print("get b:", cache.get("b"))
print("order:", cache.keys())
print("hits:", cache.hits, "misses:", cache.misses)
```

### Expected output

```text
order: ['c', 'b', 'a']
get a: 1
order: ['a', 'c', 'b']
put d evicts: b
get b: None
order: ['d', 'a', 'c']
hits: 1 misses: 1
```

### Hints

- Two sentinel nodes, `head` and `tail`, mean you never have to test for an empty list.
- Most recently used goes just after `head`, so the eviction candidate is always `tail.prev`.
- Both `get` and `put` must run in constant time. No loop over the entries is allowed.

### Acceptance checklist

- [ ] Updating an existing key moves it to the front and evicts nothing.
- [ ] `hits` and `misses` are counted correctly.
- [ ] `get` and `put` contain no loops.
