student = {
    "name": "Rahul",
    "age" : 21,
    "course": "CSE"
}

print(student)
print(student["age"])

student["city"] = "Jaipur"

print(student)

student["age"] = 22
print(student)

del student["age"]

print(student)

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key,":",value)

#len()

print(len(student))

student = dict(name = "Amit", age = 21, course = "B.Tech")
print(student)

student = {
    "name": "Rahul",
    "age" : 21,
    "course": "CSE"
}

print(student.keys())
print(student.values())
print(student.items())

#get()

print(student.get("name"))
print(student.get("city"))
# print(student["city"])

#clear()
student.clear()
print(student)

#formkeys()

keys = ["name","city","class"]

student = dict.fromkeys(keys)

print(student)

student = dict.fromkeys(keys,"Not available")
print(student)

#copy()

new_student = student.copy()
print(new_student)

#pop()

value = student.pop("city")

print("Removed item: ", value)
print(student)

#popitem

value = student.popitem()

print("Removed item: ", value)
print(student)

student = {
    "name": "Rahul",
    "age" : 21
}

print(student.setdefault("course","B.Tech"))
print(student.setdefault("name","Amit"))

# print(student["name"]) = "Amit 2"

print(student)

marks = {
    "Rahul": 85,
    "Sanjana": 90,
    "Priya" : 89
}

print(max(marks.values()))
print(min(marks.values()))
