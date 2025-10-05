'''import time
num=[1,2,3,4,5,6,7,8,9,10]
itreables=iter(num)
for i in range(len(num)):
    time.sleep(2)
    print(next(itreables))
    '''
#generator=(generator expression)
#gen=(i for i in range(10) if i%2==0)

'''
def fun(num):
    yield num**2
    yield num**3
    yield num**4

number=[1,2,3,4,5,6,7,8,9,10]
for ans in number:
    for val in fun(ans):
        print(val)
    '''
def square():
    num=0
    while num<=5:
        yield num**2
        yield num**3
        num+=1
for i in square():
    print(i)

'''
def square():
    num=0
    while num<=5:
        yield num**2
        num+=1
    num=0
    while num<=5:
        yield num**3
        num+=1
for i in square():
    print(i)
    '''