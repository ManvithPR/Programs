import time
s=time.time()
print(s)
for i in range(1,100):
    print(i,end=" ")
e=time.time()
f=(s-e)
print("\nFinal Time:",abs(f))