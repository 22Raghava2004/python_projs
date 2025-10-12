isrunning=True
key=0
text_file={ }
while isrunning:
    key+=1
    employee=input("enter the name of employee")
    
    
    if employee =="q":
        isrunning=False
    else :
        text_file.update({key:employee})
        
print(text_file.values())

file_path="C:\\Users\\ragha\\OneDrive\\Desktop\\output.txt"
try:
        with open(file_path,"w") as file:#w is used to write the file
            for x in text_file.values():#iterating the values of dictionary
                file.write("\n"+x)
    #   with open(file_path,"r") as file: for opening
     #       content=file.read()
      #      print(content)
        print(f"the file name{file_path} exist")
except FileExistsError:
        print("the file not created")