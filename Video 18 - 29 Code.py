### LINK to Videos:
# https://www.youtube.com/watch?v=RjhiMjY1nI0&list=PLP5MAKLy8lP8FAytdm2ncZbPioA9A2SgF&index=3&ab_channel=EdoardoMidali


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


### INHERITANCE (19)
class Person: 
    def __init__(self, Name, Surname): 
        self.Name = Name
        self.Surname = Surname

    def greeting(self): # define a method
        print("Hello, my name is " + self.Name)

class Teacher(Person): # create class teacher which extends the class Person
    pass               # passes all attributes and methods from the extended class

teacher_1 = Teacher("Gino","Rossi")
teacher_1.greeting()

class Teacher(Person): 
    def __init__(self, Name, Surname):
        Person.__init__(Name,Surname) # it inherits constructor from extended class (VERSION 1)

class Teacher(Person): 
    def __init__(self, Name, Surname, Subject):
        super().__init__(Name,Surname) # it inherits constructor from extended class (VERSION 2)
        self.Subject = Subject         # this is an attribute of the derived class
    def greeting(self):                # override
        print("Goodmorning, my name is " + self.Name +" "+ self.Surname + " I'm your " + self.Subject + " Teacher")
    def assign_homework(self):         # defines a characteristic method for the derived class
        print("Do your homework for next week")
    def weekly_hours(self, number):    # defines a characteristic method for the derived class with an input parameter
        print("We have "+ str(number) + " hours per week")

teacher_1 = Teacher("Gino","Rossi","Programming")
print(teacher_1.Subject)
teacher_1.greeting()
teacher_1.assign_homework()
teacher_1.weekly_hours(5)

### SCOPE of VARIABLES (20)
# make a variable available in the code (some variables are within functions and others not)
# SCOPE: is that code chunck in which a variable is available for use
#  - local scope: variable is available within a function only
#  - global scope: variable is always available
#  - keyword global scope:

## keyword global

x = 400 #global variable

def my_function():
    x = 100
    print("This is the local variable x = " + str(x))

my_function()
print("This is the global variable x = " + str(x))

def my_function_2():
    global x # set local x to global one
    x = 100  # modify global variable in local function
    print("This is the local variable x = " + str(x))

my_function_2()
print("This is the global variable x = " + str(x))


### MODULES in PYTHON (21)
# Modules are libraries containing a set of functions and variables to include in your own programming code

# To define your own module just create another Python script and write related code

import myModule

myModule.sayHello("Luca")  # recall a function from an imported module

x = myModule.person_1.get("Name")

myModule.sayHello(x)

import myModule as mm # to shorten the module's name (Alias)
                      # if you assign an alias you cannot use the original module's name 
mm.sayHello("Luca")  # recall a function from an imported module

x = mm.person_1.get("Name")

mm.sayHello(x)

import platform
x = platform.system()
print(x)

import math
print(math.sqrt(100))
print(math.floor(2.96))

# Get all functions in an imported module
print(dir(math))
print(dir(platform))

## import just a part of an entire module: you can use only what you import from the import
from myModule import person_1