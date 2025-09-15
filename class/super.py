#super()=function used in a child class to call method from a parent class {super(class)}
#  allows you to extend the functionality of the inherited method


class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    def describe(self):
        print(f"it is {self.color}  and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color, is_filled)  # Call the parent class constructor
        self.radius=radius
    def describe(self):
        print(f"it is a circle with area {3.14 * self.radius ** 2} cm²")
        super().describe()  # Call the parent class describe method
class Square(Shape):
    #class Square inherits from Shape
    def __init__(self,color,is_filled,width):
        super().__init__(color, is_filled)
        self.width=width
    def describe(self):
        print("it is a square with area", self.width ** 2, "cm²")
        super().describe()
class Triangle(Shape):
    def __init__(self,color,is_filled,height,width):
        super().__init__(color, is_filled)
        self.height=height
        self.width=width
    def describe(self):
        print("it is a triangle with area", 0.5 * self.height * self.width, "cm²")
        super().describe()


print('*******************')
circle=Circle(color="red",is_filled=True,radius=5)
square=Square(color="blue",is_filled=False,width=10)
triangle=Triangle(color="green",is_filled=True,height=8,width=6)

circle.describe()