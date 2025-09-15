#polymorphism=greek word meaning to"have many form or faces"""#poly = many, morph = form"""
class shape:
    def area(self):
        pass
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
class Triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class pizza(Circle):
    def __init__(self, topping,radius):
        self.radius = radius
        self.topping = topping


shapes=[Circle(4), square(5),Triangle(3, 6),pizza("pepperoni", 15)]
for shape in shapes:
    print("area of shape is", shape.area())

