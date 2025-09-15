#static method that belongs to a class rather than any object from that class(instance)
#  usually usef for general utility functions
#instance method = best for operation on instance and of the class
#statiic methd =  best for utility functins that do not need access to class data

class employee:
    def __init__(self,name,position):
        self.name=name
        self.psition=position
    def get_info(self):
        return f"{self.name} is a {self.psition }"
    @staticmethod
    def is_valid_position(position):
        valid_positions =[ "manager","cashier","cook","janitor","waiter"]
        return position in valid_positions
  # True
  # Create an instance of employee
  # Call the instance method on the object
 # Call the instance method on the object
employee1 = employee("john","cook")
employee2 = employee("jane","manager")
employee3 = employee("doe","waiter")
print(employee.is_valid_position("cook"))  # True
print(employee1.get_info())# Accessing the get_info method
print(employee2.get_info())
print(employee3.get_info())
 


        

