student = {
    "name": "Rahul",
    "age": 21,
    "course": "MCA"
}

print(student)
for key in student:
    print(key)

for values in student.values():
    print(values)

for key, value in student.items():
    print(key, value)

print(len(student))

student2 = dict(name="xyz",age2=20,course="B.Tech")
print(student2)

print(student2.keys())
print(student2.values())
print(student2.items())

print(student2["age2"])
print(student2.get("age2"))

print(student2.get("age3"))
# print(student2["age3"])  # This will raise a KeyError since "age3" does not exist in the dictionary

student = {
    "name": "Rahul",
    "age": 21
}

student.update({"course": "MCA"})
student.update({"age": 22})

# print(student)

print(student)

del student["age"]
print(student)

student.clear()
print(student)

keys = ["name", "age", "course"]

print(keys)

student = dict.fromkeys(keys)
print(student)
# print(keys)

student= dict.fromkeys(keys,"Not Available")
# student= dict.fromkeys(keys,"Not Available", "Available", "available soon")
print(student)


student = {
    "name": "Rahul",
    "age": 21
}

new_student = student.copy()

print(new_student)

print()
print()


student = {
    "name": "Rahul",
    "age": 21,
    "course": "MCA"
}

value = student.pop("age")
# value = student.pop()# Atleast one argument (key) is required for pop() method

print("Removed value:", value)
print(student)

print()
print()

student = {
    "name": "Rahul",
    "age": 21,
    "course": "MCA"
}

item = student.popitem()

print("Removed item:", item)
print(student)

student = {
    "name": "Rahul",
    "age": 21
}

print(student.setdefault("name", "Amit")) #This only adds if the key "name" does not exist, otherwise it returns the existing value, also it can't update the value of an existing key.

print(student.setdefault("course", "MCA"))

print(student)

student["sem"] = 1 #This adds or updates the key "sem" with the value 1
student["name"] = "Amit"

print(student)

print(max(student))

marks = {
    "Rahul": 85,
    "Amit": 92,
    "Riya": 78
}

print(max(marks.values()))
print(min(marks.values()))