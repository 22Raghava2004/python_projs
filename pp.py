class student:
    def mode(self, name):
        self.name = name
    def display(self):
        print("Name:", self.name)
student1=student()
student2=student()

student1.mode("john")

student1.display()
student2.mode("doe")
student2.display()