n=int(input("Enter No:"))
for i in range(n): #O(n)-time complexity
    num=i
    c=0
    while num>1: #O(log n)-time complexity
        c=c+1
        num=num/2
        print("Step:",c,"->",num)