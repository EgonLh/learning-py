# Python Data Structures Overview

| **Data Structure** | **Type**        | **Mutability** | **Memory Storage**                                                                                |
| ------------------ | --------------- | -------------- | ------------------------------------------------------------------------------------------------- |
| **int**            | Numeric         | Immutable      | Stored as a fixed-size object. Python caches small integers (-5 to 256) to optimize memory usage. |
| **float**          | Numeric         | Immutable      | Stored as a floating-point object. Size depends on implementation (typically 64-bit IEEE 754).    |
| **complex**        | Numeric         | Immutable      | Stored as a pair of floats (real and imaginary parts).                                            |
| **str**            | Sequence        | Immutable      | Stored as an array of Unicode characters. Small strings may be interned for memory optimization.  |
| **list**           | Sequence        | Mutable        | Dynamic array stored as a contiguous block of memory. Can grow by reallocating larger blocks.     |
| **tuple**          | Sequence        | Immutable      | Stored as a fixed-size array of pointers to its elements.                                         |
| **dict**           | Mapping         | Mutable        | Hash table with dynamic resizing. Stores key-value pairs.                                         |
| **set**            | Set             | Mutable        | Hash table for fast membership testing. Internally resizes to optimize memory usage.              |
| **frozenset**      | Set             | Immutable      | Similar to `set` but immutable and hashable.                                                      |
| **bytes**          | Binary Sequence | Immutable      | Stores a sequence of bytes in a contiguous memory block.                                          |
| **bytearray**      | Binary Sequence | Mutable        | Similar to `bytes`, but allows modification of its contents.                                      |
| **range**          | Sequence        | Immutable      | Stores start, stop, and step as integers. Values are generated on demand (lazy evaluation).       |
| **bool**           | Boolean         | Immutable      | Subclass of `int`. Values (`True`, `False`) are singleton instances, sharing the same memory.     |

### Notes:
1. **Immutable** structures (like `int`, `tuple`, and `str`) cannot be changed after creation. Any modification results in a new object being created.
2. **Mutable** structures (like `list` and `dict`) allow in-place modifications, which can save memory and execution time for certain operations.
3. Python uses **reference counting** and a **garbage collector** to manage memory. Small, frequently used objects may be cached to optimize performance.


----
### Example Codes
```python
# int
x = 42  # Immutable
y = x + 1
print(x, y)  # 42 43

# float
pi = 3.14159  # Immutable
approx_pi = round(pi, 2)
print(pi, approx_pi)  # 3.14159 3.14

# complex
z = 3 + 4j  # Immutable
z_conjugate = z.conjugate()
print(z, z_conjugate)  # (3+4j) (3-4j)

# str
s = "hello"  # Immutable
s_upper = s.upper()
print(s, s_upper)  # hello HELLO

# list
lst = [1, 2, 3]  # Mutable
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# tuple
tpl = (1, 2, 3)  # Immutable
tpl_extended = tpl + (4,)
print(tpl, tpl_extended)  # (1, 2, 3) (1, 2, 3, 4)

# dict
d = {"a": 1, "b": 2}  # Mutable
d["c"] = 3
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# set
s = {1, 2, 3}  # Mutable
s.add(4)
print(s)  # {1, 2, 3, 4}

# frozenset
fs = frozenset([1, 2, 3])  # Immutable
print(fs)  # frozenset({1, 2, 3})

# bytes
b = b"hello"  # Immutable
b_upper = b.upper()
print(b, b_upper)  # b'hello' b'HELLO'

# bytearray
ba = bytearray(b"hello")  # Mutable
ba[0] = ord("H")
print(ba)  # bytearray(b'Hello')

# range
r = range(1, 10, 2)  # Immutable
for num in r:
    print(num, end=" ")  # 1 3 5 7 9

# bool
flag = True  # Immutable
neg_flag = not flag
print(flag, neg_flag)  # True False

```
----
