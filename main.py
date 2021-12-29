#LINK al Video Corso: https://www.youtube.com/watch?v=RjhiMjY1nI0&list=PLP5MAKLy8lP8FAytdm2ncZbPioA9A2SgF&index=3&ab_channel=EdoardoMidali


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