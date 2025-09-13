a = int(input("Enter a number: "))

table = [a*i for i in range(1,11)]

with open("tables.txt", "a") as f:
    f.write(f"Table of {a}: {str(table)}\n")                       #storing in the form of string and adding a new line after every append