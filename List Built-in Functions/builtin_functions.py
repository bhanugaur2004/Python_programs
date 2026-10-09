# sorted() - returns a new sorted list (original list unchanged)
numbers = [40, 10, 30, 20, 50]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Original:", numbers)
print("Ascending:", ascending)
print("Descending:", descending)

# sorted() works on strings too
names = ["Riya", "Aman", "John", "Zara"]
print(sorted(names))
print(sorted(names, reverse=True))

# min() and max() - smallest and largest value
numbers = [45, 12, 78, 3, 56]

print("Smallest:", min(numbers))
print("Largest:", max(numbers))

print(min(10, 20, 5, 30))
print(max("apple", "banana", "mango"))

# sum() - total of all values
numbers = [10, 20, 30, 40, 50]

print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

# sum() can take a starting value
print(sum(numbers, 100))