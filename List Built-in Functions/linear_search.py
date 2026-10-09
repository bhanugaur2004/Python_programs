# Linear search on a list of numbers

numbers = [10, 25, 33, 47, 58, 61, 75]

search = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found in the list")

# Using while loop
numbers = [10, 25, 33, 47, 58, 61, 75]

search = int(input("Enter number to search: "))

found = False
i = 0

while i < len(numbers):
    if numbers[i] == search:
        print("Found at index", i)
        found = True
        break
    i = i + 1

if not found:
    print("Not found in the list")

# Using index() method
numbers = [10, 25, 33, 47, 58, 61, 75]

search = int(input("Enter number to search: "))

if search in numbers:
    print("Found at index", numbers.index(search))
else:
    print("Not found in the list")