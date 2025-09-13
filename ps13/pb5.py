from functools import reduce

l = [4, 8, 76, 178, 172, 54]

def greater(a,b):
    if(a>b):
        return a
    return b


val = reduce(greater, l)

print(val)

