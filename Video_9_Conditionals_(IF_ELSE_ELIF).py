### CONDITIONS: IF, ELIF, ELSE (09)
x = 5

# basic syntax of if operator
if x < 10:
    print("x is less than 10")
else:
    print("x is greater than 10")

## Operators to compare
# == equal to
# != different
# < / <= greater than / greater than or equal to
# > / >= less than / less than or equal to

## elif
x = 10

if x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is greater than 10")

## Logical operators: and, or & not
x = 10
y = 5

if x > 10 and x < 20: # both condition have to hold
    print("x is less than 20 and greater than 10")
else:
    print("x is not in [10,20]")

if x == 10 or y == 10: # just one condition has to hold
    print("condition holds")
else:
    print("condition does not hold")

x = 9

if not(x > 10): # it reverses rationale
    print("condition holds")
else:
    print("condition does not hold")

## Short end version of if operator

#Version 1
if x > 10: print("x is greater than 10") # it works only with one statement

#Version 2
# ---- if condition ------------------ | ------- else condition ----
print("x is greater than 10") if x > 10 else print("x is less than 10")

## nested if
x = 9

if x % 2 == 0:
        if x < 10:
            print("x is even")
            print("x is less than 10")
else:
    print("x is odd")