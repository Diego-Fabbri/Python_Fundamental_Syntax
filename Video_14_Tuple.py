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