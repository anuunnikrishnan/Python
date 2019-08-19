# 1
# class Number:
#     def add(self,a,b):
#         self.num1 =a
# # assigning values to object(self means)
#         self.num2=b
#         c=a+b
#         print(c)
#
# n=Number()
# n.add(2,3)
# 2.
# class Computer:
#     def __init__(self):
#         self.name="anu"
#         self.age=20
#
# c=Computer()
# c1=Computer()
# c.name="arya"
# print(c.name)
# print(c1.name)
# class Employee:
#     def __init__(self,id,name,sal):
#         self.id=id
#         self.name=name
#         self.sal=sal
#     def __str__(self):
#         return self.name
# emp1=Employee(1,"sanu",5000)
# emp2=Employee(2,"arya",2000)
# emp3=Employee(3,"sai",7000)
# lst=[emp1,emp2,emp3]
# namesorted=sorted(lst,key=lambda x:x.name,reverse=True)
# # namesorted=sorted(lst,key=lambda emp:emp.name,reverse=False)
# for i in namesorted:
#     print(i)
# salarysorted=sorted(lst,key=lambda emp:emp.sal,reverse=True)
# for i in salarysorted:
#     print("highest salaried employee",i)
#     break
#
#
# class Student:
#     def __init__(self,rollno,name,mark):
#         self.rollno=rollno
#         self.name=name
#         self.mark=mark
#     def displayValues(self):
#         print("name",self.name)
#         print("rollno",self.rollno)
#         print("mark",self.mark)
# s=Student(1,"anu",40)
# s.displayValues()

class A:
    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature 2")
class B(A):
    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature 4")

# a=A()
# a.feature1()
# a.feature2()
b=B()
b.feature3()
b.feature4()
b.feature1()