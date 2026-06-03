no=int(input("Enter No:"))
Li=[]
for i in range(no):
    Li.append(input("Enter Student" +str(i+1)+":"))
print(['{}{}{}'.format(i+1,".",name)
       for i, name in enumerate(Li)])

'''for i in range(len(Li)):
   Li[i]=Li[i]+"-"+input("Enter dept of" +Li[i]+":")
print(Li)
na=input("Enter name to search")
if na in Li:
    print("%s is present"%na)
else:
    print("%s is absent"%na)

print(Li[int(input("Enter starting index")):
         int(input("Enter ending index"))])'''

         
