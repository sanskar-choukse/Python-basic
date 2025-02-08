def show_Balance():
    print("***************")
    print(f"your balance is: ${balance:.2f}")
    print("***************")
def Deposit():
    Amount=float(input("Enter the deposit amount:"))

    if Amount<0:
        print("***************")
        print("That's not a valid amount")
        print("***************")
        return 0
    else:
        return Amount
    
def withdraw():
    Amount=float(input("Enter the withdraw amount:"))

    if Amount>balance:
        print("***************")
        print("unsufficient Amount")
        print("***************")
        return 0
    elif Amount<=0:
        print("***************") 
        print("Enter the Amount grater than 0")
        print("***************") 
        return 0
    else:
        return Amount

def exit():
    pass

balance=0
is_running=True

while is_running:
    print("***************")
    print("BANK OF INDIA")
    print("***************")
    print("1.SHOW BALANCE")
    print("2.DEPOSIT")
    print("3.WITHDRAW")
    print("4.EXIT")
    print("***************")

choice=input("ENTER YOUR CHOICE(1-4):")


if choice=='1':
        show_Balance()
elif choice=='2':
       balance+=Deposit()
elif choice=='3':
       balance-=withdraw()
elif choice=='4':
        is_running=False
else:
        print("***************")
        print("That is not valid choice")
        print("***************")

print("***************")        
print("Thank you! have a nice day!")
print("***************")