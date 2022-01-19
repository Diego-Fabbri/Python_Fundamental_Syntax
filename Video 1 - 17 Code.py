#LINK to Videos:
# https://www.youtube.com/watch?v=RjhiMjY1nI0&list=PLP5MAKLy8lP8FAytdm2ncZbPioA9A2SgF&index=3&ab_channel=EdoardoMidali


#messaggio = input("Insert something as input:") #Insert a user input
#print(messaggio)

#Indentation is fundamental in Python

### VARIABLES (03)
# In python variables must be declared and assigned to a value.
# Other programming languages allow on variable's declaration.
# VARIABLES' NAMES:
# nameSurname (CamelCase)
# NameSurname(Pascal case)
# Name_Surname (Snake Case) Highly suggest by Python's documentation

x = 5 #single assignment
y = 6
x,y,z = 5,6,7 #multiple assignment
print(x)
print(y)
print(z)

#math
x = 32
y = 8
z = x + y + x + x
print(z)

### DATA TYPES (04)

## Single data
# str: x = "hello"
# int: x= 20
# float: x = 20.5 
# bool: x = True 


## Collection of data
# list: x = ["Rome", "Milan", "Cosenza"] 
# tuple: x = ("Rome", "Milan", "Cosenza")
# range: x = range(6)
# dict: x = {"Name": "Diego", "Age": 25} # use a key-value relationship
# set: x = {"Rome", "Milan", "Cosenza"} 

x = 5.5
print(type(x)) #get variable's type

### CASTING (05): coherce a variable type to another 
## int(), str(), float()

x = "5"
y = str(5)
print(x + y)

### WORK WITH STRINGS (06)
x = "Hello"
print("Hello")
print(x)

## write multirow strings
x = """Hello
my 
name 
is 
Diego"""
print(x)

# strings are manipulated as array in Python

x = "Hello Diego"
print(x[0]) #each and every character as and index from 0 to ....
print(x[5])

len(x) # get length of the string
print(len(x))

## extract part of a string

x = "Hello I am Diego"
print(x[:3]) # get characters from poition 0 to 2 (3 not included)
print(x[2:]) # get characters from poition 2 to the end
print(x[2:7]) # get characters from poition 2 to 6 (7 not included)

print(x[-4]) # start from right side, returns the 4th character
print(x[-4:]) # start from right side, returns the 4th character to the end on therogth side

## Modify strings

print(x.upper()) #transform string in UPPER CASE
print(x.lower()) #transform string in LOWER CASE
x = " Hello I am Diego "
print(x.strip()) # remove blank spaces on both external sides
print(x.replace("l","K")) # replace all "l" with "K"

## Concatenate strings
x = "Hello I am "
y = "Diego" 

print(x + y) # concatenate

## Combine strings and numbers

test = "Hello I am Diego, I am {} years old"
print(test.format(25))
age = 25
print(test.format(age))

test = "Hello I am Diego, I am {} years old, I am {} cm tall"
age = 25
heigth = 181
print(test.format(age, heigth))

# you can use indexes to place arguments in {}
test = "Hello I am Diego, I am {1} years old, I am {0} cm tall"
age = 25
heigth = 181
print(test.format(age, heigth))

## Escape of characters
test = "Hello I am Diego and I am \"nice\""
print(test)

test = "Hello I am Diego and I\'m \"nice\""
print(test)

### BOOLEAN (07)
x = 0
y = 1

print(5 < 10) #verify condition

if 5 < 10:
    print("5 is less than 10")
else:
    print("5 is greater than 10")

## List of values that always return a False values using bool() function
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

print(bool(x)) # return false because x = 0
print(bool(y)) # return true because y = 1

things_to_buy = []

print(bool(things_to_buy)) #the list is empty

### MATH OPERATORS (08)
# Fist is *, second is division the addition and subtraction

x = 15
y = 7
# + addition
# - subtrction
# * multiply
# / division
# % module (remainder after division)
# ** power
# // floor division

print(x + y)
print(x - y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

## Assignment operators
x = 5
x = 5 + x # or x+=2
          # You can also use -= *= /= .
          #  There are 5 additional operators in Python
y = 7

print(x)

## Math Functions
x = min(5,10,25) # get minimum
print(x)

x = max(10,15,20) # get maximum
print(x)

x = abs(-y)       # get absolute value
print(x)

x = pow(3,2)      # get 5 up to the 2 power
print(x)

### CONDITIONS: IF, ELIF, ELSE (09)
x = 5

# basic syntax of if operator
if x < 10:
    print("x is less than 10")
else:
    print("x is greater than 10")

## Operators to compare
# == equal to
# != different
# < / <= greater than / greater than or equal to
# > / >= less than / less than or equal to

## elif
x = 10

if x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is greater than 10")

## Logical operators: and, or & not
x = 10
y = 5

if x > 10 and x < 20: # both condition have to hold
    print("x is less than 20 and greater than 10")
else:
    print("x is not in [10,20]")

if x == 10 or y == 10: # just one condition has to hold
    print("condition holds")
else:
    print("condition does not hold")

x = 9

if not(x > 10): # it reverses rationale
    print("condition holds")
else:
    print("condition does not hold")

## Short end version of if operator

#Version 1
if x > 10: print("x is greater than 10") # it works only with one statement

#Version 2
# ---- if condition ------------------ | ------- else condition ----
print("x is greater than 10") if x > 10 else print("x is less than 10")

## nested if
x = 9

if x % 2 == 0:
        if x < 10:
            print("x is even")
            print("x is less than 10")
else:
    print("x is odd")
 

### LOOPS: WHILE (10)

x = ["Rome","Milan","Cosenza"] 

# basic syntax of while loop
i = 0
while i < 6: # until condition holds loop works
    print(i)
    i = i + 1

# break: it stops loop's execution
i = 0
while i < 6: # until condition holds loop works
    print(i)
    if i == 3:
     print("break loop")   
     break
    i = i + 1

# continue: it skips to the next loop's iteration
i = 0
while i < 6: # until condition holds loop works
    i = i + 1
    if i == 3:
     print("continue loop, iteration skipped")   
     continue
    else:
        print(i)

# else: it work at the end of while loop's iterations
i = 0
while i < 6:
    print(i)
    i = i + 1
else:
    print("end of while loop")


### LOOPS: FOR (11)

list_of_cities = ["Milan","Rome","Cosenza"] # list
string = "letter" #using strings

for city in list_of_cities:
    print(city)

for c in string:
    print(c)

for x in range(6):  # using range()
    print(x)

# else: it works at the end of for loop
for x in range(6):  
    print(x)
else:
    print("end of for loop")


# break: it stops for loop iterations
for x in range(6):  
    if x==3:
        print("For loop iterations stopped")
        break      
    print(x)

# continue: it skips for loop iterations
for x in range(6):  
    if x == 3:
        print("For loop iteration skipped")
        continue      
    print(x)


### COLLECTION OF DATA: list, tuple, set, dictionary (12- Theory)

## Characteristics of a data collection: 
# - ordered: elements have a defined order
# - indexing: elements are accessible by an index
# - editable: elements can be modified, removed or added 
# - immutable: elements cannot be modified, removed or added 
# - allow duplicates: elements can be duplicated 

# Important: if elements are ordered you can access them by an index

## Data collection definitions
# - Lists are ordered and editable data collection. Lists allow duplicates
# - Tuples are ordered and immutable data collection. Tuple allow duplicates

# - Sets are unordered and unindexed data collection. Sets do not allow duplicates. (elements cannot be modified)
# - Dictionaries are ordered and editable data collection (version 3.7). Dictionaries do not allow duplicates.

### DATA COLLECTION: LIST (13)
# List is a ordered, indexed, editable and duplicates allowing data collection.

x = ["Milan","Rome","Cosenza","Turin"] # same type (Version 1)
type(x) # get type of the list
len(x) # get length of the list

# x = list("Milan","Rome","Cosenza") # (Version 2)

y = ["Hello", 95, False] # different type

print(x[0]) # access element of the list
print(x[-1]) # acces last element
print(x[2:]) # access elements by a range (from element in position 2 to last element)
print(x[1:3]) # access elemets by a range (from element in position 1 to element in position 3-1)
print(x[:2]) # access elements by a range (from element in position 0 to element in position 2-1)

# WARNING: you can also use negative index

## access elements

x[0] = "New York" # replace a single value
print(x)

x[1:3] = ["Boston","Paris"] # replace values by a range
print(x)

x[1:3] = ["Miami"] # replace multiple values with only one
print(x)
print(len(x))

# add elements

x.append("Berlin") # insert the element at the end of the list
print(x)
print(len(x))

x.insert(1, "Florence") # insert element in position 1
print(x)
print(len(x))

y = ["Barcelona", "Budapest"]

x.extend(y) # add elements of y list to the end of x
print(x)
print(len(x))

# remove elements

x.remove("Barcelona") # remove an element according to its value
print(x)

x.pop() # remove the last element of a list
print(x)

x.pop(1) # remove element in position 1
print(x)

del x[0] # remove element in position 0 of the list (you can also remove the entire list using del x)
print(x)

x.clear() # remove all elemets from the list making it empty
print(x)

x = ['New York', 'Florence', 'Miami', 'Turin', 'Berlin', 'Barcelona', 'Budapest']

# loops on elements

for city in x:
    print(city)

for i in range(len(x)):
    print(x[i])

i = 0
while i < len(x):
    print(x[i])
    i = i + 1

# list comprehension: allow to use a shorter syntax

[print(city) for city in x if city != "Turin"]

# edit order of a list
x = ['New York', 'Florence', 'Miami', 'Turin', 'Berlin', 'Barcelona', 'Budapest']

x.sort() # sorts elements in numerical/ alphabetical order (ascending)
x.sort(reverse = True) # sorts elements in reversed numerical/ alphabetical order (descending)

# how to copy a list
x = ['New York', 'Florence', 'Miami', 'Turin', 'Berlin', 'Barcelona', 'Budapest']
y = x

y[0] = "Athens" # if you change values in y, corresponding ones change in x due to  y=x
                # to avoid that you need a copy

print(x)

y = x.copy() # or use   y = list(x)
print(y)
y[0] = "New York"
print(y)
print(x) # using copy() the source list x does not change

# how to make union of lists: +, append(), extend()
x = ['New York', 'Florence', 'Miami', 'Turin', 'Berlin', 'Barcelona', 'Budapest']
y = ["Athens", "Beijing"]

print(x + y) #using +

for city in y: # using append()
    x.append(city)
else:
    print(x)

x.extend(y) # using extend()

### DATA COLLECTION: TUPLE (14)
# Tuple is a ordered, indexed, uneditable and duplicates allowing data collection.

x = ("Milan","Rome","Cosenza") #single type elements (Version 1)
y = ("Milan", True, 45) # multiple type elements

# if you want to create a tuple with only one value you must use the folloqing syntax
x = ("Milan",)

# tuple() creates a tuple (Version 2)
x = tuple(("Milan","Rome","Cosenza"))
print(x)


# access tuple's elements

print(x[0]) # access element of the list
print(x[-1]) # acces last element
print(x[2:]) # access elements by a range (from element in position 2 to last element)
print(x[1:3]) # access elemets by a range (from element in position 1 to element in position 3-1)
print(x[:2]) # access elements by a range (from element in position 0 to element in position 2-1)

#verify if an elements exists in a tuple
if "Milan" in x:
    print("City in tuple x")
else:
    print("Citu not in tuple x")

# in a tuple you cannot modify elemnts there this syntax is not allowed: x[0] = "Paris"
# in a tuple you cannot remove elements

# If you want to modify the tuple or its own elements you can transform the tuple in a list,
# modify the new created list and then transform it a tuple again as reported in the following lines:

x = tuple(("Milan","Rome","Cosenza"))

y = list(x)
print(y)

y[0] = "Paris"

x = tuple(y)
print(x)

# eliminate the entire tuple
del x 

## assign tuple's element to a variable
cities = tuple(("Milan","Rome","Cosenza"))

(x,y,z) = cities

print(x)
print(y)
print(z)

# if you have more elements than variables
cities = tuple(("Milan","Rome","Cosenza","Paris","Turin"))

(x,y,*z) = cities

print(x)
print(y)
print(z) # z is a list with remaing values

## loop on elements
for city in cities:
    print(city)


for i in range(len(cities)):
    print(cities[i])


while i < len(cities):
    print(cities[i])
    i = i + 1

# concatenate/union tuples: +

x = tuple(("Milan","Rome","Cosenza"))
y = tuple(("Turin","Bologna","New York"))

print(x + y)

# COUNT: it counts how many times a value occurs in a tuple
x = tuple(("Milan","Rome","Cosenza","Milan"))
print(x.count("Milan"))

# INDEX: it return the index of input value in a tuple (it takes only the first values occurring, it does not take in account duplicates)
x = tuple(("Milan","Rome","Cosenza"))
print(x.index("Milan"))


### COLLECTION OF DATA: SETS (15)
# Sets are unorderd, unindexed, uneditable and duplicates not allowing data collections

x = {"Milan","Rome","Cosenza"} # elements of same type VERSION 1
y = {"Turin", 69, False} # elements of same type

# you can use type(), len()

x = set(("Milan","Rome","Cosenza")) # VERSION 2

# if you want to access elements you have to use loops being sets unordered and unindexed data collections
# x[0] cannot be used as syntax, even if you print elements they are returned in a different order in output print

for city in x:
    print(city)


# add new elements: add() and update()
x = set(("Milan","Rome","Cosenza"))
y = set(("Turin","Bologna","New York"))

x.add("Venice")
print(x)

x.update(y) 
print(x)

# remove elements: remove(), pop(), clear(), del
x = set(("Milan","Rome","Cosenza"))

x.remove("Milan")  #if you put a values which is not contained in the set, remove() will return an error
x.discard("Rome")  #if you put a values which is not contained in the set, discard() will NOT return an error
x.pop()  #it removes a random elements because they are not ordered

print(x)

x = set(("Milan","Rome","Cosenza"))

del x 

# union of sets: union(), upadate(), intersection_update(), intersection(), symmetric_difference_update(), symmetric_difference() 
x = set(("Milan","Rome","Cosenza"))
y = set(("Turin","Bologna","New York","Rome"))

z = x.union(y) #it creates a new set object (duplicates are not included)
print(z)

x.update(y) # it puts y elements in x (duplicates are not included)
print(x)

x = set(("Milan","Rome","Cosenza"))
y = set(("Turin","Bologna","New York","Rome"))

x.intersection_update(y) # it returns common elements in x and y, it updates an existing set object
print(x)

x = set(("Milan","Rome","Cosenza"))
y = set(("Turin","Bologna","New York","Rome"))

z = x.intersection(y) # it returns common elements in x and y and creates a new set object
print(z)

x = set(("Milan","Rome","Cosenza"))
y = set(("Turin","Bologna","New York","Rome"))

z = x.symmetric_difference(y) # it returns a new set object containing elements in both x and y without common elements
print(z)

x.symmetric_difference_update(y) # it return elements in both x and y without common elements
print(x)

#IMPORTANT: union(), intersection() and symmetric_difference() return a new set object
#           update(), intersection_update() and symmetric_difference_update() update and existing set object

### DATA COLELCTION: DICTIONARIES DICT (16)
# Dictionaries are ordered, editable and duplicates not allowing data collections.
# It a collection of key-value elements

person = { "Name": "Diego", "Cognome": "Fabbri", "Age": 25} # you can duplicate values, keys cannot be duplicated

print(type(person))
print(len(person))

# access dict elements (keys)
print(person["Age"])
print(person.get("Age"))

x = person.keys() # it returns a list with all dict keys
print(x)

x = person.values() # it returns a list with all dict values
print(x)

x = person.items() # it returns a list of key-value tuples for the dict object
print(x)

# verify if a key exists in a dict
print("Name" in person)

# edit elements' valus in a dict
person["Name"] = "Mattew"
print(person)

person.update({"Name": "Andrea"})
print(person)

# add a key in a dict
person["Color"] = "Black" # it creates a new key-value
print(person)

person.update({"Color": "Blue"}) # it updates a key-value object
print(person)

# remove elements in a dict
person = { "Name": "Diego", "Cognome": "Fabbri", "Age": 25}
person.pop("Name") # it removes the input key-value
print(person)

person = { "Name": "Diego", "Cognome": "Fabbri", "Age": 25}
person.popitem() #it removes the last key-value
print(person)

person = { "Name": "Diego", "Cognome": "Fabbri", "Age": 25}
person.clear() #it removes all key-value in a dict making it empty
print(person)

person = { "Name": "Diego", "Cognome": "Fabbri", "Age": 25}
del person["Name"] #it removes input key-value in a dict
print(person)

del person # it removes the object person
#print(person) will return and error

# loops on a dict elements
person = { "Name": "Diego", "Cognome": "Fabbri", "Age": 25}

for x in person: # it returns all dict keys
    print(x)

for x in person.keys(): # it returns all dict keys
    print(x)

for x in person: # it returns all dict values
    print(person[x])

for x in person.values(): # it returns all dict values
    print(x)

for x,y in person.items(): # it returns all dict key-values tuples
    print(x,y)

# create a copy of a dict
x = person.copy() # you can use  x = dict(person)
print(x)

# x = person with this line of code you create a reference, if you edit person also x will be edited

# nested dict
person = { 
    "Name": "Diego", 
    "Cognome": "Fabbri", 
    "Age": 25, 
    "Address" : {
        "City": "Milan",
        "Postal Code": 1234,
        "Street": "My Street"
    }
}
print(person)

# access a nested elements in a dict
print(person["Address"]["City"])

### FUNCTIONS (17)

def my_function():       # create a function
    print("Test print 1")
    print("Test print 2")


my_function() # invoke a custom function

# define input parameters
def my_function(my_parameter):       # create a function with one parameter (you can have multiple parameters)
    print("Test print 1: " + my_parameter)
    print("Test print 2: " + my_parameter)

my_function("input")

## Type of parameters: Arbitrary arguments, Keyword arguments, Arbitrary Keyword arguments (extra content not included)
# Arbitrary arguments: when you do not know how many arguments you have as input

def my_function(*options):
    print("Test print 1: " + options[0])
    print("Test print 2: " + str(options[1]))
    if options[2] == True:
        print("Test print True: " + str(options[2]))
    else:
        print("Test print False: " + str(options[2]))

my_function("Milan", 35, True)

# Keyword arguments: assign a keyword to an input argument
def my_function(parameter_1, bool_flag):
    print("Test print 1: " + parameter_1)
    if bool_flag:
        print("Test print True")
    else:
        print("Test print False")


my_function(parameter_1 = "Hello", bool_flag = True) # when you invoke the custom function you can assign parameters' value

# defaul parameters

def my_function(option = "Default", bool_flag = True): # if you do not pass any parameter, as a defaul it is used the assigned one in function's definition
    print("Test print: " + option)
    if bool_flag:
        print("Test print True")
    else:
        print("Test print False")

my_function()         # uses defaul value
my_function("Custom", False) # uses custom input values

# return values
def make_sum(num_1,num_2):
    sum =  num_1 + num_2
    return sum

x = make_sum(2,5)
print(x)

