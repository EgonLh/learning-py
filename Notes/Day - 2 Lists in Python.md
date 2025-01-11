> A list is a collection of items in a particular order
- make the name of the list plural such as `letters` , `digits` , `names`
- `[]` indicate a `list` , `individual` elements in the list are separated by `commas`
```python
names = ['A' , 'B' , 'C' , 'D' ]
print(names)
```

##### **Accessing Elements in a list**
- list are `ordered collections`
- by using the `position` (index) of the item `desired`
```python
nums = ["one","two","three","four","five"]
print(type(nums[0]));
print(nums[0].title());
```

> start at `0`
- In order to obtain the `last` element, python use the special syntax `-1` which will return the last item

```python
print(nums[-1]) ##"five"
```

- Useful to access the `last` item in a list without knowing exactly how long the list is. 
- `-2` return the second item from the end of the list , as son `-3`

-----
##### Using `Individual` Values from a list

```python
print("Bro has " + nums[-1].title() + " pens.")
```


###### `Manipulating` Elements in List

>Most lists will be `dynamic`
- build a `list` , then `add` and `remove` elements from it as your program `runs`.

>Modifying Elements in A list
- similar to the syntax for accessing an element in a list
```python
nums[-1] = "six";
print(nums)
```

###### Adding Elements to a list

- `Appending` Elements to the end of the `list`
- Simplest way to add a new element to a `list`  - to `append` the item to the list and added to the `end` of the list.
```python
nums2 = nums;

nums.append("five")
print("origin:",nums)
print("reference: ",nums2)
##origin: ['one', 'two', 'three', 'four', 'six', 'five']
##reference:  ['one', 'two', 'three', 'four', 'six', 'five']
```
>Solution for `deep copy`
```python
# Solution
nums3 = nums.copy();
nums.append("seven");
print(">.Copy():", nums3);
print(">Origin :", nums)
```

- `append( )` method make it easy to build lists dynamically
---
###### Inserting `Elements` into a list
- Can add a new `element` at any position in list by using `insert()` method.
```python
# inserting

ages = [1,2,3,5];

ages.insert(-1,4);

print("Insert :",ages)
##Insert : [1, 2, 3, 4, 5]
```

---
###### Removing Elements from a list
- can remove a item according to its position in the list or according to its `value`.
> Using `del` statement
- can use for the whole list
- can also used for the element in the list with its index code as follow:
```python
ages.append("five")
print("Original :",ages)
del ages[0]
print("New Age after del [0] :",new_ages)
```

- no longer access the value that was removed from the list after the del statement is used.

> Removing an item using the `pop()`
- usable the `removed value` from a list, this `method` can used 
- pop method remove the `last` item in a list but let the programmer work with that item after removing it.
- `pop()` comes from thinking of a `list` as a stack of items and popping one item off the top of the stack.
```python
datas = [10,203,402,300];
print("Original :",datas)
removed_data = datas.pop();
print("Removed List : ",datas)
print("Removed : ",removed_data)
```

>Popping items from any position in a list

- use `pop(index)`
- once removed the item with pop(), there is no longer stored in the list

```python
first_data  = datas.pop(0);
print("First Data :"+str(first_data))
print("The origin :",datas)
```

`Usage` : 
- to delete an item from a list and not use that item in any way, use the del statement
- to use an item as you remove it, use the pop() method

> Removing an item by value

- `Remove()` method to remove with the element by using `values`

> [!NOTE]
> `remove` method deletes only the first occurrence of the value , for the value which is more than once in the list, use a loop to determine all occurrences of the value .
> 

```python
books = ["A" ,"B" , "C" , "D" ,"A" , " D"];
books.remove("B");
print("Books :",books);
```

##### Organizing a list
- lists will be created in an `unpredictable` order
- make it into `particular` order
- provides a number of different ways to `organize` your lists, depending on the situation.

- Python `sort()` method makes it relatively easy to sort a list
- Changes the `order` of the list `permanently`
- Sort this list in `reverse` alphabetical order by passing the argument `reverse=True` to the `sort()` method

```python
books.sort(reverse=True)
print("Permanently, Reverse",books)
```
---
###### Temporality sort()

	used sorted() function with parameters lists

- `code` as follow:

```python
# temp sorted
names = ["aung","maung" , "kyaw"]
print("sorted() :",sorted(names,reverse=True))
print("Original :",names)
```

> [!NOTE]
> Alphabetically sort is more `compilated` when all values are not in a `lowercase`, should interpret capital letters when to sort order

- Printing a list in reverse order
- use `reverse()` method
- change the order of the list `permanently`, can bring back to original by using it again
```python
names.reverse()
print("Reverse" ,names );
names.reverse()
print("Origin :",names)
```

- Finding the `lenght of a list`
- Use `len()` function 
```python
print(len(names))## 3
```

> [!NOTE]
> `Python` counts the items in a list starting with one, so you shouldn’t run into any off-by-one errors when determining the length of a list.


##### Avoiding Index errors when working with lists

> index `errors` (which is out of range)

- because of `off-by-one` nature of indexing in lists
- determine the last item as `-1`

>The index -1 always returns the last item in a list
---
