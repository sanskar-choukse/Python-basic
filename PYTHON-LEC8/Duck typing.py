# "Duck typing"= Another way to achive polymorphism besides inheritance 
#                object must have the minimum necessary attributes/methods
#                "if it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive=True

class dog(Animal):
    def speak(self):
        print("WOOF!")

class cat(Animal):
    def speak(self):
        print("MEOW!")

class car:
    alive=False

    def speak(self):
        print("HORN!")

Animal=[dog(),cat(),car()]     
   

for Animals in Animal:
    Animals.speak()  
    print(Animals.alive)