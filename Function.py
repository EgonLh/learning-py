def sayHello():
    # dotstring
    '''This is function'''
    print('Hello World!');

sayHello(); # Hello World!

# a = def sayHello():

# print(a); # SyntaxError: invalid syntax
# python function are not first class citizens
# python function are not first class citizens
# they can't be assigned to a variable
# they can't be passed as an argument to another function
# they can't be returned from another function


# Passing information to a function 
def sayNames(username):
    print("Names:",username)


sayNames("EgonLoth");

# Multiple Arguements 
# Positional Arguments

def employee_type(department, postition, name):
    """With Positional Arguement"""
    print("|------------------------------")
    print("|The department :",department);
    print("|The postition :",postition);
    print("|The name :",name);
    print("------------------------------")



# employee_type("IT","Head of Development","TH");
# employee_type("Teaching","Assisitant","Mayy");
# employee_type("Student","Manager","Khin");

def student_type(school, name):
    print("I am "+name+ " from "+school);

student_type("IMU" ,"Egon");
student_type("Egon" ,"IMU");

# with Keyword Arguement

student_type(school="PEC",name="ZayYarHtun")


# Default values

def getOrder(item , cost, token = 12):
    print("The Token (",token,") which includes Item (",item, ")is cost " , cost);

getOrder("Brush","100");


def Item_check(a,b,c=3):
    print("a :",a,"\n b :",b,"\n c :",c);


Item_check(1,2,3);
Item_check(1,2)
Item_check(a=1,b=2)

# Retrun Value