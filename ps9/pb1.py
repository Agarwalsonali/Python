f = open("poems.txt","r")
data = f.read()
print(data)
print("")
if("twinkle" in data):
    print("The word twinkle is present in the data.")
else:
    print("The word twinkle is not present in the data.")
f.close()
