# class methods =allow operation onthe class itself
#take(cls) as the first parameter,which represents the class itself
 #instance method = best for operations on the instance of the class(objects)
# static method = best for operations that don't need access to the class or instance
# class methode best for class-level operations or require access to class variables

class students:
    count=0
    gpa=0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        students.count += 1
        students.gpa += gpa
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    @classmethod
    def get_count(cls):
        return cls.count
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"cls.gpa / cls.count:.2f"
    
student1=students("spongebob", 3.5)
student2=students("patrick", 3.8)
student3=students("sandy", 3.9)
print(student1.get_info())
print(students.average_gpa())