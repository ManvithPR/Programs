usn=[i for i in range (1, int(input("Enter No:"))+1)]
print(usn)
print(["NNM23EC0"+str(no)
       for i,no in enumerate(usn)if no %2==1])