import json
employee={
    "joker":"clown",
    "batman":"dark knight", 
    "iron man":"billionaire",
    "captain america":"super soldier",
    "hulk":"green giant"
}

text_file="C:\\Users\\ragha\\OneDrive\\Desktop\\output.json"
try:
    with open(text_file,"w") as file:
        json.dump(employee,file,indent=4)
        print(f"the file name {text_file} exist")
  #  with open(text_file,"r") as file:
  #      content=json.load(file)
   #     print(content,end=" ")
except FileExistsError:
    print("the file not created")