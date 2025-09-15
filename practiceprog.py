##3countdown timer
import time #time module
my_time=int(input("enter the time"))
for x in range(0,my_time):
    second=x%60
    minutes=int(x/60)%60
    hrs=int(x/3600)
    print(f"{hrs:02}:{minutes:02}:{second:02}")
    time.sleep(1)
print("time up")



### shopping cart
food=[]
price=[]
total=0
while True:
    foods=input("enter a food  to quit q")
    if foods =="q":
        break
    else:
        prices=float(input(f"enter the price of {foods}  :"))
        food.append(foods)
        price.append(prices)
print("-----cat----")
for foods in food:
    print(foods)
    for prices in price:
        total+=prices
print(f"your total is:{total}")

#2d list
fruit1=[]
fruit2=[]
fruit3=[]

n=1
i=3
while True:


 for x in range(n):
    for y in range(i):
        fruit12=input("enter the fruit")
        fruit1.append(fruit12)
 print(fruit1)
 for row in fruit1:
    for num in row:
        print(num,end=" ")
        
 print()
 break
        
while True:
     
     for x in range(n):
       for y in range(i):
        fruit22=input("enter the fruit")
        fruit2.append(fruit22)
     print(fruit2)
     for row in fruit2:
       for num in row:
        print(num,end=" ")
        
     print()
     break
     
while True:
        
         for x in range(n):
          for y in range(i):
           fruit32=input("enter the fruit")
           fruit3.append(fruit32)
         print(fruit3)
         for row in fruit3:
            for num in row:
             print(num,end=" ")
         print()
         break

fruits=[fruit1,
             fruit2,
             fruit3]
for x in fruits:
    for num in x:
               print(num,end="")
    print()
print(fruits)

#####dial pad
num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()

    ##python quiz game
questions=("1.father of the nmation",
           "2.matrix hero",
           "3.dhoom 1 hero",
           "4.dhoom 2 hero")
options=(("A.modi","b.neharu","c.godi","4.elvish"),
         ("A.john wick","B.johny deep","C.rdj","D.mari"),
         ("A.herithik","B.salu","C.srk","D.john ab"),
         ("A.herithik","B.elvish","C.tanmay","D.dhoni"),
         )
answers=("A","A","D","A")
gusees=[]
score=0
question_no=0
for question in questions:
    print("------------------")
    print(question)
    for option in options[question_no]:
        print(option)
    gusee=input("enter your gusee").upper()
    gusees.append(gusee)
    if gusee==answers[question_no]:
        score+=1
        print("correct answer")
        print(f"{answers[question_no]} correct answer")
    else:
        print("incorrect")

    question_no+=1
print("result")
print("answer",end=" ")
for answer in answers:
    print(answer,end="")
print()
print("gusess",end="")
for guess in gusees:
    print(guess,end=" ")
print()
score=int(score/len(questions)*100)
print(score)




#consation stand program
#dictionary program
menu={"pizza":20,
      "popcorn":30,
      "coc":25.5,
      "burger":20.6,
      "puff":35,
      "soup":34.5,
      "mango juice":20
}
cart=[]
total=0
for key,value in menu.items():
    print(f"{key:12}:{value:.2f}")
while True:
    food=input("enter the food you want and q to quit").lower()
    if food=="q":
        break
    elif menu.get(food) is None:
        print("not in menu" )
        continue
    else:
      
       
       cart.append(food)
       for x in cart:
        print(f"{x},{menu.get(food)}")
        total+=menu.get(food)
        print(f"your total will be{total}")

for x in cart:
    print(x)
print(f"your total is{total}")



#####rock paper sizor
import random

#cart=["mango","orange","apple","gova","kivi"]
#num=random.choice(cart)
#random.shuffle(cart)
#print(cart)
#print(dir(random))
#print(help(random))
low=1
high=100
options=["rock","paper","sizor"]
total=0
total1=0
value=True
num=random.choice(options)

while value:
    number=input("enter the option enster q to quit: q")
   
    
    if number=="q":
        break
    elif number==num:
        print("play again")
        continue
    elif number=="rock" and num=="sizor":
        print(" player winner")
        total+=1
        continue
    elif number=="scizor" and num=="paper":
        print("player winner")
        total+=1
        continue
    elif number=="paper" and num=="rock":
        print("player winner")
        total+=1
        continue
    elif number not in options:
        print("not in options")
        continue
    else:
        print("computer win")
        total1+=1
print(f"plsyer win={total}")
print(f"computer win={total1}")
if total==total1:
    print("player and computer have same score")
elif total==0 and total1==0:
    print("player didnt played")
elif total>total1:
    print("player have high score")
elif total<total1:
    print("computer has high score")


    ######3
    #random die roll
    import random
print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
"┌──────────┐"
"│          │"
"│          │"
"│          │"
"│          │"
"└──────────┘"
dice_art={1:(
"┌──────────┐",
"│          │",
"│     ●    │",
"│          │",
"│          │",
"└──────────┘"),
2:(
"┌──────────┐",
"│          │",
"│          │",
"│    ●●    │",
"│          │",
"└──────────┘"),
3:(
"┌──────────┐",
"│ ●        │",
"│          │",
"│     ●    │",
"│        ● │",
"└──────────┘"),
4:(
"┌──────────┐",
"│  ●       │",
"│    ●     │",
"│      ●   │",
"│       ●  │",
"└──────────┘"),
5:(
"┌──────────┐",
"│  ●     ● │",
"│    ●     │",
"│  ●     ● │",
"│          │",
"└──────────┘"),
6:(
"┌──────────┐",
"│  ●     ● │",
"│    ●     │",
"│  ●     ● │",
"│      ●   │",
"└──────────┘",)
}
dice=[]

total=0
dice_no=int(input("enter the input"))
for die in range(dice_no):
    dice.append(random.randint(1,6))
#for die in range(dice_no):
   # for line in dice_art.get(dice[die]):
      #  print(line)
for line in range(6):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()
for die in dice:
    total+=die
print(f"total:{total}")