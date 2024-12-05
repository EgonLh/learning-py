print("Hello , Python!");

# Chatper 2  : Variable and Simple Data Types

# Changing Cases
_str = "egon lothbork"

print("title() :" + _str.title()); # don't mutate , the orginial one - create a new one
print("lower() :"+_str.lower());
print("upper() :" +_str.upper());
print("normal :" +_str);


#Combining or Concatenating String
print("\nCombining String\n")
f_name = "egon"
l_name = "loth"

name = f_name + " " + l_name;
print("fname + ' ' + lname :" +name)


#stripping Whitespace

str_white =  "Hello , World      "
print(str_white.rstrip() + " : Without Whitespace");
print(str_white + " : with Whitespace")

str_0 = " Hello, World  ";
print(":"+str_0+":")
print(":"+str_0.lstrip()+":")
print(":"+str_0.rstrip()+":")
print(":"+str_0.strip()+":")


# Avoiding Type Errors with the str() Function
age =  2;
print("Hello, your age is " + str(age))


# Follow the guideline of The Zen of Python by Tim Peters