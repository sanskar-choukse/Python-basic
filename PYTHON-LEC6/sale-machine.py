import random

def spin_row():
    symbols=['🍒','🌸','🍉','🎇','🎨']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🌸':
            return bet*4
        elif row[0]=='🍉':
            return bet*5
        elif row[0]=='🎇':
            return bet*10
        elif row[0]=='🎨':
            return bet*20
        return 0
    

def main():
    balance =100

    print("***********************")
    print("Welcome to python slots")
    print("🍒 🌸 🍉🎇🎨")
    print("***********************")

    while balance>0:
        print(f"current balance:${balance}")

        bet=input("place your bet amount:")

        if not bet.isdigit():
            print("place your bet amount:")
            continue

        bet=int(bet)

        if bet>balance:
            print("Insufficient funds")
            continue
        
        if bet<=0:
            print("Bet must be greater thna 0")
            continue

        balance -= bet
 
        row=spin_row()
        print("spinning....\n")
        print_row(row)
     
        payout=get_payout(row,bet)

        if payout>0:
            print(f"you won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again=input("Do you want to spin again?(Y/N):")
 
        if play_again != 'Y':
            break
    print("*******************************************")
    print(f"Game over!Your final balance is ${balance}")
    print("*******************************************")

if __name__ == '_main_':
    main()

