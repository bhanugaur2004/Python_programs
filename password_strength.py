password = input("Enter password: ")

score = 0
problems = []

if len(password) >= 8:
    score += 20
else:
    problems.append("At least 8 characters required")

if any(c.isupper() for c in password):
    score += 20
else:
    problems.append("Add an uppercase letter")

if any(c.islower() for c in password):
    score += 20
else:
    problems.append("Add a lowercase letter")

if any(c.isdigit() for c in password):
    score += 20
else:
    problems.append("Add a number")

if any(not c.isalnum() for c in password):
    score += 20
else:
    problems.append("Add a special character")

print("\nPassword Score:", score, "/ 100")

if score == 100:
    print("Strength: Very Strong")
elif score >= 60:
    print("Strength: Strong")
elif score >= 40:
    print("Strength: Medium")
else:
    print("Strength: Weak")

if problems:
    print("\nSuggestions:")
    for problem in problems:
        print("-", problem)