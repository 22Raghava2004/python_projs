#inheritance =allow a class to inherit attributes and methods from another class
#             helps with code reusability and extensibility
#             class child(parent):  
class animal:
    def __init__(self, name):
        self.name= name
       
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is asleeep")
        
        
class Dog(animal):
    def speak(self):
        print("woof")


class Cat(animal):
    def speak(self):
        print("meow")

class Mouse(animal):
    def speak(self):
        print("sweek")
        


dog=Dog("scooby")
cat=Cat("garfield")
mouse=Mouse("jerry")
print(dog.name)
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
cat.speak()