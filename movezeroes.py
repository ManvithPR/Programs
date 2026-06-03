Li=[1,2,0,3,4,5,0,6,0,69]
res=[]
for i in Li:
    if i !=0:
        res.append(i)
while len(res)<len(Li):
    res.append(0)
    
print("Original list", Li)
print("Zeroes at end:", res)