class Person:
    def setPerson(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def displayPerson(self):
        print(self.name+str(self.age)+self.gender)
class Student(Person):
    # student is a person
    school="Luminar"
    def __init__(self,mk1,mk2):
        self.mk1=mk1
        self.mk2=mk2
    def calc(self):
        self.total=self.mk1+self.mk2
        print("total mark is",self.total)
        print("college",Student.school)
st=Student(40,50)
st.setPerson("anu", 25, "f")
st.displayPerson()
st.calc()
