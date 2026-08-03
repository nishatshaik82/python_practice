#create a shape class and drive circle and rectangle
class Shape:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def display_info(self):
        print("Color:", self.color)
        print("Size:", self.size)

class Circle(Shape):
    def display_info(self):
        print("Circle Color:", self.color)
        print("Radius:", self.size)

class Rectangle(Shape):
    def display_info(self):
        print("Rectangle Color:", self.color)
        print("Length:", self.size)

circle = Circle("Red", 7)
rectangle = Rectangle("Blue", 12)

circle.display_info()
rectangle.display_info()