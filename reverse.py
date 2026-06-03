Li=[1,2,3,4,5,6,69]
res=[]
for i in Li:
    res=[i]+res
print("reversed", res)
print("reverse", Li[::-1])