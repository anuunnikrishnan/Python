class Circle:
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self,radius):
        self.p=2*3.14*self.radius
    def area(self,radius):
        self.a=3.14*self.radius*self.radius;
    def display(self):
        print("Perimeter of the circle is", self.p)
        print("Area of the circle is",self.a)
c=Circle(5)
c.perimeter(5)
c.area(5)
c.display()