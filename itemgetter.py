from itertools import groupby
from operator import itemgetter
no=int(input("Enter the number of students: "))
Li=[]
for i in range(no):
    Li.append(input("Enter the name: "))
print(Li,end=" ")

for let,na in groupby(sorted(Li),key=itemgetter(0)):
    print("\n",let)
    for n in na:
        print(n)