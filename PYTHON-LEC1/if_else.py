# age=int(input("Enter the age"))

# # 1Case:
# if age>=18:
#     print("you are eligible for job")
# else:
#     print("you are not eligible for job")

# 2Case:
# if age>=60:
#     print("retirement time soon")
# elif age>=18:
#     print("you are eligible for job")
# elif age>=12:
#  print("you are eligible soon for job")
# else:
#     print("you are not eligible for job")

# # 3Case: in which retirement time soon
# if age>=60:
#     print("retirement time soon")
# if age>=18:
#     print("you are eligible for job")
# if age>=12:
#  print("you are eligible soon for job")
# else:
#     print("you are not eligible for job")


# # Q.1

# eligible=input("Are you eligible for job")

# if eligible=="yes":
#  print("you are eligible for job:")
# else:
#  print("You are not eligible for job:")

# #  Q.2
# Name=input("Enter your name")

# if Name=="":
#  print("you did't type your name")
# else: 
#  print(f"hello{Name}")

# # Q.3
# response = True

# if response:
#     print("you are online")
# else:
#  print("you are Offline")

# # Q.4
# objective=True

# if objective:
#    print("wright")
# else:
#    print("wrong")

# # Q.5 python Mine calculater

# operation=input("Enter the operator(+,-,*,/):")
# num1=float(input("enter the 1st number:"))
# num2=float(input("Enter the 2nd number:"))

# if operation == "+":
#     result=num1+num2
#     print(round(result,3))

# elif operation == "-":
#     result=num1-num2
#     p/rint(round(result,3))

# elif operation == "*":
#     result=num1*num2
#     print(round(result,3))

# elif operation == "/":
#     result=num1/num2
#     print(round(result,3))

# else:
#     print(f"Operation is not valid:{operation}")


# # Q.6 python weight converter

Weight=float(input("Enter the weight"))
unit=input("Enter the unit(K&L)")

if unit=="K":
    Weight=Weight*2.205
    unit="Lbs."
    print(f"Your weight is:{round(Weight,1)}{unit}")
elif unit=="L":
    Weight=Weight/2.205
    unit="Lbs."
    print(f"Your weight is:{round(Weight,1)}{unit}")
else:
    print(f"{unit} was not valid")

# # Logical operation

# temp=int(input("Enter the temp"))

# if temp>=0 and temp<=30:
#     print("the temperature is good today!")
#     print("you can go Today")
# elif temp<0 or temp>30:
#     print("The temperature is bad Today")
#     print("You can't go Today outside")


# # Q.find  Temperature 
# unit=input("Enter the value of (C/f)") 
# temp=float(input("Enter the temperature"))


# if unit == "C":
#    temp=round((9*temp)/5+32,1)
#    print(f"The temperature is :{temp} F")
# elif unit == "F":
#     temp=round((temp-32)*5/9,1)
#     print(f"The temperature is :{temp} F")
# else:
#    print("{temp}temp is invalid")    

 
#  Q.
# temp=-3
# is_sunny=False

# if temp>=28 and is_sunny:
#    print("It is Hot outside '🥵")
#    print("It  is sunny'")
# elif temp<=0 and is_sunny:
#    print("It is COLD Outside '🥶")
#    print("Is is Sunny")
# elif 28>temp>0 and is_sunny:
#    print("It is warm outside '🙂")
#    print("It is sunny")
# elif  temp>=28 and not is_sunny:
#    print("It is Hot outside '🥵")
#    print("It  is Cloudy'")
# elif temp<=0 and not is_sunny:
#    print("It is COLD Outside '🥶")
#    print("Is is Cloudy")
# elif 28>temp>0 and not is_sunny:
#    print("It is warm outside '🙂")
#    print("It is Cloudy")