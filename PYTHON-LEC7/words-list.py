import random

words=("apple","Mango","orange","pineapple","banana")

hangman_art={0:(" ",
                " ",
                " "),
             1:("0",
                " ",
                " "),
             2:("0",
                "|",
                " "),
             3:("0",
                "/|",
                " "),
             4:("0",
                "/|\\",
                " "),
             5:("0",
                "/|\\",
                "/"),         
             6:("0",
                " /|\\",
                "/ \\")}

def display_wrong(wrong):
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass
def main():
    answer=random.choice(words)
    print(answer)



main()
# if __name__== "_main_":
#     main()








           
                 
                 
                 
                 
                 
                 
                    