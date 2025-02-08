# Membership operations=used to test wherether a value or variable is found in sequence 
                        # (string,list,Tuple,set or dictionary)
                        # 1.in
                        # 2.not in 

# Q.Find  the letter
# word="Apple"

# Letter=input("Enter the the letter word:")

# if Letter in word:
#   print(f"Letter {Letter} is found")
# else:
#   print(f"letter {Letter} was not found")

# Q.
# word="orange"

# Letter=input("Enter the the letter word:")

# if Letter not in word:
#   print(f"Letter {Letter} was not found")
# else:
#   print(f"letter {Letter} is found")


# Q.find the words(in)

# childreens={"sanskar","Kalu","Mohan","Shyam","Radha"}

# student=input("Enter the student name:")

# if student in childreens:
#     print(f"{student} is present")
# else:
#     print(f"{student} is not present")


# Q.(not in)
# childreens={"sanskar","Kalu","Mohan","Shyam","Radha"}

# student=input("Enter the student name:")

# if student not in childreens:
#     print(f"{student} was not present")
# else:
#     print(f"{student} is present")

# Q.
grades={"Sandy":"A",
        "Squidward":"B",
        "Spongebob":"C",
        "Patrick":"D"}

student=input("Enter the student name:")

if student in grades:
    print(f"{student} is a grade {grades[student]}")
else:
    print(f"{student} was not found")


# Q.
# grades={"Sandy":"A",
#         "Squidward":"B",
#         "Spongebob":"C",
#         "Patrick":"D"}

# student=input("Enter the student name:")

# if student not in grades:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a grade {grades[student]}")

# Q.
# Email="Sanskarchouksey468@gmail.com"

# if "@" in Email and "." in Email:
#     print("Valid email")
# else:
#     print("Invalid email")