class Employee:
    def __init__(self,eid,ename,esal,edesig):
        self.eid=eid
        self.ename=ename
        self.esal=esal
        self.edesign=edesig
    def __str__(self):
        return self.ename+str(self.esal)
f=open("company.txt")
elist=[]
for val in f:
    lst=(val[:-1].split(","))
    # print(lst)
    # lst=val.split(",")
    # print(lst)
# val[-1] means to avoid /n
    elist.append(Employee (lst[0],lst[1],lst[2],lst[3]))
print("employee sorted based on salary")
namesorted=sorted(elist,key=lambda emp:emp.esal,reverse=True)
for emp in namesorted:
    print(emp)
print("employee with salary greater than 19000")
fname=list(filter(lambda emp:int(emp.esal)>19000,elist))
for emp in fname:
     print(emp)
