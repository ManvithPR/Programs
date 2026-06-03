'''Li1=[1,2,3,4,5,6]
Li2=[6,7,8,9,0,2]
print(sorted(set(Li1+Li2)))'''

#max profuct pair
'''Li1=[1,3,5,7,9]
Li1.sort()
print("Max pro pair :",Li1[-1]*Li1[-2])'''


#split list
'''Li=[1,2,3,4,5,6,7,8,9,10,11,12,13]
size=int(input("Enter size"))
for i in range(0,len(Li),size):
    print(Li[i:i+size])'''
    
    
#swap alternate
Li=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(len(Li)//2):
    if i%2==1:
        Li[-(i+1)],Li[i]=Li[i],Li[-(i+1)]
print(Li)