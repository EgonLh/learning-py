>The name `Python` comes from the surreal `British comedy group` `Monty Python`, not from the `snake`

>Python programmers are affectionately called `Pythonistas`

---
- How `.py` extension work with `interpreter`
- Every `variable` holds a `value` 
- Change the value of a `variable` in your program at any time, and `Python` will always keep track of `its` current value.
- The Python `variables` you’re using at this point should be `lowercase`. You won’t get errors if you use `uppercase` letters, but it’s a good idea to avoid using them for now.
### String
- A `string` is simply a series of characters : use `""` , `''` to used a `string` in python eg:
```python
str = "Hello, This is a string ."
str_1 = 'Hello, this is a string too .'
```
- make it `flexible` to use `quotes` and `apostrophes` as follow
```python
str = "hello, this's a string"
name = "call'em , ganstars "
```
###### Changing Case In a String with Methods

```python
str = "egon lothbork"
print("title() :" + str.title());
print("lower() :"+str.lower());
print("upper() :" +str.upper());
print("normal :" +str);
```

- don't mutate , the original one - create a new one
- The `lower()` method is particularly useful for storing data
###### Combining or Concatenating String

To `combine` string with separate `variable` 
```python
f_name = "egon"
l_name = "loth"
name = f_name + " " + l_name;
print("fname + ' ' + lname :" +name)
```
- `Python` uses the plus symbol `(+)` to combine `strings`
- This method of combining strings is called `concatenation`
- Use concatenation to `compose` a `message` and store the `entire message` in a variable.
###### Adding Whitespace to String with Tables or Newlines
- `\t`  & `\n`
###### Stripping Whitespace
- To ensure that no whitespace exists at the `right` end of a string, use the `rstrip()` method.
- To ensure that no whitespace exists at the `left` start of a string, use the `lstrip()` method.
- strip `whitespace` from `both` sides at once using `strip()`:
```python
str_0 = " Hello, World  ";
print(":"+str_0+":")
print(":"+str_0.lstrip()+":")
print(":"+str_0.rstrip()+":")
print(":"+str_0.strip()+":")
```

###### Avoiding Syntax Errors with Strings
*This `syntax` error indicates that the interpreter doesn’t recognize something in the code as valid Python code. Errors can come from a variety of sources, and I’ll point out some common ones as they arise. You might see syntax errors often as you learn to write proper Python code.*

----
### Numbers
- `Numbers` are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications, and so on. 
- Python treats numbers in several different ways, depending on how they are being used.
##### Integer
```python
%% Arithematic Operation %%
+
-
*
/
%
```

- Support the` order of  operation `

```python
2 + 3*4
> 14
```
##### Float
```python
>>> 0.1 + 0.2
0.30000000000000004
```
```python
>>> 3 + 0.1
0.30000000000000004
```
- This happens in all languages and is of little concern.
##### Avoiding Type Errors with the `str()` Function
- Use str() to type case and avoid `type` errors
- The `variable` in the `str()` function, which tells Python to represent non-string values as strings
```python
age =  2;
print("Hello, your age is " + str(age))
```
#### Comments

> `Comments` are an extremely useful feature in most programming languages.

- The main reason to write comments is to explain `what your code is supposed to do` and `how you are making it work`
- Writing good `comments` can save you time by `summarizing` your overall approach in clear English.

----
### The Zen Of Python

```python
import this
```

>Now is better than never.

>There should be one-- and preferably only one --obvious way to do it.

>There should be one-- and preferably only one --obvious way to do it.

>Complex is better than complicated.

>Simple is better than complex.

>Beautiful is better than ugly.

----
