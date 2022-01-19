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
