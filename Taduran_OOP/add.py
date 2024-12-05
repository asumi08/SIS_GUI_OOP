class AddStudent:
    def __init__(self, student_list, StudentInfo):
        self.student_list = student_list
        self.StudentInfo = StudentInfo

    def add_initial_students(self, filename):
        initial_students = self.StudentInfo.load_students_from_file(filename)
        for student_info in initial_students:
            self.student_list.append(student_info)
            print(f"Added: {student_info.get_name()}")

    def add_new_student(self):
        name = input("Enter student's name: ")
        age = input("Enter student's age: ")
        student_id = input("Enter student's ID: ")
        email = input("Enter student's email: ")
        phone = input("Enter student's phone: ")
        student_info = self.StudentInfo(name, age, student_id, email, phone)
        self.student_list.append(student_info)
        print(f"Student {name} added successfully!")
        with open('students.txt', 'a') as file:
            file.write(str(student_info) + '\n')