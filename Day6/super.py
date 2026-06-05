'''class supermarket:
    def__init__(self):
        print("Default constructor")
    def input(self):
        self.no=int(input("Enter no:"))
    def display(self):
        for i in range(self.no):
            print(i, end=" ")
s=supermarket()
s.input()'''


class supermarket:
    def __init__(self):
        print("ABC super market")
        
    def product(self,pname,qty,price):
        print("Product",pname)
        print("Total,qty,")