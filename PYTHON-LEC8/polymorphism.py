# Polymorphism=Greak word that means to "have many forms or faces"
# poly=many
# Morphism=Form

# TWO WAY TO ACHIVE POLYMORPHISM
# 1. Inheritance=An object could be treated of the same type as a parent class
# 2."Duck typing"=object must have necessary attributes/methods

from abc import ABC, abstractmethod

class shape:
  @abstractmethod
  def area(self):
    pass


class circle(shape):
  def __init__(self,radius):
    self.radius=radius

  def area(self):
    return 3.14*self.radius**2

class square(shape):
  def __init__(self,side):
    self.side=side
 
  def area(self):
    return self.side**2

class Triangle(shape):
  def __init__(self,base,height):
    self.base=base
    self.height=height

  def area(self):
    return self.base*self.height*0.5

class pizza(circle):
  def __init__(self,topping,radius):
    self.topping=topping
    super().__init__(radius)

shape=[circle(2),square(5),Triangle(24,6),pizza("pepperoni",15)]

for shapes in shape:
  print(f"{shapes.area()} cm") 