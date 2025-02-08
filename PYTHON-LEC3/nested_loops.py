# nested loop=The "inner loop" will  finesh all of it's iteration before
#              finishing one  iteration of the "Outer loop"


# Q.
# ******
# ******
# ******
# rows=int(input("Enter the rows"))
# columns=int(input("Enter the columns"))
# symblos=input("Enter the symbols")

# for i in range(rows):
#     for j in range(columns):
#         print(symblos, end="")
#     print()

# Q.
# ******
# ******
# ******
# rows=int(input("Enter the row"))
# columns=int(input("Enter the value"))

# for i in range(rows):
#     for j in range(columns):
#       print("*",end="")
#     print()



# Q.*
#   **
#   ***

# rows=int(input("Enter the row"))
# columns=int(input("Enter the value"))

# for i in range(rows):
#     for j in range(i):
#       print("*",end="")
#     print()

# Q.
# *****
# ****
# ***
# **
# *

# rows=int(input("Enter the row"))
# columns=int(input("Enter the value"))

# for i in range(rows):
#     for j in range(rows-i):
#       print("*",end="")
#     print()


for x in range(3):
   for j in range(1,10):
      print(j,end="")
   print()