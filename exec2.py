# class InvalidAgeError(Exception):
#     pass


# try:
#     age = int(input("Enter age: "))

#     if age < 18:
#         raise InvalidAgeError("Age must be 18 or above.")

#     print("You are eligible.")

# except InvalidAgeError as e:
#     print("Error:", e)

while True:

    try:
        number = int(input("Enter number: "))

        if number < 0:
            print("Positive number required.")
            continue

        break

    except ValueError:
        print("Numbers only.")