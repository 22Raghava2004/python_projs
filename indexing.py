#indexing accessing elements of a sequence using [] (indexing operator)
#[start : end :step]
credit_num="1234-2445-3335-3333-1234"
print(f"count {credit_num.replace("-","0")}\n{credit_num[10:14]}")
print(credit_num[0])
print(credit_num[::3])
print(credit_num[5:])
last_num=credit_num[-4:]
print(f"XXXXXXxXXX{last_num}")
last_num2=credit_num[::-1]
print(last_num2)


#format specifiers ={value:flags} format a value based on wahat flag are inserted
prize1=126.2244
prize2=2334.3466
prize3=-36.456
print(f"prize 1 {prize1:012.2f}")
 # +<sign is use dto precide with + symbol
#.2f is for ast desmial after .
#>for gap in in begning
# #>for gap  
#any number 
print(f"prize 2 {prize2:>+12,}")
print(f"prize 3 {prize3:>12}")