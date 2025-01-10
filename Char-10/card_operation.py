import os;

def checkFile(fileName=""):
    if os.path.isfile(fileName):
        print("File Already Existed ...........")
        return 'a';
    else:
        print("Creating New Files .............")
        return 'w';

def writeMsg(m,fname):
    msg = input(">Enter Your Message Here :");
    with open(fname,m) as file_obj:
        file_obj.write(msg+" \n")
