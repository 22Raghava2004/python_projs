class Books:
    def __init__(self, title, author,num_pagees):
        self.title = title
        self.author = author
        self.num_pagees = num_pagees
    def __str__(self): #gives a string representation of the object
        return f"{self.title} by {self.author}"
    def __eq__(self,other): #checks if two objects are equal
        return self.title == other.title and self.author == other.author and self.num_pagees == other.num_pagees
    def __lt__(self,other) :# checks if one object is less than another
        return self.num_pagees < other.num_pagees  
    def __lt__(self, other):
        return self.num_pagees > other.num_pagees
    
    def __add__(self, other):
        return self.num_pagees + other.num_pagees
    def __contains__(self, keyword): # checks if a keyword is in the title or author
        return keyword.lower() in self.title.lower() or keyword.lower() in self.author.lower()

    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pagees":
            return self.num_pagees
        else:
            return f"'{key}' is not a valid attribute of Books"
book1=Books("hobbit", "tolkien", 310)
book2=Books("harry potter and the philosopher stone", "rowling", 223)
book3=Books("The lion, the witch and the wardrobe", "lewis", 206)
print(book1)
print(book1==book2)
print(book2<book3)  # This will raise an error since __lt__ is not defined
print(book1>book3) # this will raise an error since __lt__ is not defined
print(book1 + book2)  # This will raise an error since __add__ is not defined
print("lion" in book3)
print(book1['author'])# This will return the author of book1