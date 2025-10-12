import json
import csv
employee=[["name","age","job"],
          ["spongebob",20,"fry cook"],
            ["sandy",30,"scientist"],
            ["patrick",19,"unemploye "]
        
          ]

text_file="C:\\Users\\ragha\\OneDrive\\Desktop\\output.csv"
try:
    with open(text_file,"w", newline="") as file:
        writer = csv.writer(file)#writerow is used to write the row in csv files
        for row in employee:
            writer.writerow(row)
        print(f"the file name {text_file} exist")
    with open(text_file,"r",newline="") as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
except FileExistsError:
    print("the file not created")