# multiple inheritance=inherit from  more than one parent class 
#                      c(A,B)

# multilevel inheritance=inherit from a parent which inherit from another parent 
#                        C(B)<-B(A)<-A
# animal class is grand father
# class animal:
#     def eat(self):
#         print("this animal is eating")
    
#     def sleep(self):

#         print("This animal is sleeping") 
# # This classes is a Father
# class prey(animal):
#     def fley(self):
#         print("This animal is fleeing")

# class prerdator(animal):
#     def hunt(self):
#         print("this animal is hunting")

# # This classes is son
# class Rabbit(prey):
#     pass

# class snak(prerdator): 
#     pass
# class Fish(prey,prerdator):
#     pass 


# Rabbit= Rabbit()
# snak=snak()
# Fish=Fish()

# # This funtion call for father
# Rabbit.fley()
# snak.hunt()
# Fish.hunt()
# Fish.fley()

# #this function call for grand father
# Rabbit.eat()
# Rabbit.sleep()
# snak.sleep()
# Fish.sleep()

# or
class animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping") 
# This classes is a Father
class prey(animal):
    def fley(self):
        print(f"{self.name} is fleeing")

class prerdator(animal):
    def hunt(self):
        print(f"{self.name} is hunting")

# This classes is son
class Rabbit(prey):
    pass

class snak(prerdator): 
    pass
class Fish(prey,prerdator):
    pass 


Rabbit= Rabbit("bugs")
snak=snak("Tony")
Fish=Fish("Nemo")

# This funtion call for father
Rabbit.fley()
snak.hunt()
Fish.hunt()
Fish.fley()

print()

#this function call for grand father
Rabbit.eat()
Rabbit.sleep()
snak.sleep()
Fish.sleep()