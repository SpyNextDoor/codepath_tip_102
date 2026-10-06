"""
OOP

classes are the basics of OOP
"""

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"Hi, I am {self.name}, a {self.age} year old {self.major} major."
    
    def hi(self):
        return "Hi I am {self.name}"

s1 = Student("Alice", 20, "CS")
s2 = Student("Bob", 22, "Math")

# inheritance --> TeachingFellow will have everything Student class has and more
class TeachingFellow(Student):
    def __init__(self, name, age, major, cohort):
        super().__init__(name, age, major)
        self.cohort = cohort
    def introduce(self):
        return f"{super().introduce()} I am also TF-ing for the {self.cohort} cohort."
    

tf1 = TeachingFellow("Andrew", 22, "Physics", "Fall 2026")
print(tf1.introduce())