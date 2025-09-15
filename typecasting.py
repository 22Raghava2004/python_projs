# typecasting is a process of converting one datatype to another datatype
# str(),int(),float(),bool()
name="raghava" #<----string
age=20   #<----integer
percentage=88.88  #<----float
is_student=True
i=11
percentage=int(percentage)
print(percentage)
age1=float(age)

age=bool(age)
print(age)
if i<=10:
    print(f"allowed{age}{age1}")
    i+=1
    print(i)
    is_student=str(is_student)
    print(type(is_student))
else:
    print(f"under age{age}")
    is_student=str(is_student)
    print(type(is_student))#<<<<<<<< this isused to check which datatype is the vaiable******