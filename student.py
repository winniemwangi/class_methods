class Student:
     school = "Akirachix"
     def __init__(self,country,firstname,secondname,age):
        self.firstname = firstname
        self.country = country
        self.secondname = secondname
        self.age = age
     def full_name (self):

         return f"Hello {self.firstname} {self.secondname} How is {self.country}"
     def year_of_birth (self):  
         year=2022 - self.age
         return f"Your year of birth is {year}"
     def initials (self):
         return f"Your initials are {self.firstname[0]} {self.secondname[0]}"


    
