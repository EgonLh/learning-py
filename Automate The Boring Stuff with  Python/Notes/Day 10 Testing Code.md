- Testing proves that your code works as it’s supposed
to in response to all the input types it’s designed to receive
- using tools in Python’s `unittest` module
----
### Testing A function
- using the module will be more efficient
##### Unit Test and Test Case
- `unit` `test` from the Python standard library provides tools for testing your code.
- A unit test verifies that one specific aspect of a `function`’s behavior is correct.
- A test case is a `collection` of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle
- A good test case considers all the possible kinds of input a function could receive and includes tests to represent each of these situations
- A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function
----
###### A `Passing` Test
- once you’ve set up the test case it’s straightforward to add more unit tests for your functions.
- import the `unittest` module and the function you want to test. Then create a class that inherits from `unittest`.`TestCase`, and write a series of methods to test different aspects of your function’s behavior
- `NamesTestCase` contains a single method that tests one aspect of `get_formatted_name()`
- `unittest’s` most useful features: an assert method
- Assert methods verify that a result you received matches the result you expected to receive
- To check if this is true, we use `unittest`’s `assertEqual`() method and pass it `formatted_name` and 'Janis Joplin'
----
###### A `Failing` Test
- return as `Failed` (`errors` = `1`)
- and show error clearly with `dotstrings`
----
###### Responding To A `Fail` test
- change workflow of the code as follow:
```python
def get_formatted_name(first,last,middle=""):
   """Generate a neslty formatted full name"""
   if middle:
      fullname = first +" " + middle + " " + last
   else:
      fullname = first + " " + last
   return fullname.title();
```
- pass the test as `OK`
----
###### Adding New `Test`
- To test the function, we call `get_formatted_name`() with a first, last, and middle name, and then we use `assertEqual`() to check that the returned full name matches the full name (first, middle, and last) that we expect. When we run `test_name_function`.py again, both tests pass
- add new `test` as follow:
```python
import unittest
from name_function import get_formatted_name;
class NamesTestCase(unittest.TestCase):
    """Test for the `name_function.py`"""
    def test_first_last_name(self):
        """Do Names like Janis Joplin work"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_middle_last_name(self):
        """Do Names with middle work?"""
        formatted_name = get_formatted_name('jeason','jophin','john')
       self.assertEqual(formatted_name,"Jeason John Jophin")
unittest.main()
```

- pass it, and work
---
#### Testing A Class
- helpful to work with many `classes`
- passing `tests` for a class which will be working on its improvements
##### A Variety of Assert Methods
- provided by python for `unittest` `TestCase` class.
- assert methods test true at a `specific` point int he code which is indeed true.
- if false, t raises an exceptions
- see doc about `assert` methods
-----
### A Class For Testing
> check code in the GitHub
#### Create a Unit test for the class
- it work properly by creating 2 `test` cases
```python
import unittest
from  collectionData import CollectData
class TestCollectData(unittest.TestCase):
    """Test for the class which collect data"""
    def test_store_single_response(self):
        """Test that a single response is stored property"""
        question = "What is your hobby?";
        responses = ['Reading','Writing','Running']
        data_collection = CollectData(question);
        data_collection.store_response(responses);
        self.assertIn(responses,data_collection.responses)
```
----
##### Using the Setup method
 In order to create those objects once and then use them in each teset methods, use `setUp` method before running each method starting with `test`
 the test case should name started with `test_` as follow :
 - check codes
 - method `setUp`() does two things: it creates a survey instance, and it creates a list of responses v. Each of these is prefixed by self, so they can be used anywhere in the class. This makes the two test methods simpler, because neither one has to make a survey instance or a response.
 - you’re testing your own classes, the `setUp`() method can make your test methods easier to write. You make one set of instances and attributes in `setUp`() and then use these instances in all your test methods

> [!NOTE]
> When a test case is running, Python prints one character for each unit test as it is
completed. A passing test prints a dot, a test that results in an error prints an E, and a test that results in a failed assertion prints an F. This is why you’ll see a different number of dots and characters on the first line of output when you run your test cases. If a test case takes a long time to run because it contains many unit tests, you can watch these results to get a sense of how many tests are passing.

 - Play around with `tests` to become familiar with the `process of testing` your code. Write tests for the most critical `behaviors` of your functions and classes, but don’t aim for full coverage in early projects unless you have a `specific` reason to do so.
 ----
