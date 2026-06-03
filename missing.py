Li=[1,2,3,4,5,7,8,9]
expected=Li[-1]*(Li[-1]+1)//2
actual=sum(Li)
print("missing no", abs(actual-expected))

