# default constructor
# class Student:
#     schoolname="Luminar"
#     def __init__(self):
#         print("hai constructor")
# obj=Student()
# object with parameters
class Student:
    schoolnmae="Luminar"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("name=",self.name)
        print("roll=",self.roll)
    def __str__(self):
        # return self.name
        return self.name+str(self.roll)

obj=Student("anu",101)
obj.display()
print(obj)+