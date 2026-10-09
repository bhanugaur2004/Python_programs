name = "xyz"
print(name)

a = ""
print(len(a))
print(a)

print(len(name))
print(name[0])
print(name[-1])

# name[1] = "h" #Immuatble
print(name)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

a = "Hello"
b = "World"
print(a + " " + b)

age = 20

# print("Age "+ age)
print("Age "+ str(age))

print(f"Age {age}")

print("Hi " * 10)

print("-"*30)
print("Student Report")
print("-"*30)

text = "Python is a programming language. Python is easy to learn."

print("Python" in text)
print("Java" in text)

word = "Python"
print(word in text)
print("p" in word)
print("P" in word)
print("y" in word)
print("H" in word)

print("Java" not in text)
print("Python" not in text)

# string[start:stop]

word = "Python"
print(word[0:3])
print(word[2:5])
print(word[0:90])

print(word[:4])

print(word[2:])

print(word[-4:-1])

new_word = "Hello"
copy = new_word[:]
print(copy)

# string[start : stop : step]

new_word2 = "Hello World"
print(new_word2[::2])

new_word3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(new_word3[1:20:3])

new_word4 = "Yeahhhhhhh"
print(new_word4[::-1])

text2 = "Python is a programming language. Python is easy to learn."

for ch in text2:
    print(ch,end=" ")

print()
print()
print()
print()

for i in range(len(text2)):
    print(i,text2[i],end=" ")

j=0

while j<len(text2):
    print(j,text2[j],end=" ")
    j+=1

print()
print()
new_text = "Python programming"

count = 0

for ch in new_text.lower():
    if ch in "aeiou":
        count+=1

print(f"Number of vowels in '{new_text}' is {count}")

text2 = "PyTHonABC"

count = 0

for ch in text2:
    if ch.isupper():
        count += 1

print(count)


#Built in functions

word_5 = "python"
print(len(word_5))

print(word_5.capitalize())

word_6 = "pYTHON PROGRAMMING"
print(word_6.capitalize())

word_7 = "python programming language"
print(word_7.title())
print(word_7.capitalize())

word_8 = "PYTHON programming"
print(word_8.lower())


# answer = input("Enter yes or no: ")

# if answer.lower() == "yes":
#     print("You selected Yes")

# YES
# Yes
# yes
# yEs


word_9 = "banana"
print(word_9.count("a"))

text = "hello hello hello"

print(text.count("hello"))

print(word_9.count("a",2,5))

text = "hello world"
print(text.find("world"))
print(text.find("Python"))

print(text.index("world"))
# print(text.index("Python")) #ValueError