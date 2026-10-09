text = "python"
print(text)
print(type(text))

x = "hello"
print(x)
print(len(x))

word = "Python"
print(word[0])
print(word[1])
print(word[2])
print(word[-1])
print(word[-2])
print(word[-3])

text2 = "xyz"
# text2[0] = "h"
print(text2)

text2 = "hyz"
print(text2)

#Concatenation

first_name = "John"
last_name = "Smith"

full_name = first_name + " " + last_name

print(full_name)

a = "hello"
b = "world"

print(a+ " "+b)

age = 20

# print("Age: " + age)
print("Age: " + str(age))

print(f"Age {age}")

#Repetition

print("hi " * 3)
print("hello " * 30)
print()
print()

print("-"*30)
print("Student Report")
print("-"*30)

#Membership operator

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Python" not in text)
print("Java" not in text)

#String slicing

#string[start:stop]

word = "Python"
print(word[0:3])
print(word[2:5])
print(word[0:90])
print(word[:4])
print(word[2:])
copy = word[:]
print(copy)

print(word[-4:-1])

#string[start:stop:step]

word = "PYTHON"
print(word[::2])

word_2 = "ABCDEFGHIJKLMNOP"
print(word_2[1:9:3])

print(word[::-1])

#Traversing String using Loops

text = "Python"

for ch in text:
    print(ch, end="")

print()    
print()    

for i in range(len(text)):
    print(i,text[i])

print()
print()

text = "Python"

i = 0

# while i<len(text):
#     print(text[i],end=" ")
#     # i+=1

text = "python programming"
count = 0

for ch in text:
    if ch in "aeiou":
        count+=1

print(f"Number of vowels in '{text}' are {count}")

# Built In functions

name = "Python"
print(len(name))
print(name.upper())

word_3 = "python programming"
print(word_3.capitalize())
print(word_3.title())

word_4 = "PYTHON"
print(word_4.lower())

# xy = input("Enter either yes or no: ")

# if xy.lower() =="yes":
#     print("You have selected yes")

#Yes
#YES
# yEs
# yes    


text = "apple banana apple mango banana apple"
print(text.count("apple"))
text = "banana  mango banana "
print(text.count("apple"))

text = "Python Programming"

print(text.find("Program"))
print(text.find("python"))

print(text.index("Program"))
# print(text.index("python"))

#find()

text = "Python Programming"

print(text.find("Programming"))
print(text.find("Java"))

#index()
text = "Python Programming"

print(text.index("Python"))
# print(text.index("Java")) #Error

#endswith()

filename = "report.pdf"
print(filename.endswith("pdf"))

email = "xyz@gmail.com"
print(email.endswith("@gmail.com"))

text = "Python"
print(text.endswith("ON"))
print(text.endswith("on"))

#startswith()

text = "Python Programming"
print(text.startswith("Python"))
print(text.startswith("python"))

#isalnum()

#Alphabets = A-Z, a-z
#numeric = 0-9
print()
print()
print()
text = "Python123"
text2 = "Python 123"
print(text.isalnum())
print(text2.isalnum())

#isaplha()

text = "Python"
print(text.isalpha())
text = "Python123"
print(text.isalpha())

#isdigit()

text = "12345"
print(text.isdigit())
print(type(text))

text = "123abc"
print(text.isdigit())

# age = input("Enter your age: ")

# if age.isdigit():
#     print("Valid age")
# else:
#     print("Please enter it in digits.")

#islower()

text = "python"
print(text.islower())
text = "Python"
print(text.islower())

#isupper()
text = "PYTHON"
print(text.isupper())
text = "PyTHON"
print(text.isupper())

#isspace()
# name = input("Enter your name ")
# print(name)

text = "  "
print(text.isspace())
text = "Hello  World"
print(text.isspace())

# name = input("Enter your name: ")

# if name.isspace() or name == "":
#     print("Please enter valid name.")
# else:
#     print("Welcome",name)

#lstrip()

text = "       Python"
print(text)
print(text.lstrip())

#rstrip()

text = "Python       "
print(text)
print(text.rstrip())

#strip()

text = "        Hello       "
print(text.strip())

#replace()

text = "I like Java"
new_text = text.replace("Java","Python")
print(new_text)

text = "banana"
print(text.replace("a","o"))

text = "1 2 3 4 5 6 7 8 9"
print(text.replace(" ", "-"))

text = "hello world"
text.replace("world", "python")
print(text)


text = "hello world"
text = text.replace("world", "python")
print(text)

#join()

words = ["Python", "Java", "C++"]
print(words)
result = " ".join(words)
print(result)