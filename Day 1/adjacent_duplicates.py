s = input("Enter a string: ")
result = ""
for char in s:
    if result == "" or char != result[-1]:
        result += char
print("After removing adjacent duplicates: ", result)