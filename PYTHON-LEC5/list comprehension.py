# List comprehension=a concise way to create list in python to 
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# double=[]
# for x in range (1,11):
#     double.append(x*2)
# print(double)

# or
 
# Q.
# double=[x*2 for x in range (1,11)]
# triple=[y*3 for y in range (1,11)]
# square=[z*z for z in range (1,11)]
# print(square) 

# Q.All names in capitals
# fruits=["apple","orange","banana","coconut"]
# fruits=[fruit.upper() for fruit in fruits]
# print(fruits)

# or
# fruits=[fruit.upper() for fruit in ["apple","orange","banana","coconut"]]
# print(fruits)

# or
# Q.
fruits=["apple","orange","banana","coconut"]
fruits=[fruit[0] for fruit in fruits]
print(fruits)

# print a positive number
# number=[1,-2,-3,-5,-8,9,4]
# positive_num=[x for x in number if x>= 0]
# negative_num=[y for y in number if y<=0]
# even =[evens for evens in number if evens%2==0]
# odd=[odds for odds in number if odds%2==1]
# evenandpositive=[even for even in number if even%2==0 and even>=0]
# oddandnegative=[odd for odd in number if odd%2==1 and odd<=0]
# print(positive_num)
# print(negative_num)
# print(even)
# print(odd)
# print(evenandpositive)
# print(oddandnegative)

# grade=[33,45,55,67,60,65,23,98,99,100]
# passing_grades=[grades for grades in grade if grades>=60]
# print(passing_grades)

# or
# passing_grades=[grades for grades in [33,45,55,67,60,65,23,98,99,100] if grades>=60]
# print(passing_grades)