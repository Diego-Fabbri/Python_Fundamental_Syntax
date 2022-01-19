### LOOPS: WHILE (10)

x = ["Rome","Milan","Cosenza"] 

# basic syntax of while loop
i = 0
while i < 6: # until condition holds loop works
    print(i)
    i = i + 1

# break: it stops loop's execution
i = 0
while i < 6: # until condition holds loop works
    print(i)
    if i == 3:
     print("break loop")   
     break
    i = i + 1

# continue: it skips to the next loop's iteration
i = 0
while i < 6: # until condition holds loop works
    i = i + 1
    if i == 3:
     print("continue loop, iteration skipped")   
     continue
    else:
        print(i)

# else: it work at the end of while loop's iterations
i = 0
while i < 6:
    print(i)
    i = i + 1
else:
    print("end of while loop")