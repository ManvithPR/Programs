from collections import Counter
no=int(input("Enter No:"))
Li=[]
for i in range(no):
    Li.append(input("Enter Student" +str(i+1)+":"))
print(Li)
newLi=[]
for i in range(no):
    newLi.append(input("Enter Student" +str(i+1)+":"))
print(newLi)
print(Counter(Li)-Counter(newLi))
