class Ex:
    a = 5

n = Ex()
print(n.a)

n.a = 0
print(n.a)   

print(Ex.a)          # Output = No it will not change the class attribute.