print("Writing Python :");

filename = input("Enter Your Card Name:");
with open(filename,'a') as file_obj:
    txt = "This Card is for Mr"+filename;
    file_obj.write(txt); 