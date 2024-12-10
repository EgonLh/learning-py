names = ["Egon" ,"Htun" ,"ZYH" , "Mg Mg"];
print(names);
print(type(names))

nums = ["one","two","three","four","five"]
print(type(nums[0]));
print(nums[0].title());

print(nums[-1])

print("Bro has " , nums[-1].title() , " pens.")

nums[-1] = "six";
print(nums)

# appending
nums2 = nums;
nums.append("five")

print("origin:",nums)
print("reference: ",nums2)

# Solution
nums3 = nums.copy();
nums.append("seven");
print(">.Copy():", nums3);
print(">Origin :", nums)

# inserting
ages = [1,2,3,5];
new_ages = ages;
ages.insert(-1,4);
print("Insert :",ages)

# del ages;
ages.append("five")
print("Original :",ages)
del ages[0]
print("New Age after del [0] :",new_ages)


# pop()

datas = [10,203,402,300];
print("Original :",datas)
removed_data = datas.pop();
print("Removed List : ",datas)
print("Removed : ",removed_data)

first_data  = datas.pop(0);
print("First Data :"+str(first_data))
print("The origin :",datas)


# remove()

books = ["A" ,"B" , "C" , "D" ,"A" , "D"];
books.remove("B");
print("Books :",books);


# sort()
books.sort(reverse=True)
print("Permanently, Reverse",books)

# temp sorted
names = ["aung","maung" , "kyaw"]
print("sorted() :",sorted(names,reverse=True))
print("Original :",names)

names.reverse()
print("Reverse" ,names );
names.reverse()
print("Origin :",names)

print(len(names))