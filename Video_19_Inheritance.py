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