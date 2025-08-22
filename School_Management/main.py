from school import School
from person import Student, Teacher
from subject import Subject
from classroom import Classroom

school = School("Neffroxx", "Cumilla")

# Adding Classroom
five = Classroom("five")
six = Classroom("six")
seven = Classroom("seven")
eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school.add_classroom(five)
school.add_classroom(six)
school.add_classroom(seven)
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding Student
sahim = Student("Sahim", five)
mahim = Student("Mahim", six)
zahim = Student("Zahim", seven)
oahim = Student("Oahim", five)
jahim = Student("Jahim", eight)
nahim = Student("Nahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hamim = Student("Hamim", ten)
rahim = Student("Ramim", nine)

school.student_admission(sahim)
school.student_admission(mahim)
school.student_admission(zahim)
school.student_admission(oahim)
school.student_admission(jahim)
school.student_admission(nahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)
school.student_admission(rahim)

# Adding Teachers
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")
sabul = Teacher("Sabul Khan")
mabul = Teacher("Mabul Khan")
jabul = Teacher("Jabul Khan")

# Adding Subjects
bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)
biology = Subject("Biology", sabul)
math = Subject("Math", mabul)
english = Subject("English", jabul)

five.add_subject(bangla)
five.add_subject(physics)
five.add_subject(chemistry)
five.add_subject(math)
five.add_subject(english)

six.add_subject(bangla)
six.add_subject(physics)
six.add_subject(chemistry)
six.add_subject(math)
six.add_subject(english)

seven.add_subject(bangla)
seven.add_subject(physics)
seven.add_subject(chemistry)
seven.add_subject(math)
seven.add_subject(english)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
eight.add_subject(math)
eight.add_subject(english)

nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
nine.add_subject(math)
nine.add_subject(english)

ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)
ten.add_subject(math)
ten.add_subject(english)

five.take_semester_final_exam()
six.take_semester_final_exam()
seven.take_semester_final_exam()
eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)