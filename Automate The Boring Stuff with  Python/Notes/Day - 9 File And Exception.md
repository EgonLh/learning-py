- learn to handle `errors` so your programs don’t crash when they encounter unexpected `situations`.
- Learning to work with `files` and save `data` will make  programs easier for people to use.
----
### Reading From A File
- the first step is to read the file into `memory`.
- can read the entire contents of a `file`
- can work through the `file` one line at a time.
----
##### Reading an Entire File
- the `with` statement closes the file for you without you telling it to.
- first need to `open` the file to access it
- `open()` function needs one argument: the name of the file you want to open.
- `open()` function returns an object representing the file
- The keyword `with` closes the file once access to it is no longer needed
- call `open()` in this program but not `close()`
- if a bug in your program prevents the close() statement from being executed, the file may never close. This may seem trivial, but improperly closed files can cause data to be lost or corrupted
- With `with` keyword , Python will close it automatically when the time is right
- [Info](https://stackoverflow.com/questions/43844299/python-read-empty-string-at-the-end-of-a-file#:~:text=read()%20method%20returns%20empty,more%20text%20in%20the%20file.&text=Here%20f.,the%20length%20of%20the%20file.)
- Recall that Python’s `rstrip()` method removes, or `strips`, any whitespace characters from the right side of a string.

----
##### File Paths
- `directory` matters
- folder `scope`, environment `scope`,...
- better ways use `root` path in order to accept files > absolute `file` paths
```python
with open(r'C:\Users\egonh\Desktop\WorkSpace\MLOps\Python\Automate the Boring Stuff with Python\Learning_py\Char-10\info.txt') as file:
    context = file.read();
    print(context.strip())
```

- with `r` there will be some encoding `error`.. such as `Unicode` error.
----
##### Reading Line By Line

- use a `for` loop on the file object to examine each line from a file one at a time
```python
with open(file) as file_obj:
    for line in file_obj:
        print("Line :",line)
```

- `with` syntax to let Python open and close the file properly.
- These blank lines appear because an invisible newline character is at the end of each line in the text file
-  one from the `file` and one from the print statement
- use `strip` to remove those white lines
----
##### Making a `list` of `line` from a file
- `open`() is only available inside the with block that contains
- the `readlines`() method takes each line from the file and stores it in a list. This list is then stored in lines
- each item in lines corresponds to each line in the file, the output matches the contents of the file exactly.
```python
print("\n--------------------Making a list-------------------\n")
with open(filePath) as file_obj:
    lines = file_obj.readlines()
print('List :\t',lines,"\n");
for line in lines:
    print(line)
```
-----
#### Working with a file's contents
- reading file in memory, can do whatever such as manipulation.
- such as working with length as follow:

```python
s_string = "";
with open(filePath) as file_obj:
    print(file_obj)
    lines =file_obj.readlines(); ##return list
    print(type(lines))
for line in lines:
    print("Line From List : ",line)
    s_string += (line.strip() + "\n"); ## don't need if already string....
print(s_string)
print(len(s_string))
```

> [!NOTE]
> When Python reads from a text file, it interprets all text in the file as a string. If you
> read in a number and want to work with that value in a numerical context, you’ll
> have to convert it to an integer using the int() function or convert it to a float using the float() function

#### Large Files : One Million Digits
- Python has no inherent limit to how much data you can work with
```python
file_path = r"C:\Users\egonh\Desktop\WorkSpace\MLOps\Python\Automate the Boring Stuff with Python\Learning_py\Char-10\million.txt";

with open(file=file_path) as file_obj:
    lines = file_obj.readlines(); ## return list
    print(type(lines[0])); ## obtain as str
    print(type(lines[:3]));## now it's list

# chaing list into a single string
mil_string = "";
for line in lines[0:10]:
    mil_string += line.strip(); ## got string
print(mil_string);
print(len(mil_string))
```

check file in project folder.....

----
### Writing a File
- One of the simplest ways to save data is to write it to a file. When you write text to a file, the output will still be available after you close the terminal containing your program’s output.
- you need to call open() with a second argument telling Python that you want to write to the file
- code as follow:
```python
print("Writing Python :");
filename = input("Enter Your Card Name:");
with open(filename,'w') as file_obj:
    txt = "This Card is for "+filename;
   file_obj.write(txt);
```
- 1 . Open the file with open()
- 2 . it can contain two argument
- first one for the name of the file , if not, it will create.
- `w` for `write`
- `r` for `read`
- `a` for `append`
- w will rewrite the file if there is already exists
```txt
Python can only write strings to a text file. If you want to store numerical data in a
text file, you’ll have to convert the data to string format first using the str() function
```

#### Writing Multiple Lines
- You can also use spaces, tab characters, and blank lines to format your output, just as you’ve been doing with terminal-based output.
 #### Appending Files
- use the 'a' argument to open the file for appending rather than writing over the existing file

> check my code for mini-project

----
### Exception
- special objects called exceptions to manage errors that arise during a program’s execution
- make python program to do next excepting the error which broke down the program
- use `try-except` blocks to escape those error and continue the program
- Python Skips over the ecept block, if the code in the try-block causes an error
```python
try:
    print(5/0)
except ZeroDivisionError:## don't know don't add any keys
    print("This is Error")
```

---
##### Using Exception in Prevent Crashes
use the else block as follow to prevent crash
```python
while True:
    f_num = input("Enter Your First Number :");
    s_num = input("Enter Your Second Number: ");
    if (f_num == 'q') or (s_num == 'q'):
        print("Quit ....")
        break;
    try:
        answer = int(f_num)/int(s_num);
    except ZeroDivisionError:
        print("This is Error Here : can't divied by 0 ")
    else:
       print(answer)
```
---
#### Handling `FileNotFound` Error Exception
- One common issue when working with files is handling missing files.
- Here is the code as follow:
```python
print("For File Not Found Handling")
fname = input("Enter filename :");
print(fname)
try:
    with open(fname) as file_buildin_obj:
        lines = file_buildin_obj.readlines()
except FileNotFoundError:
    print("The file",fname,"was not found.")
```

---
#### Analyzing Text
- `split()` method separates a `string` into parts wherever it finds a space and stores all the parts of the string in a list.
```python
print("For File Not Found Handling")
fname = input("Enter filename :");
print(fname)
try:
    with open(fname) as file_buildin_obj:
        lines = file_buildin_obj.read()
except FileNotFoundError:
    print("The file",fname,"was not found.")
else:
    words = lines.split();
    print(words)
    count = len(words)
    print("Count :",count)
```
----
##### For Multiple Files
- make it with method and used it for multiple files
```python
def countWords(fname):
    """To Count Words """
    try:
        with open(fname) as file_obj:
            context = file_obj.read()
    except FileNotFoundError:
        print("The file",fname,"was not found.")
    else:
        wordsCount = len(context.split());
        print("Total Count of file: <"+fname+"> is :",wordsCount);
filenames = ['Card_1','Hello','info.txt'];
for fname in filenames:
    countWords(fname=fname)
```

### Failing Silently
- you don’t need to report every `exception` you catch.
- program to fail silently when an exception occurs and continue on as if nothing happened
- use `pass` to fail it silently
- when a `FileNotFoundError` is raised, the code in the except block runs, but nothing happens
```python
def countWords(fname):
    """To Count Words """
    try:
        with open(fname) as file_obj:
            context = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        wordsCount = len(context.split());
        print("Total Count of file: <"+fname+"> is :",wordsCount);
filenames = ['Card_1','Hello','info.txt'];
for fname in filenames:
    countWords(fname=fname)
```

- The `pass` statement also acts as a `placeholder`
- Our users wouldn’t see this file, but we’d be able to read the file and deal with any missing texts
---
#### Deciding Which `Errors` To Reports
- Giving users information they aren’t looking for can decrease the usability of your program
- Well-written, properly tested code is not very prone to internal `errors`, such as `syntax` or `logical` errors
- every time your program depends on something external, such as 
- user input, 
- the existence of a file, `or` 
- the availability of a `network` connection, there is a possibility of an exception being raised
----
### Storing Data
- will ask users to input certain kinds of information
- store the information users provide in data structures such as lists and dictionaries
- want to save the information they entered
- simple way to store is using `json` module
- `json module` allow to dump simple python data structure into a file and load the data from that data from that file next time , when the program runs.
- can use this to share data between different Python Programs,
- JSON data format can share with other ppl with different programming language
- usable and portable formal
------
### Using `json.dump()` and `json.load()`

- Stores a set of `numbers` and another program that reads these numbers back into `memory`
- `json.dump()` function takes two `arguments`: a piece of data to store and a file object it can use to store the data
- The data is stored in a `format` that looks just like `Python`
- `json.load()` to read the list back into `memory`
- storing and loading are in the same time, it won't matter the order
- a simple way to share `data` between two `programs`.
```python
import json
data = [1,2,3,4,5,4,1];
filename = 'data.json'
print("Storing ")
with open(file=filename,mode='w') as file_obj:
    json.dump(data,file_obj);
print("Loading ")
with open(filename) as file_obj:
    nums = json.load(file_obj);
print("Data Recieved :",nums)
```
---
#### Saving and Reading User-Generated `Data`
- see the code logic and workflow:
```python
# Program to remember names of the users
import json
filename = "username.json";
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? :")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, "+ username + "!");
else:
    print("Welcomeb back "+ username + "!");
```
---
### Refactoring
- recognize that you could improve the code by breaking it up into a series of functions that have specific jobs
- called `refactoring`
- make code cleaner , easier to understand and easier to extend
- update the comments with a docstring that reflects how the program currently works
- not to do so many different tasks, we’ll start by moving the code for retrieving a stored username to a separate function
- must has a clear purpose, as stated in the docstring
- a function should either return the value you’re expecting, or it should return None. This allows us to perform a simple test with the return value of the function
- each function must has a single, clear purpose.
- This compartmentalization of work is an essential part of writing clear code that will be easy to maintain and extend.
```python
def get_store_username():
    """Store User Name if avaliable"""
    filename = "username.json";
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError
        return None;
    else:
        return username
def get_new_username():
    """prompt for the username"""
    username = input("What is your name? :")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user():
    """Greet User by Name"""
    username = get_store_username();
    if username:
        print("Welcome back "+ username + "!");
    else:
        username=get_new_username()
        print("We'll remember you when you come back, "+ username + "!");
greet_user()
```

----
