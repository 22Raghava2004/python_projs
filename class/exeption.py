# exeptiom is a event that interrupt the flow of the program
# zeroDivision error , typeerror valueError
#1 try 2 except 3 finally
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("you cannot devide by zero")
except ValueError:
    print("invalid input enter ony numbers")
except exception:
    print("an error occured")
finally:
    print("do some clean up here")