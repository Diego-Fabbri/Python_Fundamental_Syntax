### STRING FORMATTING (ADVANCED)

weight = 65
height = 170
statement = "I'm " + str(height) + " cm tall"

print(statement)

statement = "I'm {} cm tall my weight is: {}" # use string formatting
print(statement.format(height,weight))

statement = "I'm {:.2f} cm tall my weight is: {:.2f}" # use string formatting with 2 figures for decimal numbers
print(statement.format(height,weight))                # you have to keep the correct order for input parameters unless you use index

# use index
statement = "I'm {1:.2f} cm tall my weight is: {0:.2f}" # use string formatting with 2 figures for decimal numbers and indexes
print(statement.format(weight,height))

# to avoid confusion you can use NAMED INDEX
statement = "I'm {height} cm tall my weight is: {weight}" # use string formatting with 2 figures for decimal numbers and indexes
print(statement.format(weight = 99,height = 200))