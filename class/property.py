#property decorator use to define a method as a property it can be accessed like as attribute
# benefit add addition logic with read ,write,or delete attribute
# give you getter,setter and deleted method
class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            return "Width must be positive"
    @height.setter  
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            return "Height must be positive"
    

    @width.deleter
    def width(self):
        del self._width
        print("width as been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("height as been deleted")
            
        

rectangle= Rectangle(10,5)
rectangle.width=10  # Setting new width
rectangle.height=12  # Setting new height
print(rectangle._width) # Accessing width as a property
print(rectangle._height)
del rectangle.width  # Deleting width property
del rectangle.height  # Deleting height property