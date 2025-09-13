class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

    
p1 = Programmer("Harry", 1200000, 245001)
print(p1.name, p1.salary, p1.pincode, p1.company)

p2 = Programmer("Rohan", 1500000, 324011)
print(p2.name, p2.salary, p2.pincode, p2.company)
        
        