class Student:
    schoolname="Luminar"
    def setValues(self,rollno,name,mark1,mark2,mark3):
        self.rollno=rollno
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def displayValues(self):
        print("student name",self.name)
        print("rolno",self.rollno)
        print("mark1",self.mark1)
        print("mark2",self.mark2)
        print("mark3",self.mark3)
        print(Student.schoolname)
    def average(self,mark1,mark2,mark3):
        avg=(mark1+mark2+mark3)/3
        print("average mark is",avg)
        # print(type(Student.schoolname))
obj=Student()
obj.setValues(1,"anu",30,40,50)
obj.displayValues()
obj.average(30,40,50)
