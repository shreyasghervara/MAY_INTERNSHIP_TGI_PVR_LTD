# student_manager.py

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, marks):
        """Add a student with marks and calculated grade."""
        self.students[name] = {
            "marks": marks,
            "grade": self.get_grade(marks)
        }

    def get_grade(self, marks):
        """Return grade based on marks."""
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "F"

    def show_all(self):
        """Display all students."""
        if not self.students:
            print("No students found.")
            return

        print("Student Records:")
        for name, data in self.students.items():
            print(f"- {name}: {data['marks']} marks (Grade {data['grade']})")


# Main Program
manager = StudentManager()

manager.add_student("Alice", 92)
manager.add_student("Bob", 78)

manager.show_all()