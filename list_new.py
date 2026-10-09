numbers = [10,20,30,40]
mixed = [10,"Python",3.5,True]

print(numbers)
print(mixed)

print(mixed[1])
print(mixed[2])

list1 = [1,2,3]
list2 = [4,5,6]

result = list1 + list2

print(result)

numbers = [1,2,3]

result = numbers * 3

print(result)

#Membership operator

numbers = [10,20,30,40,50,60]

print(20 in numbers)
print(70 in numbers)
print(70 not in numbers)

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])

print()
print()

for num in numbers:
    print(num,end=" ")

print()
numbers = [10,20,30,40,50,60]
print(len(numbers))

i = 0
while i<len(numbers):
    print(numbers[i],end=" ")
    i+=1

print()

a = [1,2,3]
# b = a
b = [1,2,3]
print(a is b)

print(id(a))
print(id(b))

print()
text = "Python"

result = list(text)
print(result)

t = (10,20,30)

result = list(t)
print(result)

text = 20
# result = list(text)
result = str(text)
result2 = list(result)
print(result2)

numbers = [10,20,30]
# numbers.append([40,50])
print(numbers)

numbers.extend([40,50])
print(numbers)

numbers.insert(2,25)

print(numbers)

text = [10,20,30]

# print(text.index(50))

# text.remove(20)
# print(text)

# text.pop()
# print(text)

text.pop(1)
print(text)

numbers = [10,20,30,40,50,60]

numbers.reverse()

print(numbers)


#sort()

numbers = [50,40,20,10,30,70]

# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)

# print(numbers)

#sorted()

numbers = [50,40,20,10,30,70]

# new_list = sorted(numbers)
new_list = sorted(numbers, reverse=True)

print(numbers)
print(new_list)

numbers = [50,40,20,10,30,70]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#Nested List

data = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(data)
print(data[0])
print(data[1][2])

for row in data:
    for element in row:
        print(element, end=" ")
    print()

    


numbers = [45,12,78,23,56]

maximum = numbers[0]

for num in numbers:
    if num>maximum:
        maximum = num

print("Maximum Value ",maximum)

print()
print()
print()



# numbers = [10,25,30,45,50]

# key = int(input("Enter the number to search: "))

# found = False

# for num in numbers:
#     if key == num:
#         found = True

# if found:
#     print("Element found at index: ",numbers.index(key))
# else:
#     print("Element not found")



# text = [10,20,30,40,50]

# num = int(input("Enter the number you want to remove: "))

# if num in text:
#     text.remove(num)
#     print("Updated list: ",text)
# else:
#     print("Element not found")

#pop()

numbers = [10,20,30,40,50]

removed = numbers.pop()

print("Removed element: ",removed)
print("Updated list: ",numbers)

numbers = [10,20,30,40,50]

numbers.pop(2)

print(numbers)


text = "python"

print(text[::-1])

numbers = [10,20,30,40,50]

numbers.reverse()

print(numbers)

#sort()

numbers = [50,40,30,20,10]

numbers.sort()

print(numbers)

numbers = [10,20,30,40,50]
numbers.sort(reverse=True)
print(numbers)

#sorted()
numbers = [20,10,40,50,30]
new_list = sorted(numbers)
print(new_list)
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = [45,12,78,23,56]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value: ", maximum)


