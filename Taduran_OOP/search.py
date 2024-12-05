class SearchStudent:
    def __init__(self, student_list):
        self.student_list = student_list

    def search_student(self, keyword):
        results = [student for student in self.student_list if any(keyword.lower() in str(value).lower() for value in vars(student).values())]
        
        if not results:
            return "No students found matching the search criteria."

        output = "\n=== Search Results ==="
        for student in results:
            output += str(student)
        output += "\n======================"
        
        return output
