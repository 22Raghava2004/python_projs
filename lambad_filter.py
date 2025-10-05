# lambda argument:expression
'''fun=lambda a,b:a+b
print(fun(2,3))'''
'''
number=[1,2,3,4,5,6,7,8,9,10]
num=lambda number:number%2==0
# this is filter
#filter(function,iterable   )
"even =list(filter(lambda number:number%2==0,number))"
''''''
even=list(filter(num,number))
print(even)
''''''

#map=map(function,iterable)
even=list(map(lambda number:number**2,number))
print(even)
'''