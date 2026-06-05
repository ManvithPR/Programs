# Student Marks Analyzer

# Accept marks of 10 students
marks = []

print("Enter marks of 10 students:")
for i in range(10):
    mark = int(input(f"Student {i+1}: "))
    marks.append(mark)

# Display marks in sorted order
sorted_marks = sorted(marks)
print("\nMarks in Sorted Order:")
print(sorted_marks)

# Find highest and lowest mark
print("\nHighest Mark:", max(marks))
print("Lowest Mark:", min(marks))

# Remove duplicate marks using a set
unique_marks = set(marks)
print("\nUnique Marks (Duplicates Removed):")
print(unique_marks)

# Binary Search Function
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Search for a specific mark
search_mark = int(input("\nEnter mark to search: "))

result = binary_search(sorted_marks, search_mark)

if result != -1:
    print(f"Mark {search_mark} found at position {result + 1} in sorted list.")
else:
    print("Mark not found.")

# Accept marks for second class
class2 = []

print("\nEnter 10 marks for Class 2:")
for i in range(10):
    mark = int(input(f"Student {i+1}: "))
    class2.append(mark)

# Find common marks using set intersection
common_marks = set(marks).intersection(set(class2))

print("\nCommon Marks Between Two Classes:")
print(common_marks)