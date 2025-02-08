import random

# random.randint
# random.random
# random.choice
# random.shuffle

number=random.randint(0,15)
print(number)

# or
low=0
high=100

number=random.randint(low,high)
print(number)

# print b/w the (0 to 1) range
number=random.random()
print(number)

options=("stone","paper","session")
option=random.choice(options)
print(option)

#sequence distract automatice
cart=["1","2","3","4","5","6","J","Q","N","r"]
random.shuffle(cart)
print(cart)
