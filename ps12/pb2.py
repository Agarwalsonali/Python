list = ["Alice", "Samarth", 18, 8, 15, "Orange", "Mango", "Ben"]

for i, item in enumerate(list):
    if(i==2 or i==4 or i==6):                           # 0- indexing
        print(f"The element at index {i} is {item}")