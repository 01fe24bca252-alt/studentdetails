"""
Student Grading System
"""

def compute_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if 90 <= average <= 100:
        return "S"
    elif 80 <= average < 90:
        return "A"
    elif 65 <= average < 80:
        return "B"
    elif 50 <= average < 65:
        return "C"
    elif 40 <= average < 50:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter Student Name       : ")
    department = input("Enter Department         : ")
    semester = input("Enter Semester           : ")

    subject1 = int(input("Enter Subject 1 Marks    : "))
    subject2 = int(input("Enter Subject 2 Marks    : "))
    subject3 = int(input("Enter Subject 3 Marks    : "))

    marks = [subject1, subject2, subject3]
    average = compute_average(marks)
    grade = calculate_grade(average)

    print("\n------ STUDENT RESULT ------")
    print("Name       :", name)
    print("Department :", department)
    print("Semester   :", semester)
    print("Marks      :", marks)
    print("Average    :", average)
    print("Grade      :", grade)


if __name__ == "__main__":
    main()
