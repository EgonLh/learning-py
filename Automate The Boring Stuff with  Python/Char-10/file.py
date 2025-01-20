# > Normal Way
# context = open('info.txt').read();
# print(context)    

with open(r'C:\Users\egonh\Desktop\WorkSpace\MLOps\Python\Automate the Boring Stuff with Python\Learning_py\Char-10\info.txt') as file:
    context = file.read();
    print(context.strip())


#  (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#  > encoding error use r in giving file paths

print("Print Line by Line")
filePath = r"C:\Users\egonh\Desktop\WorkSpace\MLOps\Python\Automate the Boring Stuff with Python\Learning_py\Char-10\info.txt";

with open(filePath) as file_obj:
    for line in file_obj:
        print("Line :",line.strip())

print("Print a list of line from a file");

# Making a list of lines from a file
print("\n--------------------Making a list-------------------\n")
with open(filePath) as file_obj:
    lines = file_obj.readlines()
print('List :\t',lines,"\n");
for line in lines:
    print(line)


print("\n Working With A File's Contents \n");

s_string = "";
with open(filePath) as file_obj:
    print(file_obj)
    lines =file_obj.readlines(); ##return list
    print(type(lines))
    

for line in lines:
    print("Line From List : ",line)
    s_string += (line.strip() + "\n");

print(s_string)
print(len(s_string))
