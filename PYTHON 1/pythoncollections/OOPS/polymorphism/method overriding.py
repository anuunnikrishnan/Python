class Parent:
    def phone(self):
        print("have nokia 1100")
    def bike(self):
        print("have herohonda")

class Child(Parent):
    def phone(self):
        print("i have a samsung phone")



obj=Child()
obj.phone()
# create object of child class and check phone method is dere in child else look for inheritance from parent
obj.bike()