#arthemetic op
#+,-,*,%,/,**
#result=result+1
#result+=1


#round()
#max()
#pow()
#min()


#math

import math
print(math.pi)#<---for pi value
print(math.e)#<>>> for expo value
num=9.1
result=math.sqrt(num)#<---- to get square root
print(result)
result1=math.ceil(num)#<_____for rondup of given value
print(result1)
result2=math.floor(num)#<for round up of given value
print(result2)


x=1.22
y=2
z=3
#result=round(x)
#print(result)
print(round(x,1))
print(abs(y))
print(pow(y,3))
print(max(x,y,z))
print(min(x,y,z))


##########exercise 1
import math
radius=float(input("enter the radius"))
print(f"your entered radius is{radius}")
pi=math.pi
circ=2*pi*radius
print(f"circumference of the given circleis{round(circ,2)}")

#####exercise 2
import math
radius=float(input("enter the radius"))
print(f"your entered radius is{radius}")
area=math.pi*pow(radius,2)
print(f"area of circle is{round(area,2)}")




#######exercise 3  c=sqrt(a^2+b^2)
import math
a=float(input("enter the a value "))
b=float(input("enter the b value "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"the side is {c}")

