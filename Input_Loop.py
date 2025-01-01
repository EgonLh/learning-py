# input 
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# promot_msg = "If you tell us who you are, we can personalize the messages you see."
# promot_msg += "\nWhat is your first name? "

# name = input(promot_msg)
# print(f"\nHello, {name}!")

# input() function always interprets the input as a string
# age = int(input("How old are you? ")); # solved the problem by using int() function
# print(type(age))

# # The modulo operator (%) divides one number by another number and returns the remainder
# print(6%2); # 0
# print(7%2); # 1

# While loop
# current_number = 1 # initial value stored in current_number
# while current_number <= 5: # condition to check whether the current_number is less than or equal to 5
#     print(current_number) # print the current_number
#     current_number += 1 # increment the value of current_number by 1

# destructuring the while loop
# initial point > condition > increment

# useMsg = "Enter 'quit' to end the program."
# useMsg += "\nWhat is your name? "
# msg = ""

# while msg != 'quit':
#     msg = input(useMsg)
#     print(msg)

# With a flag
# flag = True

# while flag:
#     msg = input(useMsg)
#     if msg == 'quit':
#         print("Flag :",flag)
#         flag = False
#     else:
#         print(msg)

# with break statement
# while True:
#     msg = input(useMsg)
#     if msg == 'quit':
#         print("break---->")
#         break
#     else:
#         print(msg)

# Using continue in a loop
counter = 0;
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print("End of the program after continue",counter)

