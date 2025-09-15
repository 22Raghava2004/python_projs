#while loop
 #loops the statement until it is True

user=input("enter your name   ")

while user=="":
    print(" please enter proper name enter your name")
    user=input("enter your name")
print(f"your name is {user}")    

#age program
age=int(input("enter you nsme"))
while age<0:
    print("enter valid age")
    age=int(input("enter you nsme"))
print(f"you age is {age}")

##food program
food=input("enter your nname")
while not food=="q":
    print(f"your nmae {food}")
    food=input("enter your nname")
print("bye")


##
num=float(input("enter your digit between 1ti 10"))
while num<1 or num>10:
    num=float(input("enter your digit between 1ti 10"))

print(f"your entered digit is {num}")    
gender=input("is he girl or boy")


while True:
        gender=input("is he girl or boy1")
        break
if gender=="boy":
    name=input("entr his name")
    print(f"hi {name} you are a {gender}")
elif gender=="girl":
    name=input("enter her nmae")
    print(f"hi {name} you are a {gender}")


##while rate intrest calculator
rate=0
principle=0
time=0
while True:
    rate=int(input("enter rate"))
    if rate<0:
        print("rate cannot be less than 0")
    else:
        break

while True:
    time=int(input("enter time not lessthan 0"))
    if time<0:
        print("you canntor enter less than 0")
    else:
        break
while True:
    principle=int(input("more  princ than 0"))
    if principle<0:
            print("less than 0")
    else:
            break
print(f"principle {principle}")
print(f"rate {rate}")
print(f"time  {time}")

total=principle*pow((1+rate/100),time)
print(f"balance after {time}year/s: ${total:.2f}")
print(f"{pow(rate,2)}")
    



     
     ####
     #for loop can block of code can be executable fixed number of times.
#          you can iterate a range,string,sequence,etc.
for x in range(1,22):
    if x==13:
        break
    else:
        print(x)


#####
credit_no="1234-5443-2222-6788"
for x in credit_no:
   print(x)

   #nested loop=a lop present within the another loop(outere,inner)
# outer loop:
#inner loop:
rows=int(input("enter the no of rows"))
colomns=int(input("enter the number of coloms"))
symbol=input("enter the syble to projecct")
for x in range(rows):
    for y in range(colomns):
        print(symbol,end="")
    print()
    #list/array same fucking same