nums = [1,2,3,5];

for num in nums:
    print("Num :",num)

print ("Range : ")
for num in range(1,10):
    print("Num :",num)

print("This is end")


names = ["egon","leessang","gil","gary"]

for name in names:
    print("Names :",name) # > print all names



    print("Goodbye ..")

print ("Range : ")
for num in range(0,5):
    print("Num :",num)
for num in range(1,5):
    print("Num :",num)

# range() to make a list of number
list_from_range = list(range(0,7));
print(list_from_range)

squares = [];
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)


print(min(squares))
print(max(squares))
print(sum(squares))


# list comprehensive
l_com  = [value**2 for value in range(1,6)]
print("List comprehensive :",l_com)


# range_list = list(range(1,11));
# print("test:",range_list)