normalUser = [
    {
        "username": "user1",
        "token" :True
    },
    {
        "username": "user2",
        "token" :True
    },
    {
        "username": "user3",
        "token" :False
    },
]

auth_user = []

while normalUser:
    print(normalUser ,"\n")
    current_user = normalUser.pop() ## decrement the list
    if current_user["token"]:
        auth_user.append(current_user)
print("Auth Users" ,auth_user)


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'rabbit' in pets:
    pets.remove('rabbit')

print(pets)

rm_duplicate = set(pets);
print(rm_duplicate)


# filling a dictionary with user input

# responses = []

# while True:
#     name = input("Enter Your Name :");
#     password = input("Enter Your Password :");
#     data = {
#         "name": name,
#         "password": password
#     }   
#     responses.append(data);

#     exit = input("Do you want to exit? (yes/no) :")
#     if(exit == "yes"):
#         break;

# print("Data :",responses)


# filling a dictionary with user input
responses = {}

while True:
    key = input("Enter Your Key :");
    value = input("Enter Your Value :");
    responses[key] = value;

    exit = input("Do you want to exit? (yes/no) :")
    if(exit == "yes"):
        break;

print("Data :",responses)