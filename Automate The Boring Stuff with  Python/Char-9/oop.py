# Commar will leave a space when using print. Plus sign will not leave a space, instead, it will combine two together

class People():
    '''A simple attempt to create a person object'''
    def __init__(self,name,job):
        '''Initialize name and job'''
        self.name = name;
        self.job = job;

    def info(self):
        print("I am",self.name, "\nI'm a",self.job);
    
    
    def sayHello():
        print("Hello ,");


# creating instance

person_1 = People("Egon","Engineer");
person_1.info()
print("The name is",person_1.name)
print("The name is "+person_1.job)

person_2 = People("Loth","Doctor");
person_2.info()
print("The name is",person_2.name)
print("The name is "+person_2.job)

print(id(person_2) == id(person_2))
print(id(person_1) == id(person_1))

print("\nSetting Up Default value to an attribute\n")
class Song():
    '''Song For Each Singer'''
    def __init__(self,name="default",singer="default",releasedYr="default",album="single"):
        '''Setting Up Variable'''
        self.name = name
        self.singer = singer
        self.releasedYr = releasedYr
        self.album = album
        self.producer = "unknown" # default value for an attributes

    def updateProducer(self,producer):
        '''updating the released year'''
        self.producer = producer;

    def showInfo(self):
        '''Showing Song's information'''
        print("Song    :",self.name.title(),
              "\nSinger  :",self.singer.upper(),
              "\nReleased:",self.releasedYr.upper(),
             "\nAlbum    :",self.album.upper(),
             "\nProducer :",self.producer.upper())
    
Nas = Song("Represent","Nas","2002","Illmatic");

Nas.showInfo()

print("\n\n")

Cole = Song("Port Antonio","J.Cole","2024");

Cole.showInfo()

print("\nUpdating the Attribute Directly\n")
Cole.releasedYr = "2023";
Cole.album = "Might Delete Later"
Cole.producer = "DJ Premier"
Cole.showInfo()

print("\nUpdating the Attribute throgh method\n")
Cole.updateProducer("T-minus")
Cole.showInfo()


# Inheritance

class Book():
    '''class for storing book information'''

    def __init__(self,name,author,edition):
        """Assigning Value to the class"""
        self.name = name
        self.author = author
        self.edition = edition

    def showInfo(self):
        """Show Book information"""
        print("From Parent")
        print("Name :",self.name)
        print("Author :",self.author)
        print("Edition :",self.edition)

class Collection():
    '''Book Collection'''
    def __init__(self,released="100",price="000"):
        "For Storing Book Info"
        self.released = released
        self.price=price
    def showCollection(self):
        '''collection book showing'''
        print("Released :",self.released)
        print("Price :",self.price)

class Pdf(Book):
    """Represent A child class for the book class"""
    def __init__(self, name, author, edition,pdf_Ver):
        super().__init__(name, author, edition)
        self.pdf_Ver = pdf_Ver;
        self.collection = Collection();

    def showInfo(self):
        """This is for testing"""
        super().showInfo();
        print("Version :",self.pdf_Ver)

    def show_ver(self):
        """For PDF verison"""
        print("From Child")
        print("Name :",self.name)
        print("Author :",self.author)
        print("Edition :",self.edition)
        print("This is Version ,",self.pdf_Ver)
        


book1 = Book(name="Machine Learning 100 pages",author="Andriy Burkov",edition="1st");

pdf1 = Pdf(name="Test",author="person",edition="IDK",pdf_Ver="1.1");

book1.showInfo();
print("From Child")
pdf1.showInfo();

pdf1.show_ver();
print("\nTesting\n")
pdf1.showInfo()

print("Showing Collection\n")
pdf1.collection.showCollection()

