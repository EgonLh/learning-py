Object-oriented programming is one of the most effective approaches to writing software. 
- In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.
- When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire
- Making an object from a class is called `instantiation`
- work with `instances` of a class
- You’ll store your classes in modules and import classes written by other programmers into your own program files
- capitalized names refer to classes in Python
- write a docstring describing what this class does
```python
class People():
    '''A simple attempt to create a person object'''
    def __init__(self, name,job):
        '''Initialize name and job'''
        self.name = name;
        self.job = job;
    def info(self):
        print("I am ",self.name, " /nI'm a ",self.job):
    def sayHello():
        print("Hello ,");
```

#### The` __init__()` Method
- A function that’s part of a class is a method
- The `__init__()` method is a special method Python runs automatically whenever we create a new instance based on the class
- This method has two leading underscores and two trailing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names.
- The `self` parameter is required in the method definition, and it must come first before the other parameters
- **Technically both `self` and `this` are used for the same thing**. They are used to access the variable associated with the current instance
- Python calls this `__init__()` method later  the method call will automatically pass the self argument


> [!NOTE] Title
> When we make an instance of Dog, Python will call the __init__() method from the Dog class. We’ll pass Dog() a name and an age as arguments; self is passed automatically, so we don’t need to pass it. Whenever we want to make an instance from the Dog class, we’ll provide values for only the last two parameters, name and age.
- The two variables defined (`setf.....`) each have the prefix self
- Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class.
- Variables that are accessible through instances like this are called `attributes`.
----
##### Making an instance from a class
- When Python reads this line, it calls the `__init__()` method with parameter
- The` __init__() `method has no explicit return statement, but Python automatically returns an instance representing the class. We store that instance in the variable of class.
- Capital for class eg . `Person`
- lowercase for instance `person_1`
----
##### Accessing Attributes
- use `Dot` Notation
```python
person.name ##got name
```

##### `Calling` Methods
- give some `instance` first if there is usage of instance.
- separated by a dot and resuse code as it interprets same way.
```python
person.showInfo()
```
----
##### Creating Multiple `instances`

- Even is the same attributes(parameters), python will create a separate instance from the class. 
- can create as many as it needed.
-  should give `unique` name.

----
#### Working with Classes and Instances

```python
class Song():
    '''Song For Each Singer'''
    def __init__(self,name="default",singer="default",releasedYr="default",album="single"):
        '''Setting Up Variable'''
        self.name = name
        self.singer = singer
        self.releasedYr = releasedYr
        self.album = album
        self.producer = "unknown" # default value for an attributes
    def showInfo(self):
        '''Showing Song's information'''
        print("Song    :",self.name.title(),
              "\nSinger  :",self.singer.upper(),
              "\nReleased:",self.releasedYr.upper(),
             "\nAlbum    :",self.album.upper(),
             "\nProducer :",self.producer.upper())
Nas = Song("Represent","Nas","2002","Illmatic");
Nas.showInfo()
print("\n\n")
Cole = Song("Port Antonio","J.Cole","2024");
Cole.showInfo()
```

##### Modifying `Attributes` Values

It can do it in three ways
- change the value directly through an instance
- set the value through a method 
- increment the value (add a cetrin amount to  it) through a method
Detail Here
###### Modifying an `attribute`'s value directly
- simplest way : modify the value of an attributes - access the attribute directly through an instance.
```python
Cole.releasedYr = "2023";
Cole.album = "Might Delete Later"
Cole.showInfo()
```

###### Modifying an attribute's value through a method

- It can be helpful to have methods that update certain `attributes` for you.
- Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.
```python
print("\nUpdating the Attribute throgh method\n")
Cole.updateProducer("T-minus")
Cole.showInfo()

%% Here is updateProducer Code %%
def updateProducer(self,producer):
        '''updating the released year'''
        self.producer = producer;
```

###### Increasing an `attribute`'s value through a `method`
- just adding some `increment` with `number`, don't need to used in my code

> [!NOTE]
> Effective security takes extreme attention to detail in addition to basic checks like those shown here

----
#### Inheritance

- if the class you’re writing is a `specialized` version of another class you wrote, you can use `inheritance`.
- it automatically takes on all the `attributes` and methods of the first class. The original class is called the `parent` class, and the new class is the `child` class.
- The child class `inherits` every `attribute` and `method` from its `parent` class but is also free to define new attributes and methods of its own.
-----
##### The `__init__()` Method for a Child Class
- first task : to assign values to all `attributes` in the `parent` class.
- To do this, the`__init__()` method for a child class needs help from its parent class.
```python
#demo code
class Book():
    '''class for storing book information'''
    def __init__(self,name,author,edition):
        """Assigning Value to the class"""
        self.name = name
        self.author = author
        self.edition = edition
    def showInfo(self):
        """Show Book information"""
        print("From Parent")
        print("Name :",self.name)
        print("Author :",self.author)
        print("Edition :",self.edition)  

class Pdf(Book):
    """Represent A child class for the book class"""
    def __init__(self, name, author, edition,pdf_Ver):
        super().__init__(name, author, edition)
        self.pdf_Ver = pdf_Ver;
    def showInfo(self):
        """This is for Method Overriding"""
        super().showInfo();
        print("Version :",self.pdf_Ver)
    def show_ver(self):
        """For PDF verison"""
        print("From Child")
        print("Name :",self.name)
        print("Author :",self.author)
        print("Edition :",self.edition)
        print("This is Version ,",self.pdf_Ver)

book1 = Book(name="Machine Learning 100 pages",author="Andriy Burkov",edition="1st");
pdf1 = Pdf(name="Test",author="person",edition="IDK",pdf_Ver="1.1");

book1.showInfo();
print("From Child")
pdf1.showInfo();

pdf1.show_ver();
print("\nTesting\n")
pdf1.showInfo()
```
----
###### Note : `Duck typing`
```python
# Duck Typing Example

class Duck:
    def quack(self):
        print("Quack!")
class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(duck_like):
    duck_like.quack()

duck = Duck()
person = Person()
make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm quacking like a duck!
```
----
##### Defining `Attributes` and `Methods` for the `Child` Class
- Once you have a `child` class that `inherits` from a `parent` class, you can add any new `attributes` and `methods` necessary to differentiate the `child` class from the `parent` class

```python
def __init__(self, name, author, edition,pdf_Ver):
        super().__init__(name, author, edition)
        self.pdf_Ver = pdf_Ver;## adding here
```
----
##### Overriding `Methods` from the `Parent` Class
- define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the parent class

```python
 def showInfo(self):
        """This is for Method Overriding"""
        super().showInfo();
        print("Version :",self.pdf_Ver)
```
----
##### Instances as `Attributes`
```python
class Pdf(Book):
    """Represent A child class for the book class"""
    def __init__(self, name, author, edition,pdf_Ver):
        super().__init__(name, author, edition)
        self.pdf_Ver = pdf_Ver;
        self.collection = Collection(); ......
        
print("Showing Collection\n")
pdf1.collection.showCollection()

```

----
#### Importing Classes

##### Importing A Single Class
- lowercase for file conventions
- Uppercase for Class
```python
from schema import Schema
data = Schema("A",12,"Data");
data.showInfo();
```
-----
##### Storing Multiple `Classes` in A `Module`
```python
from schema import DataScheme;
data_1 = DataScheme("Schema_1");
data_1.metaData.showInfo() ## self.metaData = Schema();
```
-----
##### Importing Multiple `Classes` From A `Module`
- import multiple classes from a module by separating each class with a comma
```python
from schema import Schema,DataScheme
```
-----
##### Importing an Entire `Module`
```python
import schema ##which is file_name
```
----
##### Importing All `Classes` From A `Module`
```python
from schema import *;
```
- recommended for two reasons.

> [!NOTE]
> First, it’s helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses. With this approach it’s unclear which classes you’re using from the module. This approach can also lead to confusion with names in the file. If you accidentally import a class with the same name as something else in your program file, you can create errors that are hard to diagnose. I show this here because even though it’s not a recommended approach

- better off importing the entire `module` and using the `module_name.class_name` syntax
- also avoid the potential naming conflicts that can arise when you import every class in a `module`
-----
##### Importing a `Module` into a `Module`
- When you store your classes in several modules, you may find that a class in one module depends on a class in another module. When this happens, you can import the required class into the first module
- import a module into a common module
-----
##### Standard `Libs`
- The Python standard library is a set of `modules` included with every Python installation
- `Dictionaries` allow you to connect pieces of information, but they don’t keep track of the order in which you add key-value pairs. If you’re creating a dictionary and want to keep track of the order in which key-value pairs are added, you can use the `OrderedDict` class from the collections module. Instances of the `OrderedDict` class behave almost exactly like dictionaries except they keep track of the order in which key-value pairs are added.
- This is a great class to be aware of because it combines the main benefit of lists (retaining your original order) with the main feature of dictionaries (connecting pieces of information).
-----
##### Styling Classes
- Class names should be written in `CamelCase`
- Every class should have a `docstring` immediately following the `class` definition. 
- The `docstring` should be a brief description of what the `class` does, and you should follow the same `formatting` conventions you used for writing `docstrings` in functions
- use `blank` lines to organize `code` ,don’t use them excessively
- can use one `blank` line between `methods`
- module you can use two `blank` lines to separate `classes`

-----
