from random import randint
from school import School

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return randint(1, 100)
    
    def teach():
        pass

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom # classroom object
        self.subject_grade = {}
        self.marks = {}
        self.grade = None
        self.gpa = 0.00
        self.__id = None
        # self.total_marks = None

    def calculate_final_grade(self):
        sum = 0

        for grade in self.subject_grade.values():
            sum += School.grade_to_value(grade)
        
        if not sum:
            self.gpa = 0.00
            self.grade = 'F'
        else:
            self.gpa = sum / len(self.subject_grade)
            self.grade = School.value_to_grade(self.gpa)

        return f"{self.name} Final Grade : {self.grade} with GPA = {self.gpa:.2f}"
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, val):
        self.__id = val