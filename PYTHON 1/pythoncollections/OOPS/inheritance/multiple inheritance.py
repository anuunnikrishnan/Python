# class One:
#     def m1(self):
#         print("inside class one")
# class Two(One):
#     def m2(self):
#         print("inside class two")
# class Three(Two,One):
#     def m3(self):
#         print("inside class three")
# obj=Three()
# obj.m3()
# obj.m2()
# obj.m1()

class One:
    def m1(self):
        print("inside class one")
class Two(One):
    def m1(self):
        print("inside class two")
class Three(Two,One):
# here m1 method is in two classes..working based on the order of passing the arguments (two,one)so m1 method in class 2 is workingh
    def m3(self):
        print("inside class three")
obj=Three()
obj.m3()
obj.m1()