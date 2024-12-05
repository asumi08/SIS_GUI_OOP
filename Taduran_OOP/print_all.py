class PrintAllStudent:
    def __init__(self, student_list):
        self.student_list = student_list

    def display_students(self):
        if not self.student_list:
            print("No students found.")
            return
        print("\n=== All Students ===")
        for student in self.student_list:
            print(student)
        print("====================")