from script1 import *
def favdrink(drink):
    print(f"your fav drink is{drink}")
def main():    
    print("script 2")
    favfood("mango")
    favdrink("lassi")
    print("goodbye")
if __name__=="__main__":
    main()