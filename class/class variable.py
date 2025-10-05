#class variable :shared by all instances of the class

# defin eoutside of constructor
#allow you to share data among all objects create from that class
class student:
    class_year=2024
    num_students=0
    def __init__(self,name, age):
        self.name=name# Initializing instance variable
        self.age=age# Initializing instance variable
        student.num_students+=1    
    
student1=student("spongebob", 30)# Creating an instance of student
student2=student("patric", 35)
student3=student("sandy", 28)
student4=student("squidward", 40)


print(f"my graduating class of {student.class_year} has {student.num_students} students")# Accessing class variable
print(student1.name)# Accessing the name attribute directly
print(student1.age)  # Accessing the age attribute directly 
print(student2.name)# Accessing the name attribute directly
print(student2.age)  # Accessing the age attribute directly
print(student3.name)
print(student4.name)
 

'''
 #######
class student:
    def mode(self, name):
        self.name = name
    def display(self):
        print("Name:", self.name)
dev=student()
dev2=student()
dev3=student()
dev.mode("john")
dev.display()
dev2.mode("doe")
dev2.display()  
dev3.mode("jane")# Assigning a name to dev3
print(dev3.name)  # Accessing the name attribute directly
dev3.display()  # Calling the display method to show the name
'''