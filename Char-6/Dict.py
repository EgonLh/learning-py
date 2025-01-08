# python dictionaries

dict_py = {"one" : 1,"two" : 2 ,"three" :"Four"};

print(dict_py['three'])

test = 1,2,3,4;
print(type(test))
# while tuples are immutable objects, lists are mutable


# adding a new key value pair
dict_py['Idk'] = 5;

print(dict_py)
# doesn't care about the order of the keys, but the values are ordered, and can be accessed by the keys
# care the connection between the keys and values


# Modifying the value of a key
dict_py['three'] = 3;

print("The Mutated One :",dict_py)

# DELETING A KEY VALUE PAIR
del dict_py['Idk'];

print("The Deleted One :",dict_py)
removed_value = dict_py.pop("three")  # Remove 'age' and get its value
print("The Removed One :",dict_py)
print("Removed age:", removed_value)

# A Dictionary of similar objects
dict_similar = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print(dict_similar["person1"]["name"])  # Output: Alice


# looping through the dictionary
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


# Looping with the keys only

for key in user.keys():
    print("This is Key Looping :" , key);
    print("Values using key :",user[key])


if "last" in user.keys():
    print("Last key exists in the dictionary")

if "lasts" in user:
    print("Lasts key doesn't in the dictionary")
else:
    print("Lasts key doesn't in the dictionary")

# ----------------- Merging Dictionaries -----------------

# with sorted keys
print("-------------------With Sorted Keys -------------------")
dict1 = {
    "name" : "A",
    "age ":21,
    "city" : "Pyay",
    "country" : "Myanmar"
}
for key in dict1.keys():
    print(key,dict1[key])

print("");
for key in sorted(dict1.keys()):
    print(key,dict1[key])


# looping through the values
dict_val = {
    "name" : "A",
    "name":"A",
    "city" : "Pyay",
    "country" : "Myanmar"
}

print ("------------------- Looping through the values -------------------")
# key already removed the repetition of the keys, but the values are still repeated
for key in dict_val.keys():
    print("without Rep",key) #skip the repetition , do the first one
    print("with Rep",dict_val[key])

# with repetition
for value in dict_val.values():
    print(value)
# without repetition
for withoutRep in set(dict_val.values()):
    print(withoutRep)

# checking memo address
dict_test = {
    "name" : "A",
    "names" : "A",
    "city" : "Pyay",
    "country" : "Myanmar"
}
print("Checking the memo address")
print(id(dict_test["name"]))
print(id(dict_test["names"])) ## same because they are referring to the same object called "A"


# ------------------- Dictionary Nesting -------------------

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

# with empty list

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

# A List in a Dictionary
print("A List in a Dictionary")
person = {
    "name" : "A",
    "age" : 21,
    "hobbies" : ["Reading","Coding","Gaming"]
}

print(person["hobbies"])    # Output: ['Reading', 'Coding', 'Gaming']

# A Dictionary in a Dictionary
print("A Dictionary in a Dictionary")
person = {
    "name" : "A",
    "age" : 21,
    "address" : {
        "city" : "Pyay",
        "country" : "Myanmar"
    }
}

print(person["address"]["city"])  # Output: Pyay

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