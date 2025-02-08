# *args   = allows you to pass multiple non-key arguments
# **Kwargs=allows you to pass multiple keyward arguments
#          *unpacking operator 
#           1.positional 2.default 3.Keyword 4.ARBITRATY

######*args######
# def add(*args):
#     total=0
#     for arg in args:
#       total+=arg
#     return total

# print(add(1,3,2,5,8,89))    


# def numbers(*num):
#     total=0
#     for nums in num:
#         total+=nums
#     print(total)

# numbers(1,2,3,4,5)


# Q.
# def display_name(*name):
#     for names in name:
#         print(names)

# display_name("Dr.Sanskar chouoksey","104 karas dev nager indore (M.P)","Pin Code=452010")       

# Q
# def display_firecrakers(*name):
#     for firecrakers in name:
#         print(firecrakers,end="")
          
# display_firecrakers("Anil","asdsf","dda")
# display_firecrakers("Anil","asdsf","dda")

####**Kwargs######3
# @Q# **Kwargs=allows you to pass multiple keyward arguments
            # which is :keys,value,items
#              *unpacking operator 
#              1.positional 2.default 3.Keyword 4.ARBITRATY

# def print_address(**kwargs):
#     for key,value in kwargs.items():
#       print(f"{key}:{value}")

# print_address(Street="123",city="Indore")

# @Q.
# def print_address(**kwargs):
    # for key,value in kwargs.items():
    #   print(f"{key}:{value}")

# print_address(Street="123",
#               city="Indore",
#               Pin_code="452010",
#               state="Madhya pradesh")

# ##### **kwargs,**args ######
# def print_address(*args,**kwargs):
#     for name in args:
#       print(name,end=" ")
#     print()
#     for key,value in kwargs.items():
#       print(f"{key}:{value}")
       
# print_address("Dr.","Sanskar","Chouksey",
#               Street="123",
#               city="Indore",
#               Pin_code="452010",
#               state="Madhya pradesh")

# or
def print_address(*args,**kwargs):
    for name in args:
      print(name,end=" ")
    print()
    for key in kwargs.keys():
      print(f"{key}:")
    print()
    # or
    print(kwargs.get("city"))
    # or 
    print(kwargs.get("Street")) 
    # or
    print(f"{kwargs.get("pin_code")} {kwargs.get("State")}")   

print_address("Dr.","Sanskar","Chouksey",
              Street="123",
              city="Indore",
              Pin_code="452010",
              state="Madhya pradesh")


# or
# def print_address(*args,**kwargs):
#     for name in args:
#       print(name,end=" ")
#     print()
#     # for key in kwargs.keys():
#     #   print(f"{key}:")
#     # print()

#     if "Street" in kwargs:
#         print(f"{kwargs.get("pin_code")} {kwargs.get("State")}")   
#     else:
#        print(kwargs.get("city"))
# #     # or
# #     print(kwargs.get("city"))
# #     # or 
# #     print(kwargs.get("Street")) 
# #     # or
# #     print(f"{kwargs.get("pin_code")} {kwargs.get("State")}")   

# print_address("Dr.","Sanskar","Chouksey",
#               Street="123",
#               city="Indore",
#               Pin_code="452010",
#               state="Madhya pradesh")
