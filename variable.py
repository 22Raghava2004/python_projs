# <-this is for command
print("my goal")
print("gooodei")
# a variable is a container for a value(string,integer,float,boolean)
#a variable behave as if it wass the value it contains


#strings a string is series of characters
first_name="bro"
#  f is the format blue it recuires {}
food ="pizza"
email= "bro123@gmail.com"
print(first_name)
print(f"{first_name}hello{food}")
print(f"hello {first_name}")
print(f"your email is{email}")


#integer 
#a integer is a whole number
#integer dosnt require doublecolon 
age=25
quantity=3
num_of_students=30
print(f"you are age is{age} yoyo ")
print(f"your age is {age}and you are weight is{quantity}")
print(f"your class has 30 students{num_of_students}")

# float
price=10.99
gpa=3.4
distance=33.3333333
print(f"the price is ${price}")
print(f"your gpa is{gpa}")
print(f"distance is {distance} from your home")

#boolens


#<------------------>
#boolean
#boolen can be >>>True<<< or >>>False<<<<
#the first letter should be capital
is_students=False

print(f"are u a student?:{is_students} ")
#it is usefull in if statements    <<<<<<
if is_students:
    print("you are a student")
else:
    print("you are not a student")
    #is_student
    # if it is----> true<--- it will show you are astudent
    #other wise if -->false<--- it will show you are not a student<---
#example-->
for_sale=True

print(f"sale is there:{for_sale} ")
#it is use full in if statements
if for_sale:
    print("stock avaailable")
else:
    print("stock not availble")


#example 3---->
result=True
percentage=88.9
if result:
    print(f"pass percentage {percentage}{result}")
else:
    print("fail")


#exampple 234
name="raghava" #<----string
age=20   #<----integer
percentage=88  #<----float
is_string=False

if is_string:
    print(f"{name}is {age} old and his percentage is {percentage}")
else:
    print(f"{name}is not {age}old and but his percentage is{percentage} ")

