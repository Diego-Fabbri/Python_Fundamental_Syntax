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