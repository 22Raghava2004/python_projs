#if statement is to give this or thst
#else is if if ststement is false the else is taken
#elif if not both
age=input("enter y or n")
if age=="y":
  print("you are allowed")
  age1=int(input("enter your age"))
  if age<18:
      print("enter any value")
      
  elif 100<=age1>=18:
      print("youa are allowed")
  elif age1>=100:
      print("you are too old go die")
  else:
      print("you are not 18+")

elif age=="n":
  print("you are not allowed")
elif age=="":
  print("valid value")
else:
    print("enter the y or n")



    
###elsercise 1
operatore=input("enter the operator")
num1=float(input("enter the num1 value"))
num2=float(input("enter the num2 value"))
if operatore=="+":
    result=num1+num2
    print(f"additiotn is{round(result,3)}")
elif operatore=="-":
    result=num1-num2
    print(f"sub{round(result,3)}")
elif operatore=="**":
    y=float(input("enter the value to be powered"))
    x=float(input("enter the power"))
    result=pow(y,x)
    print(f"power of the given value is{round(result,3)}")
elif operatore=="/":
    if num1>0:
        result=num1/num2
        print(result)
    elif num1<=0:
        print("invalid")
else:
    print("operator invalid")        




###3#e  exercise 2:

unit=input("enter the temp in c or f")
temp=float(input("enter the temp value"))
if unit=="c":
    temp=round((temp*9)/5+32,2)
    print(f"the temp in feranite is{temp}f")
elif unit=="f":
     temp=round((temp*9)/5+32,2)
     print(f"the temp in feranite is{temp}c")
else:
     print('temp invalid')



