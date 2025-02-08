# python quiz game

question=("How many element are in the periodic table?",
          "which animal do you like?",
          "What is the most abundant gas in Earth's atmosphere?",
          "How many bones are in the human body?",
          "which planet in the solar system is the hottest?")

option=(("A.116","B.114","C.234","D.654"),
        ("A.Whale","B.Elephand","C.crocodile","D.ortich"),
        ("A.Nitrogen","B.Oxygen","C.carbon di-oxide","D.Hydrogen"),
        ("A.105","B.234","C.123","D.642"),
        ("A. ","B. ","C. ","D. "))

answer=("A","B","C","D","A")

guesses=[]
score=0
question_num=0

for questions in question:
    print("--------------")
    print(questions)
    for options in option[question_num]:
      print(options)

    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)

    if guess==answer[question_num]:
        score+=1
        print("Correct!")
    else:
        print("INCORRECT!")
        print(f"{answer[question_num]} is the correct answer")
    question_num+=1


print("-----------------")
print("Result")
print("-----------------")

print("Correct Answer:",end="")
for answers in answer:
    print(answers,end=" ")
print()    

print("guess the Answer:",end="")
for guess in  guesses:
    print(guess,end=" ")
print() 

score=int(score/len(question)*100)
print(f"score is {score}%")