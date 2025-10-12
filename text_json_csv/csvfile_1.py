import csv

textfile="C:\\Users\\ragha\\OneDrive\\Desktop\\output2.csv"

text={"eg":"wrong","eg2":"wrong2","eg3":"wrong3","eg4":"wrong4","eg5":"wrong5"}

with open(textfile,"w",newline="") as file:
    writer=csv.writer(file)
    for key,value in text.items():
        writer.writerow([key,value])
        
    