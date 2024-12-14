nums = [1,2,3,4,5]
nums_copy = nums;
nums_copy_2 = nums[:]
print(nums)
print(nums_copy)

nums.append(1)
nums.pop(0)
nums.remove(4)
del nums
print("After Append",nums_copy)

# deep copy
print("with nums[:] ", nums_copy_2)

foods=  ['coffee','tea','burger','coke'];
# my_fav_foods = foods.copy();
my_fav_foods = foods[:];
ava_foods = foods;

print("Foods :",foods)
print("My Fav Foods :",my_fav_foods)
print("Foods :",ava_foods)

print("Add Foods")
foods.append('juices')
print("Foods :",foods)
print("My Fav Foods :",my_fav_foods)
print("Foods :",ava_foods)


