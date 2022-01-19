### CLASSES and OBJECTS (18)
class Person:
    Name = "Diego"
    Surname = "Fabbri"

person_1 = Person() # create an object of class Person
person_2 = Person()

print(person_1.Name) # print name

# defined constructor

class Person: 
    def __init__(self, Name, Surname): 
        self.Name = Name
        self.Surname = Surname

    def greeting(self): # define a method
        print("Hello, my name is " + self.Name)

person_1 = Person("Mattew","Johns") # create an instance with input values
person_2 = Person("Robert","Path")       

print(person_1.Name)
print(person_2.Surname)

# create methods
person_1.greeting()

# the self parameter has to be used in each and every input as parameter

# edit properties of an object
person_2.Name = "Michael" # edit property of an instance
person_2.greeting()

del person_2.Name # remove property of an instance
# person_2.greeting() # this returns an error

# remove an object
del person_2