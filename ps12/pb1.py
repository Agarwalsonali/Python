try:
    with open("file1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
    print("File doesn't exist")

try:
    with open("file2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
    print("File doesn't exist")

    
try:
    with open("file3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
    print("File doesn't exist")

    
    