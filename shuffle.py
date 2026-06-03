from random import shuffle
no=int(input("Enter No:"))
Li=[]
for i in range(no):
    Li.append(input("Enter Student" +str(i+1)+":"))
shuffle(Li)
print(Li)