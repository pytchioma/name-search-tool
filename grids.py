#Simple Rectangle Grid 

row = 5
cols = 5

for i in range(row):         # First/outer loop: goes through each row
    for j in range(cols):    # Inner loop: goes through each column
        print("*", end="")       # Prints division sign on the same line 
    print()              # move to the next line after finising a row/keeps printing till it reaches the end of the loop


rows = 5
for i in range(1, rows + 1):
    print("" * (rows - i) + "*" * i)