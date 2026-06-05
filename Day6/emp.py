class emp:
    def empmeth(self):
        print("from emp class ")
class Manager(emp):
    def managermeth(self):
        print("From manager class")
        
class Project(emp,Manager):
    def projmeth(self):
        print("from project class")
m=Manager()
m.empmeth()
m.managermeth()
m.projmeth()