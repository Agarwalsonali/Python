list = ["hi", "hello", "namaste", "good", "good night"]

word = input("Enter the word you want to remove: ")

def func(word):
    n=[]                #empty list
    for item in list:
        if not(item==word):
            n.append(item.strip(word))
        
    return n
        
            

print(func(word))