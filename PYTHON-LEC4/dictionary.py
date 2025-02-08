# dictionary=a collection of {Key:value} pairs
#            ordered and changeable.no duplicates

Capitals={"India":"new delhi",
          "USA":"Washington D.C",
          "China":"bejing",
          "Russia":"Moscow"}

# print(dir(Capitals))
# print(help(Capitals))
# print(Capitals.get("India"))
# print(Capitals.get("China"))
# print(Capitals.get("Russia"))
# print(Capitals.get("USA"))

# if Capitals.get("china"):
#     print("This capital exist")
# else:
#     print("This capital does't exist")

# @for add new capitals
# Capitals.update({"srilanka":"shriram"})


# @for update variable value
# Capitals.update({"USA":"shriram"})

# @for delete variable value
# Capitals.pop("China")

# @for  variable value
# Capitals.popitem() 

# all clear
# Capitals.clear()
# print(Capitals)

# key=Capitals.keys()
# print(key)
# or
# for key in Capitals.keys():
#     print(key)

# values=Capitals.values()
# print(values)
# or
# for values in values:
#     print(values)

# items which explain a proper in breacket(),(),()
items=Capitals.items()
# # print(items)
# # or
# for items i n items:
    # print(items)
    # or without '#'ke 
for key,value in  items:
    print(f"{key}:{value}")


# or
# Example=2
post={"sanskar":"Senior-datascience",
      "Aayushi":"senior research-Assocative",
      "shubh":"senior data Analysis",
      "sujal":"senior_web-developer"}



print(post.get("sanskar"))
print(post.get("Aayushi"))
print(post.get("shubh"))
print(post.get("sujal"))


if post.get("sanskar"):
    print("This employess is here")
else:
    print("this employess not here")

post.update({"vadansh":"software_engineer"})
print(post)

post.update({"vadansh":"senior_software_engineer"})
print(post)

# /pop => means delete
post.pop("Aayushi")
print(post)

post.popitem()
print(post)

post.clear()
print(post)

key=post.keys()
print(key)

value=post.values()
print(value)
# or
for value in value:
    print(value)

items=post.items()
print(items)
# or
for key,value in items:
    print(f"{key:7} : {value}")