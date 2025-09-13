# def func(n):
#     for i in range(1,n+1):
#         print("*"*((n+1)-i))

# func(3)

# Recursion method
def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)

pattern(3)