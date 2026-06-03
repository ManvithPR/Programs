no=int(input("Enter No:"))
Li=[]
for i in range(no):
     Li.append(input("Enter Student " +str(i+1)+":"))
print("Original List:", Li)
print("String FOrmat", "".join(map(str,Li)))