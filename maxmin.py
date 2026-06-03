no=int(input("Enter No:"))
Li=[]
for i in range(no):
    print()
    Li.append([])
    for j in range(int(input("Enter Count "+str(i+1)+":"))):
     Li[i].append(int(input("Enter Salary " +str(i+1)+":")))
print(Li)
print("Max salary", max(Li,key=sum))
print("Min salary", min(Li,key=sum))
print("Max count salary", max(Li,key=len))

