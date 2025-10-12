import json
import os

book="C:\\Users\\ragha\\OneDrive\\Desktop\\bbbo.json"
isrunning =True
isjog=True
list1=[]


if os.path.exists(book):
     with open(book,"r") as file:
        try:
            list1=json.load(file)
        except json.JSONDecodeError:
            list1=[]
else:
     list1=[]

while isrunning:

    c=input("enterelement to add in the book")
    list1.append(c)
    
    while isjog:
        
        d=input("do you want to continue y/n")
        if d=="n":
            isjoog=False
            isrunning=False
            break 
        elif d=="y":
                isjog=True
                isrunning=True
                break
        else:
                print("invalid input")
                isjog=True
                continue
            
        
        
with open(book,"w") as file:
    
    json.dump(list1,file,indent=4)
print(f"the file name {book} exist")