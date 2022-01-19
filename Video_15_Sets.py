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