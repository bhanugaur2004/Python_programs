# Counting the frequency of elements in a list

numbers = [10, 20, 10, 30, 20, 40, 10, 20, 10, 50]

counted = []

for num in numbers:
    if num not in counted:
        counted.append(num)

for num in counted:
    print(num, "appears", numbers.count(num), "times")

# Without using the count() method
numbers = [10, 20, 10, 30, 20, 40, 10, 20, 10, 50]

counted = []

for num in numbers:
    if num not in counted:
        counted.append(num)

for num in counted:
    frequency = 0
    for value in numbers:
        if value == num:
            frequency = frequency + 1
    print(num, "appears", frequency, "times")

# Using a dictionary
numbers = [10, 20, 10, 30, 20, 40, 10, 20, 10, 50]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

for num, count in frequency.items():
    print(num, "appears", count, "times")