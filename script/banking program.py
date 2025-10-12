def balance_(balance):
    print(f"your balance is {balance}")
def deposit_amount():
    amount=float(input("enterthe amount"))
    if amount<0:
        print("invalid input")
        return 0     
    else:
        return amount
def withdraw_amount(balance):
    amount=float(input("enter amount to withdraw"))
    if amount<0:
        print("enter valid amoiunt")
        return 0
    elif amount>balance:
        print("insuffint fund")
        return 0
    
    
    else:
        return amount

def main():
    balance=0
    is_running=True
    while is_running:
        choice=int(input("enter your choce"))
        if choice==1:
            balance_(balance)
        elif choice==2:
            balance += deposit_amount()
        elif choice==3:
            balance -= withdraw_amount(balance)
        elif choice==4:
            is_running=False
        else:
            print("invalid input")
if __name__=='__main__':
        main()

        