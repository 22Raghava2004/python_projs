import re
'''
sttr_1="apple"
if re.match(sttr_1,"apple"):
    print("match")
else:
    print("not match")
    #match in regular expression
#match()=matches the beginning of the string
if re.match(sttr_1,"applepie"):
    print("match")
else:
    print("not match")

if re.match(sttr_1,"aaapple"):
    print("match")
else:
    print("not match")
'''
#findall()=returns a list containing all matches
#if it finds the match in the string it returns the list of the matched string
sttr_2="The rain in m to shame in me Spain"
x=re.findall("ai",sttr_2)
print(x)
#syntax
# re.findall(pattern,string,flags=0)
#flags=optional, a set of flags that change how the pattern is interpreted
#If no matches are found, an empty list is returned

''''''

if re.match(sttr_2,"The rain in m to shame in me Spain"):
    # if the string starts with "The rain in m to shame in me Spain" it returns match
    #if not it returns not match
    print("match")  
else:
    print("not match")


    
#search()=searches the string for a match and returns a match object if there is a match
#If there is more than one match, only the first occurrence of the match will be returned
if re.search("ai",sttr_2):
    print("match")
else:
    print("not match")