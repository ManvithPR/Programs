# Student Attendance Analyzer

# Input total students
n = int(input("Enter total number of students: "))

students = []

print("\nEnter student names:")
for i in range(n):
    name = input(f"Student {i+1}: ")
    students.append(name)

# Input present students
p = int(input("\nEnter number of present students: "))

present_students = []

print("\nEnter names of present students:")
for i in range(p):
    name = input(f"Present Student {i+1}: ")
    present_students.append(name)

# Find absent students
absent_students = []

for student in students:
    if student not in present_students:
        absent_students.append(student)

# Display present students
print("\n--- Present Students ---")
for student in present_students:
    print(student)

# Display absent students
print("\n--- Absent Students ---")
for student in absent_students:
    print(student)

# Display counts
print("\n--- Attendance Summary ---")
print("Total Present Students:", len(present_students))
print("Total Absent Students:", len(absent_students))

# Sort present students
present_students.sort()

print("\n--- Present Students (Ascending Order) ---")
for student in present_students:
    print(student)