# return=statement used to end a function
#       and send a result back to the caller

# def add(x,y):
#     z=x+y
#     return z
# print(add(8,12))

# def multiply(x,y):
#     z=x*y
#     return z
# print(multiply(2,3))

# def substract(x,y):
#     z=x-y
#     return z
# print(substract(5,8))

# def divide(x,y):
#     z=x/y
#     return z
# print(divide(10,2))


# def create_name(first_name,last_name):
#     first=first_name.capitalize()
#     last=last_name.capitalize()
#     return first+" "+last

# Full_name=create_name("Aayushi","Chouksey")

# print(Full_name)



# or

# def Create_name(first_name,last_name):
#     return first_name+" "+last_name
# Full_name=Create_name("Sanskar","Chouksey")
# print(Full_name)
# or
# print(Create_name("Sanskar","Chouksey"))


# Q
# default arguments = A default value for certain parameters defaultis used 
#                     when that argument is omitted  make your function more flexible,
#                     reduces # of arguments 
#                     1.positional, 2.DEFAULT, 3Keyword, 4.arbitrary

# def net_price(list_price,discount=0,Tax=0.18):
#     return (list_price*(1-discount)*(1+Tax))

# print(net_price(500,0,0.1))
# print(net_price(500,0))
# print(net_price(500))

# 0.1 matlab 10%


# Q=Counting .
# import time
# def count(start,end):
#     for x in range(start,end):
#         print(x)
#         time.sleep(1)
#     print("Done")
# count(1,10)  

# Q
# import time
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
# count(10) 

# Q.just a reversed a value 
# import time 
# def count(start,end):
#     for x in (start,end):
#         print(x)
#         time.sleep(1)
# count(100,1)        

# Q.
# import time
# for x in range(1,10):
#     print(x)
#     time.sleep(1)

