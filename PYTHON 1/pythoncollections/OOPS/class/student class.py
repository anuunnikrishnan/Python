class Student:

    def setValues(self,rollno,name,college):
        self.rollno=rollno
        self.name=name
        self.college=college
    def displayValues(self):
        print("rollno",self.rollno)
        print("name",self.name)
        print("college",self.college)
obj=Student()
obj.setValues(101,"anu","luminar")
obj.displayValues()


