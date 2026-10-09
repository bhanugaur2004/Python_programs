# Finding maximum, minimum and mean of numeric values in a list

numbers = [45, 12, 78, 3, 56, 90, 34]

# Using built-in functions
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Mean:", sum(numbers) / len(numbers))

# Without using built-in functions
numbers = [45, 12, 78, 3, 56, 90, 34]

maximum = numbers[0]
minimum = numbers[0]
total = 0

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
    total = total + num

mean = total / len(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Mean:", mean)

# Taking values from the user
numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    value = float(input("Enter number: "))
    numbers.append(value)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Mean:", sum(numbers) / len(numbers))