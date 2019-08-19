class Emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
         return self.name
obj=Emp("anu",25)
print(obj)
# withount tostring method,print(obj)will print the hexadecimal address(location)