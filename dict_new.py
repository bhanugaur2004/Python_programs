student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
}

print(student)

print(student["name"])  # Accessing the value associated with the key "name"
print(student["age"])

student["city"] = "Jaipur"

print(student)

student["city"] = "Jodhpur"

print(student)

del student["city"]

print(student)

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key," : ",value)

print(len(student))

student = dict(name = "Rahul", age = 21, course = "B.Tech")
print(student)

student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
}

print(student.keys())
print(student.values())
print(student.items())

#get()

print(student.get("age"))
print(student["age"])

print(student.get("course")) #None
# print(student["course"])# Error

#clear()

student.clear()
print(student)

#formkeys()

keys = ["name","age","course"]

student2 = dict.fromkeys(keys)

print(student2)

#copy()

new_student = student2.copy()
print(new_student)

#pop()

student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
}

value = student.pop("age")
print("Removed value: ",value)
print(student)

#popitem()

student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
}

item = student.popitem()
print("Removed item: ", item)
print(student)

student = {
    "name": "John Doe",
    "age": 20,
    "city": "Jaipur"
}

#setdefault()

print(student.setdefault("course","B.Tech"))
print(student.setdefault("name","Sanjana"))
print(student)

# a = [1,2]
# b = [1,2]
# print(a is b)
# print(id(a))
# print(id(b))

a = [1,2]
b = a
print(a is b)
print(id(a))
print(id(b))