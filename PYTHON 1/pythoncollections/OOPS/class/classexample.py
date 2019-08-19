# class Person:
#     def welcome(self):
#         print("welcome user")
# obj=Person()
# print(type(obj))
# obj.welcome()
class Student:
    def displayValues(self,name,roll,college):
        self.roll=roll
        self.name=name
        self.college=college
        print("name=",self.name)
        print("roll=",self.roll)
        print("college=",self.college)
obj=Student()
obj1=Student()
obj.displayValues("sachin",1001,"luminar")
obj1.displayValues("anu",1002,"mzc")