#object = a bundle of related attribute variable and method(function)
#class=used to design the structure and layout of a object

from car import Car

car1 = Car("BMW", 2020, "black", False)
car2 = Car("Audi", 2021, "white", False)
car3 = Car("Mercedes", 2022, "blue", True)
all_car = [car1, car2, car3]
for cars in all_car:
    print(f"Model: {cars.model}, Year: {cars.year}, Color: {cars.color}, For Sale: {cars.for_sale}")
car1.drive()
car2.stop()     
car1.stop()
car2.drive()    
car3.drive()
car3.stop() 
car1.describe()     
car2.describe()
car3.describe() 
      