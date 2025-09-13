username = input("Enter the username: ")
length = len(username)

if(length<10):
    print("Username contains less than 10 characters.")
else:
    print("Username contain more than or equal to 10 characters.")