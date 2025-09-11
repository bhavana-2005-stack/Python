from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("Area of rectangle:",self.length*self.breadth)
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("area of circle:",3.14*self.radius*self.radius)
r1=Rectangle(10,20)
c1=Circle(10)
r1.area()
c1.area()