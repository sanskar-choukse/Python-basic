FOOD={"Apple":2.00,
      "mango":3.89,
      "orange":4.3,
      "pineapple":12.0}

cart=[]
Total=0

print("----------MENU---------")
item=FOOD.items()
# print(item)
for keys,values in item:
    print(f"{keys:9}:${values}")
print("------------------------")

while True:
    foods=input("Enter the food items:").lower()
    if foods == "q":
        break
    elif FOOD.get(foods) is not None:
        cart.append(foods)


print("YOUR ORDER")
for foods in cart:
    Total+=FOOD.get(foods)
    print(foods)

print()
print(f"Total is :{Total:.2f}")
