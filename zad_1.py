class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50


student0 = Student("Zuzanna", [59, 98, 82, 75])
student1 = Student("Jan", [50, 39])
print(student0.is_passed())
print(student1.is_passed())

