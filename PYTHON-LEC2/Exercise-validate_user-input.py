# validate user input exercise
# 1.username is no more than 12 character
# 2.username must not contain space
# 3.username must not contant digit

username=input("Enter the name:")

if len(username)>12:
    print("your username can't be content 12 char")
elif not username.find(" ")==-1:
    print("your username can't content space")
elif not username.isalpha():   
    print("your username can 't content alpha") 
else:
    print("Most Welcome")    