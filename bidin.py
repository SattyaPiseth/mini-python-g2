# ================================
#        Welcome to the Quiz
# ================================

quiz = [
    {
        "question": "1) What does 'CPU' stand for in computer technology?",
        "options": ["A) Central Processing Unit",
                    "B) Computer Processing Unit",
                    "C) Central Performance Unit",
                    "D) Computer Performance Unit"],
        "answer": "A"
    },
    {
        "question": "2) Who is known as the father of the World Wide Web?",
        "options": ["A) Bill Gates",
                    "B) Steve Jobs",
                    "C) Tim Berners-Lee",
                    "D) Mark Zuckerberg"],
        "answer": "C"
    },
    {
        "question": "3) What does 'HTTP' stand for?",
        "options": ["A) HyperText Transfer Protocol",
                    "B) HyperText Transmission Protocol",
                    "C) HighText Transfer Protocol",
                    "D) HighText Transmission Protocol"],
        "answer": "A"
    },
    {
        "question": "4) What is the primary function of a modem in networking?",
        "options": ["A) To store data",
                    "B) To process data",
                    "C) To transmit data",
                    "D) To modulate and demodulate signals"],
        "answer": "D"
    },
    {
        "question": "5) In which year was the iPhone first released?",
        "options": ["A) 2005",
                    "B) 2007",
                    "C) 2009",
                    "D) 2011"],
        "answer": "B"
    },
    {
        "question": "6) What does 'AI' stand for?",
        "options": ["A) Automated Intelligence",
                    "B) Artificial Intelligence",
                    "C) Advanced Integration",
                    "D) Algorithmic Interpretation"],
        "answer": "B"
    },
    {
        "question": "7) Which company developed the video game 'Fortnite'?",
        "options": ["A) Activision",
                    "B) Electronic Arts",
                    "C) Epic Games",
                    "D) Ubisoft"],
        "answer": "C"
    },
    {
        "question": "8) What technology is used to record cryptocurrency transactions?",
        "options": ["A) Digital Ledger",
                    "B) Blockchain",
                    "C) SQL Database",
                    "D) Cloud Storage"],
        "answer": "B"
    },
    {
        "question": "9) Which programming language is widely used for AI and machine learning?",
        "options": ["A) Java",
                    "B) C++",
                    "C) Python",
                    "D) JavaScript"],
        "answer": "C"
    },
    {
        "question": "10) What does 'OLED' stand for?",
        "options": ["A) Organic Light-Emitting Diode",
                    "B) Original Light-Emitting Display",
                    "C) Organized Light-Emitting Diode",
                    "D) Optical Light-Emitting Device"],
        "answer": "A"
    }
]

# ============================
#          QUIZ START
# ============================

score = 0
total_questions = len(quiz)

print("=======================================")
print("           Welcome to the Quiz")
print("=======================================")
print(f"There are {total_questions} questions.\n")


for index, q in enumerate(quiz, start=1):

    print("---------------------------------------")
    print(f"Question {index} of {total_questions}")
    print("---------------------------------------\n")

    print(q["question"])
    print()
    for option in q["options"]:
        print(option)
    print()

    # Input validation
    while True:
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input! Please enter A, B, C, or D.\n")

    # Check answer
    if answer == q["answer"]:
        print("✔ Correct!\n")
        score += 1
    else:
        print(f"✘ Wrong! The correct answer is: {q['answer']}\n")