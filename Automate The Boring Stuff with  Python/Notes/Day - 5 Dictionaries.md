`A dictionary in Python is a collection of key-value pairs`
- A `dictionary` is wrapped in braces, `{}`, with a series of `key-value` pairs inside the `braces`, as shown in the earlier example:
```python
dict_py = {"one" : 1,"two" : 2 ,"three" :"Four"};
```
- Accessing `Values`
```
To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets
```

```python
print(dict_py['three'])
```

- can have an `unlimited` number of` key-value` pairs in a `dictionary`
----
#### Adding New `Keys` and `Values`

Dictionaries are `dynamic` structures, and you can add new `key-value` pairs to a `dictionary` at any time
- doesn't care about the `order` of the keys, but the `values` are ordered, and can be accessed by the keys
- care the `connection` between the keys and values
Use empty `dictionaries` when storing `user-supplied` data in a `dictionary` or when you write `code` that generates a large number of `key-value` pairs `automatically`.

----
#### Modifying `Values` in a Dictionary

- To modify a `value` in a `dictionary`, give the name of the `dictionary` with the key in square brackets and then the new value you want associated with that key.
```python
dict_py['three'] = 3;
print("The Mutated One :",dict_py)
```

- used with `if-elif-else` block to modify value in `key-valu`e pair

----
#### Removing `Key-Value` Pairs

`del` statement to completely remove a `key-value pair`. All `del` needs is the name of the `dictionary` and the `key` that you want to remove.

```python
del dict_py['Idk'];
print("The Deleted One :",dict_py)
removed_value = dict_py.pop("three")  # Remove 'age' and get its value
print("The Removed One :",dict_py)
```

Be aware that the deleted `key-value` pair is `removed permanently`.

---
#### A `Dictionary` of Similar Objects
- Can also use a `dictionary` to store one kind of information about many `objects`.
```python
dict_similar = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(dict_similar["person1"]["name"])
```
##### Looping Through A `Dictionary`
- `Dictionaries` can be used to store information in a variety of ways; therefore, several different ways exist to loop through them
##### Looping Through All `Key-Value` Pairs
- `Python` doesn’t care about the `order` in which `key-value` pairs are stored, it tracks only the `connections` between individual `keys` and their `values`
```python
user = {
    "name": "Alice",
    "age": 25,
    "first" : "Alice",
    "last" : "Bob"
}
for key,value in user.items():
    # print(f"{key} : {value}") ## f means format, and the curly braces are placeholders for the variables
    print("Key :",key,"Value :",value)
for k,v in user.items():
    print(k,v)
```
---
#### Looping Through All the `Keys` in a `Dictionary`
- The `keys()` method is useful when you don’t need to work with all of the values in a `dictionary`
- `keys()` method to find out if a particular `person` was polled
- The `keys()` method isn’t just for looping: It actually returns a list of all the key.

```python
for key in user.keys():
    print("This is Key Looping :" , key);
    print("Values using key :",user[key])

if "last" in user.keys():
    print("Last key exists in the dictionary")
if "lasts" in user:
    print("Lasts key doesn't in the dictionary")
else:
    print("Lasts key doesn't in the dictionary")
```
- Looping Through a `Dictionary`’s Keys in Order
- use the `sorted()` function to get a `copy` of the keys in order
```python
print("-------------------With Sorted Keys -------------------")

dict1 = {
    "name" : "A",
    "age ":21,
    "city" : "Pyay",
    "country" : "Myanmar"
}
for key in dict1.keys():
    print(key,dict1[key])
print("Another one : ");
for key in sorted(dict1.keys()):
    print(key,dict1[key])
```

- Tells `Python` to list all keys in the `dictionary` and sort that `list` before looping through it.

---
#### Looping Through All `Values` in a Dictionary

- use the `values()` method to return a list of `values` without any `keys`.
- pulls all the `values` from the `dictionary` without checking for `repeats`
- In a poll with a large number of `respondents`, this would result in a very `repetitive` list
- use a `set` 

```python
for key in dict_val.keys():
    print("without Rep",key) #skip the repetition , do the first one
    print("with Rep",dict_val[key])

# with repetition
for value in dict_val.values():
    print(value)
# without repetition
for withoutRep in set(dict_val.values()):
    print(withoutRep)
```
- checking `memo` address
```python
dict_test = {
    "name" : "A",
    "names" : "A",
    "city" : "Pyay",
    "country" : "Myanmar"
}
print("Checking the memo address")
print(id(dict_test["name"]))
print(id(dict_test["names"])) ## same because they are referring to the same object called "A"
```
----
#### Nesting

- want to store a set of `dictionaries` in a list or a list of items as a value in a dictionary. This is called `nesting`

##### A `List` of `Dictionaries`
- common to store a number of `dictionaries` in a `list` when each `dictionary` contains many kinds of `information` about one object
- check code :
```python
# List of Dictionaries

person_1 = {
    "name" : "A",
    "age" : 21
}
person_2 = {
    "name" : "B",
    "age" : 22
}

person_3 = {
    "name" : "C",
    "age" : 23
}
people = [person_1,person_2,person_3]
print(type(people))
for person in people:
    print(person)
print("With `:` :",people[0:1])
print("With `:` :",people[:])
for person in people:
   print(person["name"])
# with empty lis
data = []
for bundle in range(30):
    new_data = {"type":"application/api","metadata":"data_1"}
    data.append(new_data)
print("Data :",data)##without format
for d in data:
    print(d) ## with format
print("Length :",len(data))
# first 10
print("Showing the first 10")
for d in data[:10]:
    print(d)
for d in data[:5]:
    if d["metadata"] == "data_1":
       d["metadata"] = "data_updated"
print("Updated Data :",data[:6])
```
- All of the `dictionaries` in the list should have an `identical` structure so that can be looped through the list and work with each dictionary `object` in the same way.

##### A `List` in a `Dictionary`
- sometimes useful to put a `list` inside a `dictionary`.
- `nest` a list inside a `dictionary` any time you want more than one value to be `associated` with a `single` key in a `dictionary`

> [!NOTE]
> You should not nest lists and dictionaries too deeply. If you’re nesting items much
> deeper than what you see in the preceding examples or you’re working with someone else’s code with significant levels of nesting, most likely a simpler way to solve the problem exists.

```python
print("A List in a Dictionary")
person = {
    "name" : "A",
    "age" : 21,
    "hobbies" : ["Reading","Coding","Gaming"]
}
print(person["hobbies"])
```
##### A `Dictionary` in a `Dictionary`
```python
print("A Dictionary in a Dictionary")
person = {
    "name" : "A",
    "age" : 21,
    "address" : {
        "city" : "Pyay",
        "country" : "Myanmar"
    }
}
print(person["address"]["city"])  # Output: Pyay
users = {
    "egon" :{
        "first" : "egon",
        "last" : "spengler",
        "location" : "new york"
    },
    "peter" : {
        "first" : "peter",
        "last" : "venkman",
        "location" : "new york"
    }
}
for username,userinfo in users.items():
    print("Username(key) :",username)
    print("User Info(value) :",userinfo)
    print("Detailed User Info :",);  
    for userinfo_key,userinfo_value in userinfo.items():
        print("Key :",userinfo_key,"\nValue :",userinfo_value)
```

----
