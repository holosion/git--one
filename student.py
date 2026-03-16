class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.average = self.calculate_average()

    def calculate_average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}, Average: {self.average:.2f}"