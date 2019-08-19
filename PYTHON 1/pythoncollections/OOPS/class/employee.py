class Employee:
    def __init__(self,empid,sal,name):
        self.empid=empid
        self.sal=sal
        self.name=name
    def __str__(self):
        return self.name
# def getEname(emp):
#         return emp.name
# def getsalary(emp):
emp1=Employee(101,1000,"anu")
emp2=Employee(102,2000,"emi")
emp3=Employee(103,3000,"varsha")
emp4=Employee(104,6000,"arya")
lst=[emp1,emp2,emp3,emp4]
# namesorted=sorted(lst,key=getEname,reverse=False)
namesorted=sorted(lst,key=lambda emp:emp.name,reverse=False)
for i in namesorted:
    print(i)
salarysorted=sorted(lst,key=lambda emp:emp.sal,reverse=True)
for i in salarysorted:
    print("person with higher salary:",i)
    break





