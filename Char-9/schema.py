from anotherModule import AnotherModule;
class Schema():
    """Schema for the information structure"""
    def __init__(self,name="default",age="default",location="default"):
        self.name = name
        self.age = age
        self.location = location

    def showInfo(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Location :",self.location)

if __name__ == "__main__":
    print("This is Not From the Class")


class DataScheme():
    '''Data Structure for Schema'''

    def __init__(self,data_type):
        self.data_type = data_type
        self.metaData = Schema()

    def printInfo(self):
        print("Data :",self.data_type)