name=input("enter the name")
name1=len(name)#<<<-----length of the given string
print(name1)
name2=name.find("g")#<<<<<< it is used to find the first occuranc eof anything u want
print(name2)
name3=name.rfind("-")#<<<<------- it is use to find the occurance of the given string from the last<<<<<<<          #<--- it is a reverse of find
print(name3)
 

name4=name.capitalize()#<<<<< first letter in the string is capitalize
print(name4)
name5=name.upper()#<<<<<< it is used to convert all the letterr in the string in uppercase
print(name5)
name6=name.lower()#<<<<<<< it is use to conver all to lowercase
print(name)
name7=name.isdigit()#<<<<< it is true if all string have digit if any letter false
print(name7)
name8=name.isalpha()#<<<< true if only alphabet else false
print(name8)
print(name.count("-"))#<<<<for count the occurance character in given string
result=name.replace("-","0")
print(result)#,,,it is used to replce the character with oter character in given string


# user name not more than 12
# user name must not contain space
#user name must not contain any digit
username=input("enter the username:  ")
if len(username)>=12:
    print(f"user name taken {username}")
elif not username.find(" ")==-1:
    print("user name cannot contain space")
elif not username.isalpha():
    print("enter only charaacter")   
else :
    print("user name not taken")
    