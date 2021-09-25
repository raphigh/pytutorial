class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def print_first_name(self):
        print('my first name is : '+self.first_name)
    def print_last_name(self):
        print('my last name is : '+self.last_name)
    def print_info(self):
        print('my full name is : '+self.first_name+' '+self.last_name+' ')

class Student(Person):
    def print_info(self):
        print('I am a student my full name is : '+self.first_name+' '+self.last_name+' ')

class Teacher(Person):
    def print_info(self):
                print('I am a teacher my full name is : ' + self.first_name + ' ' + self.last_name+' ')