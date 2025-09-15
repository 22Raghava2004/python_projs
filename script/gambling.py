#slot machine
import random
def spin_row():
    symbols=['🍓','🍒','🍋','💲','🃏']
    return[random.choice(symbols) for _ in range(3)]
def display_row(row):
    print(' '.join(row))
def pay_out(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🍓':
            return bet*4
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='💲':
            print("jackpot")
            return bet*10
        elif row[0]=='🃏':
            print('jockey')
            return bet**3
    return 0
    
def main():
    balance=int(input("your amount"))
    print('welcome to python slots')
    print('symbols:🍓🍒🍋💲🃏')
    print("************************")
    while balance>0:
        print(f"enter the currennt balance{balance}")
        bet=input("enter your bet aamount")
        if not bet.isdigit():
            print("enter a digit")
            continue
        bet=int(bet)
        if bet > balance:
            print("***insufficeint fund***")
            continue
        
        if bet<=0:
            print("****bet must be greaater than 0***")
            continue
        balance-=bet
        row=spin_row()
        print("spinning")
        display_row(row)
        payout=pay_out(row,bet)
        print(f"you won {payout}" if payout>0 else f"you lost try again")
        balance+=payout
        play_again=input("do you want to play again (Y/N)").upper()
        if play_again=="N":
            break
    print('***********************************')    
    print(f"game ovwer your final balance is {balance}")
        
        
if __name__=='__main__':
    main()
