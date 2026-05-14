# student_management.py

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, marks):
        """Add student with marks and grade."""
        self.students[name] = {
            "marks": marks,
            "grade": self.get_grade(marks)
        }

    def get_grade(self, marks):
        """Calculate grade based on marks."""
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "F"

    def show_all(self):
        """Display all student records."""
        if not self.students:
            print("\nNo student records found.")
            return

        print("\nStudent Records:")
        print("-" * 30)

        for name, data in self.students.items():
            print(f"Name  : {name}")
            print(f"Marks : {data['marks']}")
            print(f"Grade : {data['grade']}")
            print("-" * 30)


# Main Program
manager = StudentManager()

# Taking user input
num = int(input("Enter number of students: "))

for i in range(num):
    print(f"\nEnter details for Student {i + 1}")

    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    manager.add_student(name, marks)

# Display all students
manager.show_all()