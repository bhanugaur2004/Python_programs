class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))
try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
except InvalidAgeError as e:
    print(f"Error: {e}")
else:
    print("You are eligible.")
