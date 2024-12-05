class LoginPage:
    def __init__(self, student_list):
        self.student_list = student_list

    def login(self):
        attempts = 0
        while attempts < 3:
            student_id = input("==========LOGIN PAGE==========\nEnter your Student ID: ")
            student = next((s for s in self.student_list if s.get_idnumber() == student_id), None)
            if student:
                print("Login successful!")
                return student
            else:
                attempts += 1
                print("Invalid Student ID. Please try again.")
                print(f"You have {3 - attempts} attempts remaining.")
        print("Too many failed attempts. Returning to the main menu.")
        return None