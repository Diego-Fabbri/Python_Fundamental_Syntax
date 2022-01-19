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