class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def calculate_average(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def subject_average(self, subject):
        if subject not in self.grades or not self.grades[subject]:
            return 0
        return sum(self.grades[subject]) / len(self.grades[subject])

def main():
    students = {}

    while True:
        print("\n--- Student Grades Tracker ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Averages")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            if name not in students:
                students[name] = Student(name)
                print(f"Student {name} added.")
            else:
                print("Student already exists.")

        elif choice == '2':
            name = input("Enter student's name: ")
            if name in students:
                subject = input("Enter subject: ")
                try:
                    grade = float(input("Enter grade: "))
                    students[name].add_grade(subject, grade)
                    print(f"Grade {grade} added for {subject}.")
                except ValueError:
                    print("Invalid grade. Please enter a numeric value.")
            else:
                print("Student not found.")

        elif choice == '3':
            name = input("Enter student's name: ")
            if name in students:
                student = students[name]
                print(f"\nGrades for {student.name}:")
                for subject, grades in student.grades.items():
                    print(f"{subject}: {grades} (Average: {student.subject_average(subject):.2f})")
                print(f"Overall Average: {student.calculate_average():.2f}")
            else:
                print("Student not found.")

        elif choice == '4':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
