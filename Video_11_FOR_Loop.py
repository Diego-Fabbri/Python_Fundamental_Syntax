### LOOPS: FOR (11)

list_of_cities = ["Milan","Rome","Cosenza"] # list
string = "letter" #using strings

for city in list_of_cities:
    print(city)

for c in string:
    print(c)

for x in range(6):  # using range()
    print(x)

# else: it works at the end of for loop
for x in range(6):  
    print(x)
else:
    print("end of for loop")


# break: it stops for loop iterations
for x in range(6):  
    if x==3:
        print("For loop iterations stopped")
        break      
    print(x)

# continue: it skips for loop iterations
for x in range(6):  
    if x == 3:
        print("For loop iteration skipped")
        continue      
    print(x)
