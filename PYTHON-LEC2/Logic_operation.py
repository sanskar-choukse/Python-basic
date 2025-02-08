# Logical operation(and,or,not)me symbal ka use nahi hota ha direct and ,or ,not
# likha tha ha


# Q=>using and /or related
temp=int(input("Enter the temp"))

if temp>=0 and temp<=30:
    print("the temperature is good today!")
    print("you can go Today")
elif temp<0 or temp>30:
    print("The temperature is bad Today")
    print("You can't go Today outside")

# Q.Related using Not gate 

temp=int(input("Enter the temp")) 

if not(temp>=0 and temp<=30):
    print("the temperature is good today!")
    print("you can go Today")
elif not (temp<0 or temp>30):
    print("The temperature is bad Today")
    print("You can't go Today outside")


#  Q.
temp=-3
is_sunny=False

if temp>=28 and is_sunny:
   print("It is Hot outside '🥵")
   print("It  is sunny'")
elif temp<=0 and is_sunny:
   print("It is COLD Outside '🥶")
   print("Is is Sunny")
elif 28>temp>0 and is_sunny:
   print("It is warm outside '🙂")
   print("It is sunny")
if temp>=28 and not is_sunny:
   print("It is Hot outside '🥵")
   print("It  is Cloudy'")
elif temp<=0 and not is_sunny:
   print("It is COLD Outside '🥶")
   print("Is is Cloudy")
elif 28>temp>0 and not is_sunny:
   print("It is warm outside '🙂")
   print("It is Cloudy")
