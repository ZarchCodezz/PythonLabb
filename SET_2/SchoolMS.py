class Students:
    def __init__(self,name,enrl):
        self.name = name
        self.enrl = enrl
    
    def stud_info(self):
        print(f"Student Name : {self.name}\nEnrollment no. : {self.enrl}\n")

class Teachers:
    def __init__(self,fname,id,subj):
        self.fname = fname
        self.id = id
        self.subject = subj

    def faculty_details(self):
        print(f"Teacher's name : {self.fname}\nTeacher's ID : {self.id}\nSubject : {self.subject}\n")

class Courses:
    def __init__(self,code,c_name,faculty,div):
        self.name = c_name
        self.code = code
        self.faculty = faculty
        self.div = div

    def course_info(self):
        print(f"Course Name : {self.name}\nCourse code : {self.code}\nTeacher : {self.faculty}\nStudents : {self.div}\n")

def main():
    s = Students("Mohan",1234)
    s.stud_info()

    t = Teachers("Rajiv",2661,"Maths")
    t.faculty_details()

    c = Courses(12986,"CSE","Mr. Gupta","AI-1")
    c.course_info()

if __name__ == "__main__":
    main()
