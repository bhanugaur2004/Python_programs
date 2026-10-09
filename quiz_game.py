questions = [
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["6", "8", "9", "12"],
        "answer": "B",
        "marks": 2
    },
    {
        "question": "Which data type is immutable?",
        "options": ["List", "Set", "Tuple", "Dictionary"],
        "answer": "C",
        "marks": 3
    },
    {
        "question": "Which keyword creates a function?",
        "options": ["func", "define", "def", "function"],
        "answer": "C",
        "marks": 2
    },
    {
        "question": "Which structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "B",
        "marks": 3
    }
]

score = 0
total_marks = 0
wrong = []

for i, q in enumerate(questions, 1):

    print(f"\nQuestion {i}")
    print(q["question"])

    for j, option in enumerate(q["options"]):
        print(chr(65 + j) + ".", option)

    answer = input("Your answer: ").upper()

    total_marks += q["marks"]

    if answer == q["answer"]:

        print("Correct!")
        score += q["marks"]

    else:

        print("Wrong!")
        wrong.append(i)

print("\n========== RESULT ==========")

print("Score:", score)
print("Total Marks:", total_marks)

percentage = score / total_marks * 100

print(f"Percentage: {percentage:.2f}%")

print("Correct:", len(questions) - len(wrong))
print("Wrong:", len(wrong))

if wrong:
    print("Wrong Questions:", wrong)