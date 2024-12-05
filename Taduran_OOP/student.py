class StudentInfo:
    def __init__(self, name, age, idnumber, email, phone):
        self._name = name
        self._age = age
        self._idnumber = idnumber
        self._email = email
        self._phone = phone

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_idnumber(self):
        return self._idnumber

    def get_email(self):
        return self._email

    def get_phone(self):
        return self._phone

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_idnumber(self, idnumber):
        self._idnumber = idnumber

    def set_email(self, email):
        self._email = email

    def set_phone(self, phone):
        self._phone = phone

    def __str__(self):
        return f"{self._name}, {self._age}, {self._idnumber}, {self._email}, {self._phone}"


    def from_string(student_str):
        
        if not student_str.strip():
            return None
        try:
            name, age, idnumber, email, phone = student_str.strip().split(', ')
            return StudentInfo(name, age, idnumber, email, phone)
        except ValueError:
            print(f"incorrect format: {student_str.strip()}")
            return None

    
    def load_students_from_file(file_name):
        students = []
        try:
            with open("students.txt", 'r') as file:
                for line in file:
                    student_info = StudentInfo.from_string(line)
                    if student_info:
                        students.append(student_info)
        except FileNotFoundError:
            print(f"File {"students.txt"} not found.")
        return students
