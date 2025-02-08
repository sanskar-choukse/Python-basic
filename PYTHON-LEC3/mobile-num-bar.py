# num_pad=[(1,2,3),
#          (4,5,6),
#          (7,8,9),
#          ("*",0,"#")]

# # double loop ke help se breacket and , duno remove ho gye
# for listed in num_pad:
#     for final_listed in listed:
#       print(final_listed,end=" ")
#     print()

# OR 

Num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))


for number in Num_pad:
  for listed in number:
    print(listed,end=" ")
  print()