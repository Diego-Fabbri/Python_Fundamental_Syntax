### TRY and Except

# Sometimes code chunks might generate errors:
# - try allows you to test a code chunk,
# - except allows you to catch the potential error generated in try, 
# - finally executes a code chunk after try and except
## check error types in the following documentation: https://docs.python.org/3/library/exceptions.html

x = 5
print(x) # No Error

# print(y) #Generates and error (y is not defined)
try:
    print(y)
except:
    print("You got an ERROR !")
    # pass                            # skips this line of code and the compiler does nothing

## manage multiple type of errors
try:
    print(y)
except NameError:  # define what to do if a specific error occurs (NameError is a specific kind of error)
    print("You got an NAME ERROR !")
except:
    print("You got an ERROR !") # define what to do if another kind of error occurs

## Get the name of the exeption you get (Version 1)
y = 55
try:
    print(y + "Hello")
except NameError:  # define what to do if a specific error occurs
    print("You got an NAME ERROR !")
except Exception as e: # define what to do if another kind of error occurs
    print(e)           # - print a message with the kind of error
   # print("You got an ERROR Sir!") 


## Get the name of the exeption you get (Version 2)

y = 74
try:
    print(y + "Hello")
except NameError:  # define what to do if a specific error occurs
    print("You got an NAME ERROR !")
except Exception as e: # define what to do if another kind of error occurs
    print(e)           # - print a message with the kind of error
   # print("You got an ERROR Sir!") 

import traceback # Use this module to trace the exception

try:
    1/0
except Exception:
    traceback.print_exc()


## If an error does not occur
y = 55
try:
    print(y)
except NameError:  # define what to do if a specific error occurs 
    print("You got an NAME ERROR !")
except Exception as e: # define what to do if another kind of error occurs
    print(e)           # - print a message with the kind of error
    print("You got an ERROR Sir!") 
else:      # if an error does not occur else works otherwise it does not
    print("No Error Occurred")

## If an error does not occur
y = 55
try:
    print(y+"Hello")
except NameError:  # define what to do if a specific error occurs 
    print("You got an NAME ERROR !")
except Exception as e: # define what to do if another kind of error occurs
    print(e)           # - print a message with the kind of error
    print("You got an ERROR Sir!") 
finally:              # finally works independently of the ERROR occurrence
    print("I always work even if the error occurs")

## How to raise an exeption (programmers use this function to test their programming code)

x = -1

if x < 0:
    raise Exception(" Negative number")  # here the code will stop working

print("This print will not be given in console")

