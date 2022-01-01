#LINK al Video Corso:
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