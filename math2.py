import math

print(math.pi)

r = 2

a = math.pi * r * r

print(a)

print(math.e)

print(math.sqrt(25))
print(math.sqrt(36))


print(math.fabs(-5))
print(math.fabs(10))
print(math.fabs(-5.5))

print(abs(-5.5))
print(abs(-5))

# print(math.fabs(2+3j))

print(abs(2+3j))

print(math.ceil(3.2))
print(math.ceil(-3.2))

print(math.floor(4.8))
print(math.floor(-4.8))

print(math.pow(2,3))

print(math.sin(0))
print(math.cos(0))

angle = 90

radians = math.radians(angle)

print(math.sin(radians))

print(math.cos(math.pi/2))

import random

for i in range(5):
    print(random.random())

import random

print(random.randint(1,10))

print(random.randrange(1,10))

print(random.randrange(0,20,2))

import statistics

numbers = [10,20,30,40,50]

result = statistics.mean(numbers)

print(result)

numbers = [10,20,30,40]

result2 = statistics.median(numbers)

print(result2)

numbers = [10,20,20,30,40]

result = statistics.mode(numbers)

print(result)

def greet():
    print("Hello Python")

greet()

def show_details():
    print("BCA")
    print("Lords University")

show_details()


def greet(name):
    print("Hello", name)

greet("Rahul")

def add(a,b):
    print(a+b)

def add2(c,d):
    return c + d





