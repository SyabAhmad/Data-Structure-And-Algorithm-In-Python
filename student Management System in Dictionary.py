print("Small Student Management System using Dictionary in Python")

class teacherData:
    teacherList = {}
    studentList = {}

    def addingNewTeacher(self, name, salary, ID, age, phoneNumber):
        if ID in self.teacherList.values():
            print("Teacher Already Exist with spacific ID, try deferent one")
        else:
            self.teacherList["name"] = name
            self.teacherList["phoneNumber"] = phoneNumber
            self.teacherList["age"] = age
            self.teacherList['salary'] = salary
            self.teacherList["ID"] = ID

            print("Teacher Added Successfully")


    def DIsplayListOfTeachers(self):
        print(self.teacherList)


class studentData(teacherData):
    def addingNewSTudent(self, name, rollNumber, age, phoneNumber):
        if rollNumber in self.teacherList.values():
            print("Student Already Exist with spacific Roll Number, try deferent one")
        else:
            self.studentList["name"] = name
            self.studentList["phoneNumber"] = phoneNumber
            self.studentList["age"] = age
            self.studentList["rollNumber"] = rollNumber

            print("Student Added Successfully")


    def DIsplayListOfStudent(self):
        print(self.studentList)


# Adding New Teacher
teacherdata = teacherData()
teacherdata.addingNewTeacher("MR. Shah", 45000, 1, 45, 9823423222)
teacherdata.DIsplayListOfTeachers()


# adding New Student
studentdata = studentData()
studentdata.addingNewSTudent("MR. Developer", 206274, 35,923469745939)
studentdata.DIsplayListOfStudent()


