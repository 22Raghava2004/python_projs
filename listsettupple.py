#collection =single "variable"used to store multiple values
#list/array=[] ordered and changeable,duplicates OK
#set={} unordered and immutable ,but add/remove OK.no duplictes
#tuples =() ordeered and unchangable .duplicate OK.faster

#fruit=["apple","mang0","orange","coconut"]
#print(fruit) 
#print(fruit[0])
#print(fruit[0:3])
#print(fruit[::-1])
#if len(fruit[1])==5 and len(fruit[2])==6:
#       print(f"{len(fruit[1])} {len(fruit[2])}")
#else:
#       print("lfg")
#print("apple" in fruit)#thie give boolean answer true or false
#print(dir(fruit))
#print(help(fruit))
#fruit[0]="pineaple"#<---it can be iterated
#print(fruit)
#fruit.append("gova")
#fruit.remove("apple")
#fruit.insert(0,"moimoi")
#fruit.sort()
#fruit.reverse()
#fruit.clear()
#print(fruit.index("apple"))###<---at which place it is placed
#print(fruit.count("orange"))##<counts  how many times the its is repeated
#for fruits in fruit:
   # print(fruits)


   ###------sets
#fruits2={"apple","mang0","orange","coconut"}
#print(dir(fruits2))
#print(help(fruits2))
#print(len(fruits2))
#print("pineapple" in fruits2)
#fruits2.remove("apple")
#fruits2.add("pineapple")
#fruits2.pop()
#fruits2.clear()

#print(fruits2)


###tuple
fruits2=("apple","mang0","orange","coconut")
print(len(fruits2))
print(fruits2.count("coconut"))
print(fruits2.index("apple"))

#3#33

price=[1,2,2,3]


total=sum(price)
print(f"your total is:{total}")


'''setttt1=set()
isturning=True
isrunning=True
while isrunning:
    name=input("enter your name")
    setttt1.add(name)

    while isturning:
        exit=input("do u want to exit y/n")
        if exit=="y":
            isrunning=False
            isturning=False
        elif exit=="n":
            isrunning=True
            break
            

    print(setttt1)'''