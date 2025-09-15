#functions=a block of reusable code
#         place()after the function name to invoke it
def birthday(name,age): # parameter  is a temperaury variable use within the function
    print(f"happy birthday{name}")
    print(f"its bros birtday{age}")
    print("bo its your birthdsy")
    print()
birthday("bro",20)#<--- giving it arguments
birthday("bro",14)
birthday("bro",15)



def add(a,b):
    z=a+b
    return z

def sub(a,b):
    z=a-b
    return z
def mul(a,b):
    z=a*b
    return z
def div(a,b):
    z=a/b
    return z

    
print(add(1,2))
print(sub(2,3))
print(mul(2,4))
print(div(6,2))
#default functions
def functi_moi(age,name=100):
    print(f"{name} is and age is {age}")


ask="ass"
functi_moi(ask)
#sample prog
def create(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + last
firstname=input("enter the first naem")
lastname=input("enter the last naem")
full=create(firstname,lastname)
print(full)


#default prog
import time
def timer(stop,start=0):
    for x in range(start,stop+1):
        print(x)
        time.sleep(1)
    print("done")
timer(10)


#sample default
def fun_discount(price,discount,tax):
    total=(price*discount)/tax
    return total
fun_discount(1000,200,0.5)

#keyword= used to notify what is the order
def fun_age(name,age,first,last,middle):
    print(f"{name}-{age}-{first}-{last}-{middle}") 

fun_age(last="judo",name="karate",age="muithai",first="taikondo",middle="kungfu")


####***args
def fun_(*args):
    total=0
    for arg in args:
        total+=arg
    print(args)
    return total


dice=[]

while True:

    value=input("enter the number to be added")
    
    if value==value.isalnum() or value.isalpha() :
        if value=="q":
            
            
            break
        else:
            print("cannot be alphabet")
            continue
    else:
        dice.append(int(value))
        continue
        
    
fun=fun_(*dice)
print(fun)


######
def display(*args):
    for arg in args:
        print(arg,end=" ")
    print(args)
display("dr","ddo","little")


#####*kwargs for keyword 
#*args(for multiple arguments)
#**kwargs(for multiple keywords)
# * unpacking operator
def add(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")#,end=" ")
    
ele={}
ab=True
while ab:
    a=input("enter the key value")
    b=input("enter the value")
    ele.update({a:b})

    while True:
        
        reenter=input("do you want to enter more y/n")
        if "y" in reenter:
            break
        elif not reenter=="n" or reenter =="y":
            continue
        elif "n" in reenter:
            ab=False
            break
    continue
            
    
    
    
add(**ele)


