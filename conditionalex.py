#conditional expresssion a non-line shortcut for the if-else statement(ternary operator)
#print or assign one of two value based on a condition

#  "output" if condition else "output"
num=-1
print("positive" if num>0 else "negative")
num1=6
result="even" if num1%2==0 else "odd"
print(result)
a=8
b=9
max_num=f"a is grester {a}" if a>b else f"b is greater{b}"
print(max_num)
# age
age=25
print("adult " if age>=18 else "not adult")


##
unit="guest"
print(f"{unit} has all access " if unit=="admin" else f"{unit} limited access")


###
temp=32
print("hot" if temp>=35  else "cold")


