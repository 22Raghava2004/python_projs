# character and character sequence in regular expression\

# ^ - start of a string
# $ - end of a string
# \d - digit
# \D - non-digit
# \s - whitespace
# \S - non-whitespace
# . - any character except newline

import re
'''
str="my name is raghav 669"
if re.match("^m",str):
    print("match")
else:   
    print("not match")

pat="v$"
print(re.findall(pat,str))

pat="."
print(re.findall(pat,str))


pat= "\d"
print(re.findall(pat,str))

pat ="\D"
if re.match(pat,str):
    print("amtch")
else:
    print("not match")

print(re.findall("\s",str)) # this finds the no of space present in the string

pat="\S"
print(re.findall(pat,str)) # this print all the character present in the string except space

'''

str_3="faaapaple faell from the tree"
# pat="a..le"
# print(re.findall(pat,str_3))

# * - zero or more occurrences
# + - one or more occurrences
# ? - zero or one occurrence
#() - capture and group
#{} - exact number of occurrences
#| - either or
'''
pat="ae*"
print(re.findall(pat,str_3))

pat="ae+"
print(re.findall(pat,str_3))


pat="^f.*?"
print(re.findall(pat,str_3))


pat ="^faaapaple (\S+fr\S+)"
print(re.findall(pat,str_3))
'''



# []- match characters in brackets
# [^]- match characters not in brackets 
# - - range of characters
# \ - escape special characters
#{m,n} - match from m to n times

str_4="heelloo 12345, this is raghav 67890"




pat="[a-g]"
print(re.findall(pat,str_4))
# the rang of characters from a to g is printed


pat="he{2}llo{2}"
print(re.findall(pat,str_4))
# curli barackets defins how many time should the character should repeat from the dtring



pat="t([^ ]*)"
print(re.findall(pat,str_4))