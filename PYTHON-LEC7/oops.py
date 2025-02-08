# object:A "bundle" of related attributed (variable) and methods functions 
#        Ex.Phone,cup,book
#         you need a "class" to create many object 

# class=(blueprint) used to design the structure and layout of an object

class car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color 
        self.for_sale=for_sale 

            
car1=car("fortuner",2024,"white",False)
car2=car("bugatti",2018,"blue",True)
car3=car("BMW",2025,"black",False)
# for print memory address
print(car3)
# for print personal inquery
print(car1.model)
print(car1.color)
print(car1.year)
print(car1.for_sale)
 










