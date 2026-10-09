numbers = [10, 20, 30, 40, 50]
names = ["Aman", "Riya", "John"]
mixed = [10, "Hello", 3.5, True]

print(numbers)
print(names)
print(mixed)


fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[2])
print(fruits[-1])

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)


numbers = [1, 2, 3]

result = numbers * 3

print(result)


numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)

numbers = [10, 20, 30, 40]

print(50 not in numbers)

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

numbers = [10, 20, 30, 40, 50]

print(len(numbers))


numbers = [10, 20, 30, 40, 50]

i = 0

while i < len(numbers):
    print(numbers[i], end=" ")
    i += 1

print()

text = "Python"

result = list(text)

print(result)

text = 20

# result = list(text) #Error: 'int' object is not iterable
result = list(str(text))  # Convert the integer to a string before converting to a list

print(result)

t = (10, 20, 30)

print(list(t))


numbers = [10, 20, 30]

numbers.append(40)

print(numbers)


numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print(numbers)


a = [1, 2, 3]
# a.append(4,5)# Error: append() takes exactly one argument (2 given)
a.append([4, 5])
print(a)
print(a[3])

b = [1, 2, 3]
b.extend([4, 5])
print(b)


numbers = [10, 20, 40, 50]

numbers.insert(2, 30)

print(numbers)


numbers = [10, 20, 10, 30, 10, 40]

print(numbers.count(10))

numbers = [10, 20, 30, 40, 30]

print(numbers.index(30))
# print(numbers.index(70)) #Error: 70 is not in list

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)

numbers = [10, 20, 30, 40]

removed = numbers.pop()

print("Removed:", removed)
print("List:", numbers)

numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print("Removed:", removed)
print("List:", numbers)

numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)


numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)

numbers = [50, 10, 40, 20, 30]

new_list = sorted(numbers)

print("Original:", numbers)
print("Sorted:", new_list)

numbers = [50, 10, 40, 20, 30]

print(sorted(numbers, reverse=True))


numbers = [50, 10, 40, 20, 30]

print(min(numbers))

numbers = [50, 10, 40, 20, 30]

print(max(numbers))

numbers = [10, 20, 30, 40, 50]

print(sum(numbers))

#Nested lists

data = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(data)
print(data[0])
print(data[1][2])

for row in data:
    for item in row:
        print(item, end=" ")
    print()


#Find maximum values in a list without using max() function

numbers = [45, 12, 78, 23, 56]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value:", maximum)


#Linear Search

numbers = [10, 25, 30, 45, 50]

key = int(input("Enter number to search: "))

found = False

for num in numbers:
    if num == key:
        found = True
        print("Element found at index:", numbers.index(num))
        break

if found:
    print("Element found")
else:
    print("Element not found")


# numbers = [10, 25, 30, 45, 50]

# key = int(input("Enter number to search: "))

# for i in range(len(numbers)):
#     if numbers[i] == key:
#         print("Element found at index:", i)
#         break
# else:
#     print("Element not found")


numbers = [10, 20, 10, 30, 20, 10, 40]

checked = []

for num in numbers:
    if num not in checked:
        frequency = 0

        for value in numbers:
            if value == num:
                frequency += 1

        print(num, "occurs", frequency, "times")
        checked.append(num)
print(checked)