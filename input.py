#input()= it is a function  that prompt the userr to enter data 
# return the entered data as a string
name=input("what is your name:")#inputing string value

print(f"hello {name}")
name=int(name)#<---changing itsdatatype to integer
print(type(name))
name+=1
print({name})

if name<=12:
         print("ok")
else:
         print("n0")


         ##dlodkrgjrkm
         name=input("your name")
         age=int(input("your age"))
         age=age+1
         print(f"my{name} is and i will be {age} years old next year")

#area of rectangle
length=int(input("enter the length"))
width=int(input("enter the width"))
area=length*width
print(f"area of the rectangle is {area}")#<------ for both variable and command f is used as format
print(area)#only for variable justa area is used

#exercise 3 shopping cart program
item=input("wha titems u would like to buy")
price=float(input("what is the price"))
quantity=float(input("how many woul u like"))
total=price*quantity
print(f"our prize is{price}")
print(f"we brought{item}*{quantity}")
print(f"our total is{total}")
