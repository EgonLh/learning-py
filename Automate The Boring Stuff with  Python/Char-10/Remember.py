# Program to remember names of the users

import json

# filename = "username.json";

# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What is your name? :")
#     with open(filename,'w') as f_obj:
#         json.dump(username,f_obj)
#         print("We'll remember you when you come back, "+ username + "!");
# else:
#     print("Welcomeb back "+ username + "!");
    
# Refactored One
def get_store_username():
    """Store User Name if avaliable"""
    filename = "username.json";
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
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