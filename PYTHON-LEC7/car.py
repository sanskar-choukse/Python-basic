class car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color 
        self.for_sale=for_sale 

    def drive(self):
       print(f"you drive the {self.color} {self.model}")


    def stop(self):
       print(f"you stop the {self.color}  {self.model}")

    def describe(self):
        print(f"{self.model} {self.year} {self.color} {self.for_sale}")

car1=car("Fortuner",2025,"Black","False")

print(car1.model)