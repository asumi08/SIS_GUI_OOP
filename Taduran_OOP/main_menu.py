from add import AddStudent
from student import StudentInfo
from print_all import PrintAllStudent
from search import SearchStudent
from login_page import LoginPage

class MainMenu:
    def __init__(self):
        self.student_list = []
        self.add_student = AddStudent(self.student_list, StudentInfo)
        self.add_student.add_initial_students('students.txt')
        self.login_page = LoginPage(self.student_list)
        self.print_students = PrintAllStudent(self.student_list)
        self.search = SearchStudent(self.student_list)

    def show_menu(self):
        logged_in_student = self.login_page.login()  

        while True:
            if logged_in_student is None:
                print("No student logged in. Exiting.")
                break

            print(f"\nWelcome, {logged_in_student.get_name()}!")  
            print("""Pick one of the following options:\n1. View your information\n2. View other student's information\n3. Register a New Student\n4. Print all students in the list\n5. To quit""")
            choice = input("Your choice: ")

            if choice == "1":
                print("\n=== Student Information ===\n")
                print(f"Name: {logged_in_student.get_name()}")
                print(f"Age: {logged_in_student.get_age()}")
                print(f"ID: {logged_in_student.get_idnumber()}")
                print(f"Email: {logged_in_student.get_email()}")
                print(f"Phone: {logged_in_student.get_phone()}")
                print("\n=== Nothing Follows ===")
            elif choice == "2":
                keyword = input("Enter Student ID: ")
                print(self.search.search_student(keyword))
            elif choice == "3":
                self.add_student.add_new_student()
            elif choice == "4":
                self.print_students.display_students()
            elif choice.lower() == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


