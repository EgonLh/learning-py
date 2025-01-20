> How to Loop through an `Entire` list

##### For `Loops`
- Tells Python to pull a name from the `list` , and store it in the variable
```python
nums = [1,2,3,5];
for num in nums:
    print("Num :",num)
```

- Using `singular` and `plural` names can help you identify whether a section of code is working with a single element from the list or the entire list.


>Python uses `indentation` to determine when one line of code is `connected` to the line above it

- `Blocks of code` indented at a few different levels

```python
for num in range(1,10):
print("Num :",num) ##> error here
```

- Take care of common `errors` such as forgetting `comma`, `indentation` and `logic` `error`
---
##### Making Numerical `List`
- `Reasons` exist to store a set of numbers
- `Lists` are ideal for storing sets of `numbers`, and Python provides a number of tools to help you work `efficiently` with `lists of numbers`.

> range() > provide a series of number

- offer `off-by-one` behavior
- eg `range(1,5)` -> `1,2,3,4`
- Start counting at the first `value` you give it, and it stops when it reaches the `second` value you provide

>Using `range` to make a list of `number`

- wrapped with `list()` as type `casting`
```python
list_from_range = list(range(0,7));
print(list_from_range)

squares = [];
for value in range(1,11):
    square = value**2
    squares.append(square)
```

> [!NOTE]
> Using a `temporary` variable makes your code easier to read; other times it makes the code unnecessarily long. Focus first on writing code that you understand clearly, which does what you want it to do. Then look for more `efficient` approaches as you review your `code`.

##### Simple `Statistics` with a list of number

- `max` , `min` , `sum`  > supported from `python`
```python
print(min(squares))
print(max(squares))
print(sum(squares))
```
#### List `Comprehensions`

>The approach described for generating the list `squares` consisted of using three or four lines of code

- Allows you to `generate` this same `list` in just one line of `code`
- combines the `for loop` and the creation of new elements into one line, and automatically `appends` each new element
```python
l_com  = [value**2 for value in range(1,6)]
print("List comprehensive :",l_com)
```
- open a set of square `brackets` and define the `expression` for the values you want to store in the new `list`
- Write a for `loop` to generate the numbers you want to feed into the `expression`, and close the square `brackets`
- takes practice to write your own list `comprehensions`
---
#### Working with Part of a `list`
>how to access single elements in a `list`

##### Slicing a `list`
```python
players = ['egon','loth','florence','elly']
print(players[:3])
print(players[2:3])
print(players[1:])
print(players[:])
print(players[3:])
```
- For the last three players , we can use the slice `players[-3:]`
```python
# start from -1 position to start
print(players[:-1])
# start end to -1
print(players[-1:])
```
---
#### Looing Through a  Slice
- Python `loops` through only the first two `names`
```python
for player in players[:2]:
    print("Name: "+player.title())
```
- `Slices` are very useful in a number of `situations`
##### Copying a `list`
- Start with an existing `list` and make an entirely new `list` based on the `first` one
- Can make a slice that includes the entire `original` list by omitting the first index and the second index ([:])
```python
nums = [1,2,3,4,5]
nums_copy = nums;
nums_copy_2 = nums[:]
print(nums)
print(nums_copy)
nums.append(1)
nums.pop(0)
nums.remove(4)
del nums
print("After Append",nums_copy)
# deep copy
print("with nums[:] ", nums_copy_2)
```
- by using that syntax , obtain `separated` copy >two separate `lists`.
```python
nums_copy = nums;
```
- Syntax actually tells Python to connect the new variable  to the list that is already contained in the `original` list, so now both `variables` point to the same list.

>Example `code`
```python
foods=  ['coffee','tea','burger','coke'];
# my_fav_foods = foods.copy();
my_fav_foods = foods[:];
ava_foods = foods;
print("Foods :",foods)
print("My Fav Foods :",my_fav_foods)
print("Foods :",ava_foods)
print("Add Foods")
foods.append('juices')
print("Foods :",foods)
print("My Fav Foods :",my_fav_foods)
print("Foods :",ava_foods)
```

----
#### `Tuple`
>`Lists` work well for storing sets of items that can change throughout the life of a program
- The ability to modify `lists` is particularly important
- to create a list of items that `cannot` change. `Tuples` allow you to do just that
- an `immutable` list is called a `tuple`
##### Defining a `Tuple`
- A `tuple` looks just like a list except you use `parentheses` instead of `square brackets`
```python
_tuple = 10,20
print(_tuple)
_tuple = (1,2)
print(_tuple)
```
- use `square brackets` to access it individual element
- can't update `tuple`, `immutable`
```python
_tuple[0] = 1; #> error
```
- This is `beneficial` because we want Python to raise an error when a line of code tries to change the element of the `tuple`.
- overwriting a `variable`, (`tuple`) is valid.

> [!NOTE]
> When compared with `lists`, `tuples` are simple data structures. Use them when you want to store a set of values that should not be changed throughout the life of a program.

---
#### Styling `Code`
- Make `code` as easy as possible to read
- `easy-to-read` code helps you keep track of what your `programs` are doing and helps others `understand` your code as well.

>`Guild` - Python Enhancement Proposal (PEP)

> [!NOTE]
> The Python style guide was written with the understanding that `code` is read more often than it is written. You’ll write your code once and then start reading it as you begin debugging. When you add `features` to a program, you’ll spend more time reading your code. When you share your code with other `programmers`, they’ll read your code as well.


>`Indentation`
- `PEP 8` recommends that you use `four` spaces per indentation level
- Using `four spaces` improves readability while leaving room for multiple levels of `indentation` on each line.
- The Python `interpreter` gets confused when `tabs` are mixed with spaces
- Mixing `tabs` and `spaces` in your file can cause problems that are very `difficult` to `diagnose`.
>`Line Length`

> [!NOTE]
> `PEP 8` also recommends that you limit all of your comments to` 72 characters` per line, because some of the tools that generate `automatic` documentation for larger projects add formatting characters at the beginning of each commented line.

>`Blank Lines`

- To group parts of your program `visually`, use `blank lines`
- Blank lines won’t affect how your code runs, but they will affect the `readability` of `code`. The Python interpreter `uses` horizontal `indentation` to interpret the meaning of your code, but it `disregards` vertical `spacing`.
[Styling Guide](https://peps.python.org/pep-0001/)
----

