'''Li=[30,10,20,30,40,35,20,68,67,30,20,20,10,20,30,40,35]
dup=[]
for i in Li:
    print(i,"-", Li.count(i))
    if Li.count(i)>1 and i not in dup:
        dup.append(i)
print("Original elements are: ", Li)
print("Duplicate elements are: ", dup)'''


Li=[1,2,2,3,5,4,4]
dup=[]
for i in Li:
    if i not in dup:
        dup.append(i)
print(dup)
