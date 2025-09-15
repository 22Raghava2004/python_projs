#and<----both should be true
#or<------any one of them should be true
#not<-----opposit to given
temp=float(input("enter te temp"))
unit=input("enter a or b")
if temp>=35 or temp<=0 or unit=="a":
    print("canceled")
else:
    print("sceduled")



    temp=float(input("enter te temp"))
unit=True
if temp>=35 or temp<=0 or unit:
    print("canceled")
else:
    print("sceduled")
    
    

    temp=float(input("enter te temp"))
sunny=False #<------true or false for not
if temp>=35 and sunny:
    print("sunny")
    print("hot")
elif temp<=0 and sunny:
    print("cold very cold")
    print("cool weather")
elif temp>0 and temp<35 and  sunny:
    print("warm out sidee")
    print("simple warm weather")
elif temp>=35 and not sunny:
    print("sunny")
    print("cloudy")
elif temp<=0 and not sunny:
    print("cold very cold")
    print("cloudy")
elif temp>0 and temp<35 and not sunny:
    print("warm out sidee")
    print("cloudy")
     