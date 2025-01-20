#### How the Input() function work

- pauses the program
- wait for the user to enter text
- store the text in a variable to continue the program

- take one argument : the `prompt`
The input() function takes one argument: the `prompt`, or `instructions`,that we want to display to the user so they know what to do.

---
#### Writing Clear Prompts
- should include a clear, easy-to follow prompt that tells the user exactly what kind of information you’re looking for.
- Add a space at the end of your `prompts`
- multi-line string eg:
```python
promot_msg = "If you tell us who you are, we can personalize the messages you see."
promot_msg += "\nWhat is your first name? "
name = input(promot_msg)
print(f"\nHello, {name}!")
```
---
#### Using `Int()` to Accept Numerical Input
- Python interprets everything the user enters as a `string` ,resolve this issue by using the `int()` function
```python
# input() function always interprets the input as a string
age = int(input("How old are you? ")); # solved the problem by using int() function
print(type(age))
```

>The Modulo Operator
- A useful tool for working with numerical information is the modulo operator `(%)`
 - divides one number by another number and returns the remainder

---
#### `While Loop`
The `for loop` takes a collection of `items` and executes a block of `code` once for each item in the `collection`. In contrast, the while loop runs as long as, or `while`, a certain condition is `true`.

```python
# destructuring the while loop
# initial point > condition > increment
# While loop
current_number = 1 # initial value stored in current_number
while current_number <= 5: # condition to check whether the current_number is less than or equal to 5
    print(current_number) # print the current_number
    current_number += 1 # increment the value of current_number by 1
```

```txt
In the first line, we start counting from 1 by setting the value of current_number to 1. The while loop is then set to keep running as long as the value of current_number is less than or equal to 5. The code inside the loop prints the value of current_number and then adds 1 to that value with current_number += 1.
Python repeats the loop as long as the condition current_number <= 5 is true. Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2. Because 2 is less than 5, Python prints 2 and adds 1 again, making the current number 3, and so on. Once the value of current_number is greater than 5, the loop stops running and the program ends:
```
---
##### With `User` Interaction

```python
useMsg = "Enter 'quit' to end the program."
useMsg += "\nWhat is your name? "
msg = ""
while msg != 'quit':
    msg = input(useMsg)
    print(msg)
```
---
##### Using a `Flag`

```python
flag = True
while flag:
    msg = input(useMsg)
    if msg == 'quit':
        print("Flag :",flag)
        flag = False
    else:
        print(msg)
```
---
##### Using `break`
- To exit a while loop immediately without running any remaining code in the loop,
```python
# with break statement
while True:
    msg = input(useMsg)
    if msg == 'quit':
        print("break---->")
        break
    else:
        print(msg)
```
- You can use the `break` statement in any of Python’s loops. For example, you could use `break` to quit a for loop that’s working through a list or a dictionary.
- Using `Continues` in A Loop
- Rather than breaking out of a loop entirely without executing the rest of its code
- `continue` statement to return to the beginning of the loop based on the result of a conditional test

```python
counter = 0;
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print("End of the program after continue",counter)
```

- the `continue` statement tells Python to ignore the rest of the loop and return to the beginning. If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number

##### Avoiding `Infinite` Loop

```[note]
To avoid writing infinite loops, test every while loop and make sure the loop stops when you expect it to. If you want your program to end when the user enters a certain input value, run the program and enter that value. If the program doesn’t end, scrutinize the way your program handles the value that should cause the loop to exit. Make sure at least one part of the program can make the loop’s condition False or cause it to reach a break statement
```

---
##### Using While loop with `list` and `dictionaries`
- Moving Items from one list to another
```python
normalUser = [
    {
        "username": "user1",
        "token" :True
    },
    {
        "username": "user2",
        "token" :True
    },
    {
        "username": "user3",
        "token" :False
    },
]
auth_user = []
while normalUser:
    print(normalUser ,"\n")
    current_user = normalUser.pop() ## decrement the list
    if current_user["token"]:
        auth_user.append(current_user)
```
---
- Removing All instances of Specific Values from a list

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'rabbit' in pets:
    pets.remove('rabbit')
print(pets)
rm_duplicate = set(pets);
print(rm_duplicate)
```
----
#### Filling A Dictionary with User Input
```python
responses = {}
while True:
    key = input("Enter Your Key :");
    value = input("Enter Your Value :");
    responses[key] = value;
    exit = input("Do you want to exit? (yes/no) :")
    if(exit == "yes"):
       break;
print("Data :",responses)
```
----
