
> [!NOTE]
> `Functions`, which are named blocks of code that are designed to do one specific job

##### Defining a `function`
- Use the keyword `def`
- indented line that follow `def` , make up the body of the function
- `'''This is docstring'''
- Python looks `docstring` for when it generates documentation for the functions in your programs.
```
python function are not first class citizens
they can't be assigned to a variable
they can't be passed as an argument to another function
they can't be returned from another function
they can't be stored in a data structure
```
---
#### Passing `Information` to a Function 
- `parameter`
- to produce a predictable output every time.
```python
def sayNames(username):
    print("Names:",username)
```
The variable named "`username`" is called `parameter`
- a piece of information the function needs to do its jobs

```python
sayNames("Egon");
```
- the term "`Egon`" us called `agruement`
- the value is stored in the parameter `username`

> [!NOTE]
> People sometimes speak of `arguments` and `parameters` interchangeably. Don’t be surprised if you see the variables in a function definition referred to as `arguments` or the variables in a function call referred to as `parameters`.


#### Passing `Arguments`
- function can have `multiple` parameters , may need multiple arguments
- can use positional `arguments` > which need to be the same order the parameters were written:  keyword arguements

#### Positional `Arguments`
- The simplest way to do this is based on the order of the `arguments` provided.
- Values matched up this way are called `positional` arguments
```python
def employee_type(department, postition, name):
    """With Positional Arguement"""
    print("|------------------------------")
    print("|The department :",department);
    print("|The postition :",postition);
    print("|The name :",name);
    print("------------------------------")
```

- can use `multiple` time as follow:
```python
employee_type("IT","Head of Development","TH");
employee_type("Teaching","Assisitant","Mayy");
employee_type("Student","Manager","Khin");
```
----
##### Order Matter in Positional Argument
```python
employee_type("Head of Development","Khin Khin","IT"); ##wrong order
```
check the order of the parameters in the function’s definition

----
#### Keyword `Argument`
- A `keyword` argument is a `name-value` pair that you pass to a function
- explicitly tell Python which parameter each argument should be matched with.
- The order of keyword arguments doesn’t matter because Python knows where each value should go.
```python
def student_type(school, name):
    print("I am "+name+ " from "+school);
student_type("IMU" ,"Egon");
student_type("Egon" ,"IMU");
# with Keyword Arguement
student_type(school="PEC",name="ZayYarHtun")
```

When you use keyword arguments, be sure to use the exact names of the parameters in the function’s `definition`.

----
#### Default `Values`

> [!NOTE]
> When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.

```python
def getOrder(item , cost, token = 12):
    print("The Token (",token,") which includes Item (",item, ")is cost " , cost);
getOrder("Brush","100");
```

- The default `parameter` must be the `rightmost` because of its orders , let see how:

```python
%% Error Case %%
def Item_check(a=1,b,c):
    print("a :",a,"\n b :",b,"\n c :",c);
Item_check(1,2,3)
Item_check(b=1,c=2); ##non-default argument follows default argument
```

##### Equivalent `Function` Call

- Because positional `arguments`, keyword `arguments`, and default values can all be used together, often you’ll have several equivalent ways to call a function.

```python
##sample func call
def Item_check(a,b,c=3):
    print("a :",a,"\n b :",b,"\n c :",c);
Item_check(1,2,3);
Item_check(1,2)
Item_check(a=1,b=2)
```

> [!NOTE]
> It doesn’t really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.


#### Avoiding `Argument` Errors
- get a similar traceback that can help you correctly match your function call to the function definition.

---
#### `Return` Values

- The value the function `returns` is called a return value.
- The return statement takes a value from inside a function and sends it back to the line that called the `function`.
- `Return` values allow you to move much of your program’s grunt work into functions, which can `simplify` the body of your program.

```python
def return_FName(firstName,lastName,middleName=""):
    return (firstName+" "+middleName+" "+lastName);
print(return_FName("Egon","Loth" ,"Helling").upper())
print(return_FName("Egon","Loth").upper())
```

- `Optional values` allow functions to handle a wide range of use cases while letting function calls remain as simple as possible.
---
##### Return A `Dictionary`
- A `function` can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.

```python
# Returing Dict
def setNameDict(fName,Lname,Mname=""):
    if Mname:
        nameDict={'firstName':fName,'MidName':Mname,'lastName':Lname}
    else :
        nameDict={'firstName':fName,'lastName':Lname}
    return nameDict;
person1 = setNameDict('Zay','Htun','Yar')
print(person1)
person2 = setNameDict('Zayar','Htun')
print(person2)
```

- This function always stores a person’s name, but it can also be modified to store any other information you want about a person.

#### Using a Function with a while Loop

---
- Passing A `List`

```python
names = ["Egon","Loth","Hellsing","Zayar ", "Alex","Norman"];
def print_name(names=[]):
    for name in names:
        print("Hello, ", name);
print_name(names)
```

- Modifying a `List` in a function

```python
unregistered_students = ["Egon","Zayar","Htun"];
registered_student = []
def registered_system(unregistered_student,registered_student):
    while unregistered_student:
        pending_student = unregistered_student.pop();
        print("This student named (",pending_student,") pending to register.....");
        registered_student.append(pending_student);
def showRegistered_student(student_list):
    for name in student_list:
        print("Name :",name);
print("-------------------------------------------------\nBefore Register ,\nStudentList > ",unregistered_students , "\nRegister Student > ",registered_student,"\n-------------------------------------------------")
registered_system(unregistered_students,registered_student);
showRegistered_student(registered_student)
```
- This example also demonstrates the idea that every function should have `one specific job`. The first function prints each design, and the second displays the completed models. This is more beneficial than using one function to do both jobs.

##### Preventing a Function From `Modifying` a list:
- `The list is now empty, and the empty list is the only version you have; the original is gone.`
- `Any changes the function makes to the list will affect only the copy, leaving the original list intact.`

```python
func(list_name[:])
```

- Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy.
- It’s more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you’re working with large lists.

```python
org_list = [1,2,3,4];

update_list = [];
def change_list(org, update):
    '''For Changing the list from org to update'''
    while org:
        item = org.pop();
        update.append(item);
    print("End")
print("Before \n",org_list ,"\n",update_list)
# change_list(org_list,update_list); #change the orginal
change_list(org_list[:],update_list) #don't change the orgnial
print("After \n",org_list ,"\n",update_list)
```

> [!NOTE]
> Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy. It’s more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you’re working with large lists


----
#### Passing an `Arbitrary` Number of Arguments

- For the case where don't know how many arguments a function needs to accepts
- thus used an `arbitrary` number of arguments from the calling statement
- The `asterisk` in the parameter name `*` toppings tells Python to make an empty `tuple`
- Note that `Python` packs the arguments into a tuple, even if the function receives only one value
- This syntax works no matter how many arguments the function `receives`.
```python
# Aribitary Numbers
logs_collection = [];
def showLog(*Logs):
    logs_list = list(Logs)
    while logs_list:
        current_log = logs_list.pop();
        print("Log :",current_log);
        logs_collection.append(current_log);
showLog("Create 1","Create 2 ","Update 2")
print("Collection :",logs_collection)
```

----
#### Mixing `Positional` And `Arbitrary` Arguments
- Python matches `positional` and `keyword` arguments first and then collects any remaining arguments in the final parameter
- Python stores the first value it receives in the parameter size. All other values that come after are stored in the tuple. The function calls include an argument for the size first, followed by as many  as needed.

```python
def showStatus(status,*Logs):
    logs_list = list(Logs)
    while logs_list:
        current_log = logs_list.pop();
        print("Log :",current_log);
        logs_collection.append(current_log);
    print("Status Code :",status);
showStatus(404,"The Page Not Contain Any Informative Content","Web Page is too cringe","Sorry, it is Squid game 2")
```
---
Using `Arbitrary` in Keyword Arguments

> [!NOTE]
> `*`args (arguments) allows you to pass a variable number of positional arguments to a function. `**`kwargs (keyword arguments) allows you to pass a variable number of keyword arguments (key-value pairs) to a function.


```python
def build_profiles(fname,lname,*info,**kwargs):
    print(fname);
    print(lname);
    print(info);
    print("Keyword:\n",kwargs);
build_profiles("egon","loth","2121","!2123123","!2313",size = 12,age=20)
```

Note:
- can mix positional, keyword, and arbitrary values in many different ways when writing your own functions. It’s useful to know that all these argument types exist because you’ll see them often when you start reading other people’s code
- It takes practice to learn to use the different types correctly and to know when to use each type
```python
profiles_datas = [];
def profile_builder(fname,lname,address,**data):
    '''example app'''
    personalProfile={};
    personalProfile['FirstName'] = fname;
    personalProfile['LastName'] = lname;
    personalProfile['address'] = address;
    for key,value in data.items():
        personalProfile[key]= value;
    print(personalProfile);
    profiles_datas.append(personalProfile);
profile_builder("Anna","Wong","China",age=20,zipcode=1212,bloodType="A");
profile_builder("Taylor","Lockhart","Rome",age=30,zipcode=1232,city="IDK",passion="Reading");
print("\n\nProfle Datas :")
print(profiles_datas)
```

#### Storing Functions in Modules

- can go a step further by storing your functions in a separate file called a module and then importing that module into your main program
- An import statement tells Python to make the code in a module available in the currently running program file
- Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. It also allows you to reuse functions in many different programs. When you store your functions in separate files, you can share those files with other programmers without having to share your entire program. Knowing how to import functions also allows you to use libraries of functions that other programmers have written.
-----
##### Importing an entire module
- A module is a file ending in `.py` that contains the code
- don’t actually see code being copied between files because Python copies the code behind the scenes as the program runs. All you need to know is that any function defined in `module.py` will now be available in `file_name.py`.
- don’t actually see code being copied between files because Python copies the code behind the scenes as the program runs. All you need to know is that any function defined in pizza.py will now be available in `making_pizzas.py`.
- example code :
```python
import arithmetic; ##importing an entire module
sum = arithmetic.add(1,2);
print("module.methpd:",sum)
ans = arithmetic.subtract(2,1);
print("module.methpd:",ans)
```

##### Importing specific functions

- Import a specific function from a module as follow:
```python
from showLog import showError;
showError("Error 1")
```

- With this `Syntax`, you don’t need to use the dot notation when you call a function. Because we’ve explicitly imported the function  in the import statement.

##### Using `as` to Give a function an alias

- can use a short, unique `alias`—an alternate name similar to a nickname for the function.
```txt
from module_name import function_name as fn
```
- Demo code
```python
from showLog import showData as pr;
pr("Hello this is alias import");
```
- can also provide an `alias` for a module name
- Giving a module a short `alias`
- These function and import should named clearly to  tell you what each function does, are more important to the readability

as follow:
```python
import learn as ln;
ln.learn("machine")
```
---
##### Importing all functions in a module
- can tell `Python` to import every function in a module by using the asterisk `(*)` operator
- Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite the `functions`
- The best approach is to import the function or functions you want, or import the entire module and use the dot notation.
```python
from learn import *
learn("From * :")
```

##### Styling
- Functions should have descriptive names,
- should use lowercase letters and underscores
- Module names should use these conventions as well
- Every function should have a comment that explains concisely what the function does.
- In a well-documented function, other programmers can use the function by reading only the description in the docstring.
- If you specify a default value for a parameter, no spaces should be used on either side of the equal sign
- If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins.
- All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program.
- PEP 8 [doc](https://www.python.org/dev/peps/pep-0008/) recommendation
----
