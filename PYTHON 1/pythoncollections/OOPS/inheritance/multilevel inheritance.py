class One:
    def m1(self):
        print("inside class one")
class Two(One):
    def m2(self):
        print("inside class two")
class Three(Two):
    def m3(self):
        print("inside class three")
obj=Three()
obj.m3()
obj.m2()
obj.m1()