s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

common = ""

for char in s1:
    if char in s2 and char not in common:
        common += char

print("Common characters: ", common)