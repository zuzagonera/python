class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50


student_1 = Student("Zuzanna", [59, 98, 82, 75])
student_2 = Student("Jan", [50, 39])
print(student_1.is_passed())
print(student_2.is_passed())

