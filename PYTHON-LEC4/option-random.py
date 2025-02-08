import random

option=("stone","Paper","Scissore")
running=True

while running:

  player=None
  computer=random.choice(option)

while player not in option:
      player=input("Enter the value:(Stone,paper,scissore:)").lower()

print(f"player:{player}")
print(f"computer:{computer}")

if player == computer:
         print("It's Tie!")
elif player=="stone" and computer=="paper":
    print("You win!")
elif player=="Paper" and computer=="Scissore":
    print("you win!")
elif player =="Scissore" and computer=="stone":
    print("you win!")
else:
    print("you lose!")  


if not input("play again(y/n)").lower()=="y":
    running=False

print("Thanks")