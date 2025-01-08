from collections import OrderedDict;

fav_data = {};
fav_data["D"] = "This is D";
fav_data["C"] = "This is C";
fav_data["E"] = "This is E";

for key,value in fav_data.items():
    print("This Key",[key]," has data :",value);
#3.7  > update
#This means there is no real need for OrderedDict anymore 🎉. They are almost the same.

