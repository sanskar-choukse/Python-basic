# @property=Decorator used to define a method as a property(It can be accessed like an attribute)
#          benefit:add additional logic when read,write, or delete  attributes 
#          gives you getter,setter,and deleter method

class rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return f"{self._width:.2f}cm"

    @property
    def height(self):
        return f"{self._height:.2f}cm"

    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("width must be greater thna zero")

    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height = new_height
        else:
            print("Height must be greater thna zero")
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

# rectangle=rectangle(3,4)
# or
rectangle.width=-1
rectangle.height=-4
 

# for this class
# print(rectangle._width)
# print(rectangle._height)

# for this function
print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height