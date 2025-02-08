# # Python number guessing game
import random


lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
# print(answer)

guesses=0
is_running=True

print("Python number guessing game")
print(f"Select a number b/w {lowest_num}to{highest_num}")

while is_running:
    guess=input("Enter you guess")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1
        if guess<lowest_num or guess> highest_num:
            print("This number is out of range")
            print(f"Select a number b/w {lowest_num}to{highest_num}")
        elif guess<answer:
            print("Too low !try again")
        elif guess>answer:
            print("Too high ! try again") 
        else:
            print(f"correct the answer the was{answer}")
            print(f"number of guesses{guesses}")  
            is_running=False
    else:
        print("Invalid guess")
        print(f"Select a number b/w {lowest_num}to{highest_num}")


# or
import random

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
# print(answer)

guesses=0
is_running=True

print("Python number guessing game")
print(f"Select a number b/w {lowest_num}to{highest_num}")

while is_running:
    guess=input("Enter you guess")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1
        if guess<lowest_num or guess> highest_num:
            print("This number is out of range")
            print(f"Select a number b/w {lowest_num}to{highest_num}")
        elif guess<answer:
            print("Too low !try again")
        elif guess>answer:
            print("Too high ! try again") 
        else:
            print(f"correct the answer the was{answer}")
            print(f"number of guesses{guesses}")  
            # is_running=False
    else:
        print("Invalid guess")
        print(f"Select a number b/w {lowest_num}to{highest_num}")        