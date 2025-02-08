# conditon expression=A one line shortcut for the if -else statement (Ternary operater )
#                     print or assign one of two values based on a condition
#                     X if condition else Y

num=int(input("Enter the number"))
print("positive" if num>0 else "negative")
print("even" if num%2==0 else "odd")

a=15
b=6
print("A is larg" if a>b else "b is larg")


age=25
status="adult" if age>=18 else "child"
print(status)

temperature=float(input("Enter the temperature"))
weather="Hot" if temperature >20 else "Cold"
print(weather)

status="space"
hotel="Available" if status == "space" else "Sorry  space is not available"
print(hotel)

