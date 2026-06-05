class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate(self):
        self.total = sum(self.marks)
        self.average = self.total / len(self.marks)
        self.highest = max(self.marks)
        self.lowest = min(self.marks)

        self.above_average = 0
        for mark in self.marks:
            if mark > self.average:
                self.above_average += 1

    def display(self):
        print("\n--- Student Performance Report ---")
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total)
        print("Average:", self.average)
        print("Highest Mark:", self.highest)
        print("Lowest Mark:", self.lowest)
        print("Subjects Above Average:", self.above_average)


# Input
name = input("Enter Student Name: ")

marks = []
print("Enter 5 Subject Marks:")
for i in range(5):
    mark = int(input(f"Subject {i+1}: "))
    marks.append(mark)

# Object Creation
student = Student(name, marks)

# Processing
student.calculate()

# Output
student.display()