# Type of methods
# 1.class method
# 2.instance method
# 3.static method
class Student:
    school="Luminar Technologies"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        # instance method
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    # class method
    @classmethod
    def info(cls):
        cls.school="techno lab"
        print(cls.school)
        # staticmethod
    @staticmethod
    def staticMeth():
        print("hello")
s1=Student(50,40,30)
print(s1.avg())
s2=Student(10,20,30)
print(s2.avg())
Student.info()
Student.staticMeth()