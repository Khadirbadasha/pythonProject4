#Polymorphism - objected -oriented programming(oop)
class Shape:
    def area(self):
        print("Area of shape")
class Rectangle(Shape):
    def __init__(self,legth,width):
        self.legth = legth
        self.width = width
    def area(self):
        return self.legth*self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
shape1 =Rectangle(3,4)
print(shape1.area())
shape2 = Circle(10)
print(shape2.area())
shape3 =Shape()
shape3.area()
