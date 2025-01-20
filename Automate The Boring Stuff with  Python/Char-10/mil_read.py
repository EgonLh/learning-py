file_path = r"C:\Users\egonh\Desktop\WorkSpace\MLOps\Python\Automate the Boring Stuff with Python\Learning_py\Char-10\million.txt";

with open(file=file_path) as file_obj:
    lines = file_obj.readlines(); ## return list
    print(type(lines[0])); ## obtain as str
    print(type(lines[:3]));## now it's list

# chaing list into a single string
mil_string = "";
for line in lines[0:10]:
    mil_string += line.strip(); ## got string
    
print(mil_string);
print(len(mil_string))