# Nested list - a list inside a list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix)
print(matrix[0])
print(matrix[1][2])
print(matrix[2][0])

# Loop through a nested list
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Accessing rows and elements
students = [["Aman", 85], ["Riya", 92], ["John", 78]]

print(students[0][0])
print(students[1][1])

# Modifying a nested list
matrix[0][1] = 99
print(matrix)

matrix.append([10, 11, 12])
print(matrix)

matrix[1].append(100)
print(matrix)

# Nested list with different sizes
jagged = [[1, 2], [3, 4, 5], [6]]

for row in jagged:
    print(row)