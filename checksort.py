Li=[1,2,3,4,5,6,7]
s=True
for i in range(len(Li)-1):
    if Li[i]>Li[i+1]:
        s=False
        break
print("Sorted?", s)
