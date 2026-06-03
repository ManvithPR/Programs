no=int(input("Enter No:"))
Li=[]
for i in range(no):
    print()
    Li.append([])
    for j in range(int(input("Enter Count "+str(i+1)+":"))):
     Li[i].append(int(input("Enter Salary " +str(i+1)+":")))
print(Li)
    