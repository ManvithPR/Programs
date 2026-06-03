# Counter function to compare two List elements
from collections import Counter

n = int(input("Enter Number of Employee to Process: "))
namelist=[]
for i in range(n):
    Li = input("Enter Name " + str(i+1)+ " : ")
    namelist.append(Li)

print("Name List are : " , namelist)

PreList=[]
CurrList=[]

for i in range(0,len(namelist)):
    print()
    name=namelist[i]

    newvar=input("Enter Previous month Salary to " + str(name)+ " : ")
    x=[name,newvar]
    PreList.append(x)
    
    newvar=input("Enter Current month Salary to " + str(name) + " : ")
    x=[name,newvar]
    CurrList.append(x)
 

print("\nEmployee Status Report:")
print("\nEmployee Name Previous Salary List:" ,PreList)
print("\nEmployee Name Current Salary List:" ,CurrList)

print()

for i in range(n):
    print("Same Salary to " + PreList[i][0] + " ? ", Counter(PreList[i]) == Counter(CurrList[i]))
