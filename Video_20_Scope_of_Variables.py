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