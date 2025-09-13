class twoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j")

    
class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show2(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")


p1 = twoDvector(3,4)
p1.show()

p2=threeDvector(3,4,5)
p2.show2()
