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