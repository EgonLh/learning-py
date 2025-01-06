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

def return_FName(firstName,lastName,middleName=""):
    return (firstName+" "+middleName+" "+lastName);

print(return_FName("Egon","Loth" ,"Helling").upper())
print(return_FName("Egon","Loth").upper())



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

# makeRecoursive
def factorial(n):
    """Recursive function to find the factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

# with a list of names

names = ["Egon","Loth","Hellsing","Zayar ", "Alex","Norman"];

def print_name(names=[]):
    """Printing Each Names"""
    for name in names:
        print("Hello, ", name);

print_name(names);

# Modifying a list in a function
# assigning students name

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
showRegistered_student(registered_student);


# List with modifying mutate, or not

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

def showStatus(status,*Logs):
    logs_list = list(Logs)
    while logs_list:
        current_log = logs_list.pop();
        print("Log :",current_log);
        logs_collection.append(current_log);
    print("Status Code :",status);

showStatus(404,"The Page Not Contain Any Informative Content","Web Page is too cringe","Sorry, it is Squid game 2","WE need to delete that shit")


# Build Proficle
database = []
# bad practice
# def build_profile(fname,lname,*info,work="default"):
#     print(fname);
#     print(lname);
#     print(work);
#     print(info);
# build_profile("egon","loth","12312","!231231","!2312321","!2313")

# best parctice
def build_profiles(fname,lname,*info,**kwargs):
    print(fname);
    print(lname);
    print(info);
    print("Keyword:\n",kwargs);


build_profiles("egon","loth","2121","!2123123","!2313",size = 12,age=20)

# profile builder

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