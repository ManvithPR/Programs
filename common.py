Li1=[1,2,3,4,5,6]
Li2=[1,2,34,5,65,43]
common=[]
for i in Li1:
    if i in Li2:
        common.append(i)
print("common elements", common)