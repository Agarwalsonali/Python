n = int(input("Enter a number: "))

def sum(n):
    if(n==0):
        return 0
    return n + sum(n-1)

s = sum(n)
print(f"The sum of is {s}")