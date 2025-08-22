class Classroom:
    def __init__(self, name, student, subjects):
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        reg_no = f"{self.name} - {len(self.student) + 1}"
        student.id = reg_no
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)

        for student in self.students:
            student.calculate_final_grade()

    def get_top_students():
        pass