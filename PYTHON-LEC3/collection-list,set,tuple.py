# Collection=single "variable" use to store multiple value
#    list   =[] ordered and changeable.duplicates Ok
#    set    ={} unordered and immutable,but add/remove OK.NO duplicates
#   tuple   =() ordered and unchangeable.duplicates Ok. FASTER

# list[].

# fruit=["apple","orange","banana","coconut"]

# print(fruit[0:3])
# print(fruit[0::3])
# print(fruit[0::2])
# print(fruit[-1])
# print(fruit[3])

#Reverse all 
# print(fruit[::-1])

# print fruit name in list
# for varible in fruit:
#     print(varible)

# print(dir(fruit))
# print(help(fruit))

# Q.find the lenght
# print(len(fruit))

# True and False
# print("apple" in fruit)
# print("orange" in fruit)
# print("pineapple" in fruit)
# print("banana" in fruit)
# print("coconut" in fruit)
# print("Mango" in fruit)

# Q.change fruit items
# fruit[0]="mango"
# fruit[2]="pineapple"
# or
# fruit.insert(0,"banana")


# fruit wali value me or fruit add kerna ka liya  (append) use kerte ha
# fruit.append("shack")
# fruit.append("radhe")
# fruit.append("papita")

# Remove fruit items
# fruit.remove("coconut")
# fruit.remove("banana")
# print(fruit)

# all fruit name print in a list
# for fr in fruit:
#     print(fr)

# sort=sequence arrange in small to large
# fruit.sort()
# print(fruit)

# reverse all value 
# fruit.reverse()
# print(fruit)

# Clear all items
# fruit.clear()
# print(fruit)

# print(fruit.count("banana"))


# set{}: but duplicate value is not allowed
# if duplicate value is present so value present is only 1 time

# fruit={"apple","orange","banana","coconut","coconut"}

# @heck pineapple present in fruit
# print("pineapple" in fruit)

# @add fruit in set{}
# fruit.add("pineapple")
# print(fruit)

# @ remove some fruit
# fruit.remove("apple")
# print(fruit)

# @
# fruit.pop()
# print(fruit)

#@
# fruit.clear()
# print(fruit)

# print(fruit)

# Tuple():are faster and ordered and unchangeable

fruit=("apple","banana","mango","orange","orange","apple")

# print(dir(fruit))
# print(fruit)
# print(help(fruit))
# print(len(fruit))
# print("pineapple" in fruit)

# @find friut which index
print(fruit.index("apple"))
# print(fruit)

# @count frout items
# print(fruit.count("apple"))
# print(fruit.count("orange"))

# @ print in a list
# for a  in (fruit):
#  print(a)