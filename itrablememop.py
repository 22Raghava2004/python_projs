#iterables an object or collection thar can return its elements one at a time
#     allowing it to be iterated over in a loop
#num=(1,2,3,4,5) 
#for nu in num:
#    print(nu)

#for nu in reversed(num):
 #   print(nu)
#fruits={"apple","oraange","banana","coconut"}
#for fruit in fruits:
#    print(fruit)
#nma="Raghava"
#for x in nma:
#    print(nma)
my_dictionary={"a":1,"b":2,"c":3}
for key,value in my_dictionary.items():
    print(f"{key}:{value}")


#membership operators =used to test a value or variable is
#  founf in the sequence (string,list,tupl,set,dictionary)
#in
#not in

#word="apple"
#Tru=True
#while Tru:
 #   for x in word:
#
 #       if "a" in x:
  #          print(word)
   # Tru=False
from collections import Counter 
student={"apple","manggo","banana","gova"}

tue=True
while tue:
    students=input("enter the student name")
    if students in student:
            print(f"{students} is student")
            break
        
    elif students not in student:
            print(f"enterd student not in students ")
            continue
grades={"sandy":"A","mondy":"B","cundy":"C","dondy":"D"}

tue=True
while tue:
    students=input("enter the student name")
    if students in grades:
            print(f"{students} is student {grades[students]}")
            break
        
    elif students not in grades:
            print(f"enterd student not in students ")
            continue




word="raghavangowda@gmail.com"
if "a" in word and "@" in word:
       print(word)
       counter=Counter(word)
       rep_letter={char:count for char,count in counter.items() if count>1}
       print(rep_letter)


       #####
       from collections import Counter
word="raghavangowda@gmail.com"

if "a" in word and "@" in word:
       print(word)
       counter=Counter(word)
       print({key:value for key,value  in counter.items() if value>3})
            



#list comprehension=A concise way to create list in python
#                compact and easier to read that treditional loops
#                [expression for value in range iteerables if condition]


value={1:2,2:3,3:4}
print( {key:valuee for key,valuee in value.items()   if key>=1 })
value2=["1","3",4,5]
print([valuee2   for valuee2 in value2 if 4 in value2])
double=[ x**2  for x in range (1,11)]
print(double)
fruits=["orange","mango","pinapple","gova"]
fruits=[x for x in fruits  ]
print(fruits)
num=[1,-2,3,4,-5,6,-7,8,9]
nume=[x for x in num if x%2==0]

nump=[x for x in num if x>=0]

numn=[x for x in num if x<0]

num0=[x for x in num if x%2==1]
print(nume)
            

grades=[85,76,65,54,93,64,31]
passing_grades=[f"pass{x}" for x in grades if x>=60]
print(passing_grades)
fruits=["orange","mango","pinapple","gova"]
fruits=[x[0] for x in fruits  ]
print(fruits)