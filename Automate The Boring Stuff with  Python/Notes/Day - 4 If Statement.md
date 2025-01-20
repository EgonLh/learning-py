>Python uses the values True and False to decide whether the code in an if statement should be executed


##### Checking for `Equality`

```python
car = 'audi'
car == 'bmw' #false
```

- A single equal sign is  a `statement`
- Equality operator(`==`) returns `True` if the values on the left and right side of the operator match.

##### Case Error
- `solved`
```python
car.lower() == 'audi'
#true
car #Audi
```

##### Inequality
- Two values are not equal, you can combine an exclamation point and an `equal` sign (`!=`)
> `<=` ,`>=`, `>` 
#### Using and to Check Multiple Condition
>`and``or``in`
- To improve `readability`, you can use `parentheses`
```python
(age_0 >= 21) and (age_1 >= 21)
```
#### `Boolean` Expressions
- Statement 
	- Careful with `idention`

- The `purpose` of the `if-elif-else` chain is `narrower`.
- `Python` does not require an `else` block at the end of an `if-elif` chain

> [!NOTE]
> The else block is a catchall statement. It matches any `condition` that wasn’t matched by a specific `if` or `elif` test, and that can sometimes include invalid or even malicious data.

- Only one block of `code` to run, use an `if-elifelse` chain. If more than one block of code needs to run, use a series of independent `if` statement.
#### Checking `empty` 
```python
if list:
...
```

----
