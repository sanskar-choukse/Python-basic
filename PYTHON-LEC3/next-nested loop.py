# nested loop=A loop with in another loop (outer,inner)
#            outer loop:
#                inner loop:

# end=""=>same in a 1 line
# end=" "=>same in a 1 line with space
# end="\n"=>next line

# for x in range(1,10):
#     print(x,end=" ")

# for x in range(1,10):
#     print(x,end="")

# for y in range(3):
#   for x in range(1,10):
#     print(x,end="")

# for y in range(3):
#   for x in range(1,10):
#     print(x,end="")
#   print()


# row=int(input("Enter the row"))
# column=int(input("Enter the column"))
# symbol=input("Enter the symbol")
# Q.
# &&&&&
# &&&&&
# &&&&&
# &&&&&
# &&&&&
# for x in range(row):
#     for y in range(column):
#         print(symbol,end="")
#     print()


# Q.
# *
# **
# ***
# for i in range(row):
#     for j in range(i):
#         print(symbol,end="")
#     print()

# Q.
# 0
# 01
# 012
# 0123
# for i in range(row):
#     for j in range(i):
#         print(j,end="")
#     print()

# Q.
# 1
# 22
# 333
# 4444
# for i in range(row):
#     for j in range(i):
#         print(i,end="")
#     print()


# Q.
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# for i in range(row):
#     for j in range(i):
#         print(i-j+1,end="")
#     print()

# Q.
# 000000
# 111111
# 222222
# for i in range(row):
#     for j in range(column):
#         print(i,end="") 
#     print()

# Q.
# 0123
# 0123
# 0123
# for i in range(row):
#     for j in range(column):
#         print(j,end="")
#     print()    

# Q.
# 4321
# 4321
# 4321
# 4321
# for i in range(row):
#     for j in range(column):
#         print(column-j,end="")
#     print() 
 
# Q
# //A A A A
# //B B B B
# //C C C C


# Q.
# //ABC
# //ABC
# //ABC

# Q.
# //ABC
# //DEF
# //GHI

# Q.
# //A
# //BB
# //CCC
# //DDDD

# Q.
# //DDDD
# //CCC
# //BB
# //A

# Q.
# //   *
# //  **
# // ***
# //****