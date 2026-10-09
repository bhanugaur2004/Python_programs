import math

print(math.pi)

r = 20

a = math.pi * r * r
print(a)

print(math.e)

print(math.sqrt(16))

print(math.ceil(4.2))
print(math.ceil(-4.8))

print(math.floor(4.2))
print(math.floor(-4.8))

print(math.pow(2, 3))
print(math.pow(3, 2))

# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))

# result = math.pow(base, exponent)
# print(f"{base} raised to the power of {exponent} is: {result}")

print(math.fabs(-5.5))
print(math.fabs(10))
print(math.fabs(10.2))
print(math.fabs(-10.2)) #Math.fabs() is faster than abs() because it is implemented in C and does not have to check the type of the input. However, abs() can handle more types of inputs, such as complex numbers.

print(abs(-5.5))
print(abs(10))
print(abs(10.2))
print(abs(-10.2))

# print(math.fabs(2+3j)) # This will raise a TypeError because math.fabs() does not support complex numbers.
print(abs(2+3j))

print(math.sin(0))
print(math.cos(0))


import statistics

numbers = [10, 20, 30, 40, 50, 60]

print(statistics.median(numbers))