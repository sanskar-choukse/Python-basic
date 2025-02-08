#Exercise 1:Area of rectangular
length=int(input("Enter the length"))
width=int(input("Enter the width"))
area = length * width
print(f"area of rectangular {area}")

#Exercise 2:shopping card

item=input("what item would you like")
price =float(input("what is the price"))
quantity=int(input("how many would you like"))
total=quantity * price


print(f"you have bought {quantity} x {item}/s")
print(f"total price${total}")


# Exercise3

#madlibs game
# word game where you create a story
# by filling in blanks with random works
 

adjective1=input("Enter an adjective")
adjective2=input("enter a noun (persin,place,thing)")
adjective3=input("enter the  adjective")
verb=input("enter a verb with ('ing')")
noun1=input("enter the noun")

print(f"today i went to a {adjective1} zoo.")
print(f"In an exhibit,I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb}")
print(f"I was {adjective3}!")