class student:
    def __init__(self, name: str, marks: list[float]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50


student1 = student("Anna", [70, 65, 80])
student2 = student("Daniel", [40, 20, 35])

print(student1.is_passed())
print(student2.is_passed())
