# class Student:
#     name = "Raziah"
#     code = "004"
#     school = "AkiraChix"
#     age = 20


    # OUTPUT
#     >>> from student import Student
#     >>> s= Student()
#     >>> s.name
#     'Raziah'
#     >>> type(s)
#     <class 'student.Student'>


class Student:
    school = "AkiraChix" 
    def __init__(self, first_name, last_name, age, country, code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code


    def greet_student(self):
        greeting = f"Hello {self.first_name}, welcome to {self.school}. Your code is {self.code}"
        return greeting
    
    def year_of_birth(self):
        birth_year = f"Hello {self.first_name}, you were born in {2024 - self.age}"
        return birth_year
    
#     >>> mercy.year_of_birth()
# 'Hello Mercy, you were born in 2004'

    
    def student_initials(self):
        initial = f"Your initials are {self.first_name[0]}.{self.last_name[0]}"
        return initial
    
#     >>> mercy = Student(first_name = "Mercy", last_name = "Chemtai", age = 23, country = "Kenya", code = 69)
# >>> mercy.student_initials()
# 'M C'
    
    def student_fullname(self):
        fullname = f"{self.first_name} {self.last_name}"
        return fullname
    
#     >>> mercy.student_fullname()
# 'Mercy Chemtai'
    

    def enrollment(self):
        enroll = f"Hello {self.first_name} {self.last_name}, you have successfully enrolled at {self.school} and your code number is {self.code}"
        return enroll
    
#     >>> mercy.enrollment()
# 'Hello Mercy Chemtai, you have successfully enrolled at AkiraChix and your code number is 69'




















# OUTPUT
# >>> from student import Student
# >>> mercy = Student(first_name = "Mercy", last_name = "Chemtai", age = 23, country = "Kenya", code = 69)
# >>> mercy.code
# 69

# >>> eshe = Student(first_name = "Eshe", last_name = "Aziz", age = 24, country = "Kenya", code = 48)
# >>> eshe.last_name
# 'Aziz'

# >>> aline = Student(first_name = "Aline", last_name = "Mutesi", age = 24, country =  "Rwanda", code = 34)
# >>> aline.country
# 'Rwanda'


# Part Two
# def greet_student(self):
# >>> from student import Student
# >>> mercy = Student(first_name = "Mercy", last_name = "Chemtai", age = 23, country = "Kenya", code = 69)
# >>> mercy.greet_student()
# 'HelloMercy, welcome to AkiraChix. Your code is 69'













