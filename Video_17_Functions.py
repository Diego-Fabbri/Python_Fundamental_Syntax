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