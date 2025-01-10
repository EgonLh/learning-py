import json

data = [1,2,3,4,5,4,1];

filename = 'data.json'
print("Storing ")
with open(file=filename,mode='w') as file_obj:
    json.dump(data,file_obj);
    
print("Loading ")
with open(filename) as file_obj:
    nums = json.load(file_obj);
    
print("Data Recieved :",nums)