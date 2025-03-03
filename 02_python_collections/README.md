#### 0. Miscellaneous

```python
# To iterate over char 'a' to 'z' in python
for i in range(ord('a'), ord('z') + 1):
    letter = chr(i)
    print(letter)
```

#### 1. Overview of Python Collections

- **Built-in Collection Types**
  - **Lists**: mutable sequences
  - **Tuples**: immutable sequences
  - **Sets**: unordered unique elements
  - **Dictionaries**: key-value pairs
- **Collections Module**
  - Specialized container datatypes

#### 2. List Operations

```python
# List Creation
lst = []  # Empty list
lst = [1, 2, 3]  # With elements

# Core Operations
lst.append(element)      # Add to end
lst.insert(index, element)  # Insert at index
lst[index]              # Access element
lst.pop(index)          # Remove by index
lst.remove(element)     # Remove by value
lst.index(val, optional_start_search_from_index, optional_end_search_till_index)

# Utility Operations
lst.extend(iterable)    # Bulk add
element in lst         # Check existence
len(lst)              # Get length
lst.clear()           # Remove all
```

#### 3. Tuple Operations

```python
# Tuple Creation
tup = ()               # Empty tuple
tup = (1, 2, 3)       # With elements
tup = 1,              # Single element

# Operations
len(tup)              # Get length
tup[index]            # Access element
tup.count(element)    # Count occurrences
tup.index(element)    # Find position
```

#### 4. Set Operations

```python
# Set Creation
s = set()             # Empty set
s = {1, 2, 3}        # With elements

# Core Operations
s.add(element)        # Add element
s.remove(element)     # Remove (raises error)
s.discard(element)    # Remove (no error)

# Set Operations
s1 | s2               # Union
s1 & s2               # Intersection
s1 - s2               # Difference
s1 ^ s2               # Symmetric difference
```

#### 5. Dictionary Operations

```python
# Dictionary Creation
d = {}                # Empty dict
d = {'key': 'value'}  # With elements

# Core Operations
d[key] = value        # Add/Update
d.get(key, default)   # Safe retrieval
d.pop(key)           # Remove and return
del d[key]           # Remove entry

# Additional Operations
d.update(other_dict)  # Merge dictionaries
key in d             # Check key existence
d.keys()             # Get keys view
d.values()           # Get values view
d.items()            # Get key-value pairs
```

#### 6. Collections Module Specialties

```python
from collections import defaultdict, Counter, deque, OrderedDict

# defaultdict
d = defaultdict(list)  # Auto-creates list for missing keys

# Counter
c = Counter(['a', 'b', 'a'])  # Count elements

# deque (double-ended queue)
q = deque()
q.append(x)           # Add to right
q.appendleft(x)       # Add to left
q.pop()              # Remove from right
q.popleft()          # Remove from left

# OrderedDict
od = OrderedDict()    # Remembers insertion order
```

#### 7. List Comprehensions

```python
# List comprehension
[x for x in range(10)]
[x for x in range(10) if x % 2 == 0]

# Dict comprehension
{x: x**2 for x in range(5)}

# Set comprehension
{x for x in range(10)}
```

#### 8. Best Practices

- Use **list** for ordered, mutable sequences
- Use **tuple** for immutable sequences
- Use **set** for unique elements
- Use **dict** for key-value mappings
- Use **collections module** for specialized needs
- Prefer **list comprehensions** over loops when appropriate
- Use `in` operator for **membership testing**

#### 9. Built-in Functions

```python
# Sorting
sorted(iterable)      # Return new sorted list
sorted(iterable, key=func)  # Sort with key function

# Other Operations
len(collection)       # Get size
max(collection)       # Find maximum
min(collection)       # Find minimum
sum(collection)       # Sum numbers
any(collection)       # True if any true
all(collection)       # True if all true
```

#### 10. Heap Operations using heapq

```python
import heapq

# Creating a heap
heap = []
heapq.heapify(heap)    # Convert list to heap in-place O(n)

# Core Operations
heapq.heappush(heap, item)    # Add element - O(log n)
heapq.heappop(heap)           # Remove & return smallest - O(log n)

# Max Heap Simulation (multiply by -1)
max_heap = []
heapq.heappush(max_heap, -item)  # For max heap
largest = -heapq.heappop(max_heap)
```

#### 11. Frequency counting using Counter

```python
from collections import Counter

# Creating a Counter
counter = Counter()           # Empty counter
counter = Counter(['a', 'b', 'a'])  # From iterable
counter = Counter('hello')    # From string

# usage
char_count = Counter('hello')

for ch, freq in char_count.items():
  ...

```
