# Inheritance=Allow a class to Inherit attributes and methed from another class 
#             Inheritance allow kerta ha ek class to other class ke leye 
#             Help with code reusability and extensibility
#             class child(parent) 

# Ex-1 
# class Animal:
#     def __init__(self,name):
#         self.name=name
#         self.is_alive=True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class dog(Animal):
#     pass

# class cat(Animal):
#     pass

# class mouse(Animal):
#     pass


# dog1=dog("rocky")
# cat2=cat("pari")
# mouse1=mouse("Mickey")


# print(dog1.name)
# print(cat2.name)
# print(mouse1.name)
# print(dog1.is_alive)

# dog1.eat()
# cat2.sleep()

# Ex-2
class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(Animal):
    def speak(self):
        print("WOOF!")     

class cat(Animal):
    def speak(self):
        print("MEOW") 

class mouse(Animal):
    def speak(self):
        print("SQUEEK")


dog1=dog("rocky")
cat2=cat("pari")
mouse1=mouse("Mickey") 

dog1.speak()
cat2.speak()
mouse1.speak()







