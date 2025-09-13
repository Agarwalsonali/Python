def func():    
    a=int(input("Enter number 1: "))
    b=int(input("Enter number 2: "))
    c=int(input("Enter number 3: "))

    if(a>b and a>c):
        print(f"The greatest number is {a}")
    elif(b>a and b>c):
        print(f"The greatest number is {b}")
    else:
        print(f"The greatest number is {c}")


func()