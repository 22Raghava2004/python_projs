# ducktying = another way to achieve polymorphism besides inheritance
#      object must have minimum necessary attributes ?methods 
#  "if it quacks like a duck and walks like a duck, then it is a duck"
class Animal:
    Alive= True
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "meow"
class Car():
    def speak(self):
        return "vroom"
animal=[Dog(), Cat(),Car()]
for x in animal:
    print(x.speak())


