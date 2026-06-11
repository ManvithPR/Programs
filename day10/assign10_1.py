import numpy as np

# Accept 12 student marks
marks = []

for i in range(12):
    m = int(input(f"Enter mark {i+1}: "))
    marks.append(m)

arr = np.array(marks)

# Highest, Lowest, Average
print("Highest Mark :", np.max(arr))
print("Lowest Mark :", np.min(arr))
print("Average Mark :", np.mean(arr))

# Reshape into 3x4 matrix
matrix = arr.reshape(3, 4)

print("\nReshaped Matrix (3x4):")
print(matrix)

# Row-wise Sum
print("\nRow-wise Sum:")
print(np.sum(matrix, axis=1))

# Column-wise Sum
print("\nColumn-wise Sum:")
print(np.sum(matrix, axis=0))

# Time Complexity
print("\nTime Complexity:")
print("Finding Maximum Mark : O(n)")
print("Calculating Total Sum : O(n)")