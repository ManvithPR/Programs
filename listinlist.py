no=int(input("Enter No:"))
Li=[]
for i in range(no):
     Li.append([input("Enter Student " +str(i+1)+":"),
               input("Enter Dept " +str(i+1)+":"),
               int(input("Enter Salary " +str(i+1)+":"))])
print("Original List:", Li)
print(Li[int(input("Enter row:"))-1])
print(Li[int(input("Enter row:"))-1][int(input("Enter col:"))-1])
print([row[-1]for row in Li])

