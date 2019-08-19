
# low=int(input("enter the range"))
# upp=int(input("enter upper range"))
# while(low<upp):
#     low=low+1
#     i=low+1
#     print(i)

class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        avg=(self.m1+self.m2+self.m3)/3
        print(avg)
s=Student()
s.avg(20,30,40)
























































