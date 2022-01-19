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