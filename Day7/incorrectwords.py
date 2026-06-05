import time
txt="Python is a dynamic programming language"
st=time.time()
ty=input(f"\n Start typing\n {txt}\n")
et=time.time()
tt=st-et
s=len(txt.split())/(tt/60)
if txt==ty:
    print("Speed:",abs(s),"\nTime taken:",abs(tt))
else:
    print("Incorrect Words")