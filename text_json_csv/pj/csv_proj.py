import json
import csv
company={}

employees=input("how many employees do you want to add")
key=0

for i in range(int(employees)):
    employee_id=input("enter the employee id")
    employee_name=input("enter the employee name")
    employee_salary=input("enter the employee salary")
    company[employee_id]={key:employee_id,"name":employee_name,"salary":employee_salary}
    key+=1
        


        


text_file="C:\\Users\\ragha\\OneDrive\\Desktop\\output.csv"
try:
    with open(text_file,"w", newline="") as file:
        writer = csv.writer(file)#writerow is used to write the row in csv files
        for key,value in company.items():
            writer.writerow([key, value["name"], value["salary"]])

        print(f"the file name {text_file} exist")
    with open(text_file,"r",newline="") as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
except FileExistsError:
    print("the file not created")