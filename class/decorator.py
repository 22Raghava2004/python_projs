# decorator = a function that extends the behavior of another function
#   w/omodify the base finction
# pass the base function as an argument to the decorator

def sprincles(func):
    def wrapper(*args, **kwargs):
        print("add some sprincles🍬")
        func(*args, **kwargs)
    return wrapper

def cake(flo):
    def wrapper(*args, **kwargs):
        print(f"give cake")
        flo(*args, **kwargs)
    return wrapper


@sprincles
@cake
def icecream(floavor):
    print(f"give {floavor}me some icecream")



icecream('chocolate')