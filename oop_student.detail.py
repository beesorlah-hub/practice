
class Student:

    def __init__(self,name,matric_no,course):
        self.name = name
        self.matricno = matric_no
        self.course = course
    
    def student_name(self, name):
        self.name = name
        print(self.name)

    def matric_no(self, matric_no):
        self.matricno = matric_no
        print(self.matricno)

    def course_of_study(self, course_of_study):
        self.course_of_study = course_of_study
        print(self.course_of_study)


c2018 = Student("Bisi","sci18chm004","Chemistry")
c2018.student_name("Bisi")
c2018.matric_no("sci18chm004")
c2018.course_of_study("Chemistry")
c2018 = Student("Akym","sci18MEH001","Mechanical Engineering")
c2018.student_name("Akym")
c2018.matric_no("sci18MEH001")
c2018.course_of_study("Mechanical Engineering")
c2018 = Student("Tomi","sci18CSC030","Computer Science")
c2018.student_name("Tomi")
c2018.matric_no("sci18CSC030")
c2018.course_of_study("Computer Science")