class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teacher = {}   # { subject : teacher object }
        self.classroom = {} # { name : classroom object }

    def add_classroom(self, classroom):
        self.classroom[classroom.name] = classroom 

    def add_teacher(self, subject, teacher):
        self.teacher[subject] = teacher

    def student_admission(student):
        pass

    @staticmethod
    def calculate_grade(self, marks):
        if marks>=80 and marks<=100: return 'A+'
        
        elif marks >= 70 and marks<80: return 'A'
        
        elif marks >= 60 and marks <70: return 'A-'
        
        elif marks >= 50 and marks <60: return 'B'

        elif marks >= 40 and marks < 50: return 'C'

        elif marks >= 33 and marks < 40: return 'D'

        else: return 'F'

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value == 5.00: return 'A+'

        elif value >= 4 and value <= 4.99: return 'A'

        elif value >= 3.0 and value <= 3.99: return 'A-'

        elif value >= 2.5 and value < 3.0: return 'B'

        elif value >= 2.0 and value < 2.5: return 'C'
        
        elif value >= 1.0 and value < 2.0: return 'D'
        
        else: return 'F'

    def ___repr__(self):
        # All Classrooms
        # All Student
        # All Teacher
        # All Subject
        # All Student Results
        pass