# super()=Function used in a child class to call methods from a parent class (superclass).
#         Allows you to extend the functionality of the inherited mathods



# shape class is a  super function
class shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    
    def describe(self):
      print(f"It is a {self.color} color and also {"color_filled" if self.is_filled  else "not filled"}")


class circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

    def describe(self):
     #    super().describe() isliye use kera ke super class ka 
     #    describe function bhi print ho juy 
       super().describe()
       print(f"It is a circle with an area of {3.14*self.radius*self.radius} cm^2")
       
class square(shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width

    def describe(self):
        print(f"It is a square with an area of{self.width*self.width} cm^2")
        super().describe()
        
class Triangle(shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled) 
        self.width=width
        self.height=height
    
    def describe(self):
        print(f"It is a triangle with an area of {self.width*self.height/2} cm^2")
        super().describe()


# circle=circle(color="red",is_filled=True,radius=4) 
# or 
circle=circle("red",True,4) 

# square=square(color="blue",is_filled=True,width=5)
# or
square=square("blue",False,5)

# Triangle=Triangle(color="yellow",is_filled=True,width=5,height=2)
# or
Triangle=Triangle("yellow",True,5,2)


# print(circle.color)
# print(circle.is_filled)
# print(square.color)
# print(square.is_filled)
# print(Triangle.color)
# print(f"{Triangle.height}cm")

# circle.describe()
# Triangle.describe()
# square.describe()


circle.describe()
print()
square.describe()
print()
Triangle.describe()