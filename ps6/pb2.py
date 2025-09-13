marks1 = int(input("Enter first subject marks: "))
marks2 = int(input("Enter second subject marks: "))
marks3 = int(input("Enter third subject marks: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(marks1>=33 and marks2>=33 and marks3>=33 and total_percentage>=40):
    print("Passed",total_percentage)
else:
    print("Failed",total_percentage)


