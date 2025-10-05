class Car:
    def __init__(self, model, year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale    
    def drive(self):
        print(f"The {self.color} {self.model} is now driving.")
    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
car1 = Car("Toyota Camry", 2020, "Red", True)
car2 = Car("Honda Accord", 2019, "Blue", False) 
car1.describe()
car1.drive()
car1.stop()
car2.describe()
car2.drive()
car2.stop() 