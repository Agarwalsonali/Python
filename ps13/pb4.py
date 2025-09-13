l = [2,4,5,10,15,89,20]

def func(n):
    if(n%5 == 0):
        return True
    return False


f = list(filter(func, l))

print(f)

