no=int(input("Enter No:"))
Li=[]
for i in range(no):
     Li.append(int(input("Enter Student " +str(i+1)+":")))
print("Original List:", Li)
Li.sort()
print("Asc order:", Li)
print("Reverse:", sorted(Li,reverse=True))