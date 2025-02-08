# shoping card
foods=[]
prices=[]
total=0

while True:
   food=input("Enter the food to buy:")
   if food.upper()=="OK":
    break
   else:
       price=float(input(f"Enter the prices to {food}:$"))
       foods.append(food)
       prices.append(price)


print("-----YOUR CART -----")

for food in foods:
  print(food,end=" ")

print()

for price in prices:
   total+=price
   print(f"YOUR Total is :{total}")