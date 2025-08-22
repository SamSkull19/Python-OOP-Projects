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

    def student_admission(self, student):
        classname = student.classroom.name
        self.classroom[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
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

    def __repr__(self):
        # All Classrooms
        for key in self.classroom.keys():
            print(key)

        # All Student
        print("----All Student----")
        result = ''
        for key, value in self.classroom.items():
            result += f"--- {key.upper()} Classroom Students\n"
            for val in value.students:
                result += f"{val.name}\n"
        print(result)    

        # All Subject
        print("----All Subjects----")
        subject = ''
        for key, value in self.classroom.items():
            subject += f"--- {key.upper()} Classroom Subjects\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject) 


        # All Teacher
        
        # All Student Results
        print("----All Student Results----")

        for key, value in self.classroom.items():
            for student in value.students:
                for k, i in student.marks.items():
                    print(student.name, k, i, student.subject_grade[k])
                print(student.calculate_final_grade())
                print(student.calculate_total_marks())

        print("----Topper Students----")

        topper = ''
        for key, value in self.classroom.items():
            topper += f"Class {key.upper()} - \t"
            top = value.get_top_students()

            if top:
                topper += f"Topper Name : {top.name},\t GPA: {top.gpa:.2f} ({top.grade}) Total Marks: {top.calculate_total_marks()}\n"
            
            else:
                topper += f"No students yet.\n"

        print(topper)

        return ''