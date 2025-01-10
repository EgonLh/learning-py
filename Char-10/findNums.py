file_path = r"C:\Users\egonh\Desktop\WorkSpace\MLOps\Python\Automate the Boring Stuff with Python\Learning_py\Char-10\million.txt";

with open(file=file_path) as file_obj:
    lines = file_obj.readlines(); ## return list
    print(type(lines[0])); ## obtain as str
    print(type(lines[:3]));## now it's list

# chaing list into a single string
mil_string = "";
for line in lines[0:10]:
    mil_string += line.strip(); ## got string


client_nums = input("Enter Your Number: ");
if(client_nums in mil_string):
    print("Your Number is Here !.")
else:
    print("Invalid Number !")