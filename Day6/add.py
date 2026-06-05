class sample:
    def add(self, datatype,*no):
        if datatype=='int':
            ans=0
        elif datatype=='float':
            ans=0.0
        elif datatype=='string':
            ans=' '
            
        for x in no:
            ans=ans+x
        print(ans)
s=sample()
s.add('int',10,20,30)
s.add('float',10,50,20,20)
s.add('string','This ', 'is ','sample ','text')