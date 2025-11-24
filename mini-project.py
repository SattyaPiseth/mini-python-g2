"""Simple terminal quiz using lists, dictionaries, for-loops, and if-else."""

# Simple emoji mapping for feedback.
EMOJIS = {
    "correct": "✅",
    "wrong": "❌",
    "note": "📝",
    "trophy": "🏆",
    "thumbs": "👍",
    "seed": "🌱",
    "bulb": "💡",
}


def emojize(name):
    """Return an emoji symbol for a given name."""
    return EMOJIS.get(name, "")


# Quiz data: each question is a dictionary with text, options, and the correct answers.
QUESTIONS = [
    {
        "text": "1) In modern CPU pipelines, which unit translates complex instructions into micro-ops before dispatch?",
        "options": [
            "A) Decoder",
            "B) Reorder buffer",
            "C) Branch predictor",
            "D) Execution unit",
        ],
        "answers": ["A"],
    },
    {
        "text": "2) Which protocol negotiates cryptographic parameters for secure HTTP traffic over TLS 1.3?",
        "options": [
            "A) ALPN",
            "B) OCSP",
            "C) HSTS",
            "D) HPKP",
        ],
        "answers": ["A"],
    },
    {
        "text": "3) In distributed systems, which algorithm is designed for leader election and log replication with log compaction support?",
        "options": [
            "A) Paxos",
            "B) Raft",
            "C) Two-Phase Commit",
            "D) Gossip",
        ],
        "answers": ["B"],
    },
    {
        "text": "4) Which storage technology pairs NAND flash with a PCIe interface and an optimized command set for parallel I/O?",
        "options": [
            "A) SATA SSD",
            "B) NVMe SSD",
            "C) SAS HDD",
            "D) UFS card",
        ],
        "answers": ["B"],
    },
    {
        "text": "5) Which networking device uses TCAM to apply ACLs at wire speed while operating at Layer 3?",
        "options": [
            "A) Access point",
            "B) Core router",
            "C) Hub",
            "D) Media converter",
        ],
        "answers": ["B"],
    },
    {
        "text": "6) In relational databases, which isolation level prevents dirty reads and non-repeatable reads but may allow phantom reads?",
        "options": [
            "A) Read Uncommitted",
            "B) Read Committed",
            "C) Repeatable Read",
            "D) Serializable",
        ],
        "answers": ["C"],
    },
    {
        "text": "7) Which public-key scheme relies on the hardness of discrete logarithms over elliptic curves?",
        "options": [
            "A) RSA",
            "B) ECDSA",
            "C) AES-GCM",
            "D) ChaCha20",
        ],
        "answers": ["B"],
    },
    {
        "text": "8) In machine learning, which dimensionality reduction technique preserves global variance but may lose neighborhood structure?",
        "options": [
            "A) t-SNE",
            "B) PCA",
            "C) UMAP",
            "D) DBSCAN",
        ],
        "answers": ["B"],
    },
    {
        "text": "9) Which consistency model guarantees monotonic reads and writes but not strict linearizability?",
        "options": [
            "A) Eventual consistency",
            "B) Strong consistency",
            "C) Causal consistency",
            "D) Read-your-writes only",
        ],
        "answers": ["C"],
    },
    {
        "text": "10) For high-refresh gaming displays, which feature reduces perceived motion blur by briefly turning off the backlight each frame?",
        "options": [
            "A) Black frame insertion",
            "B) Local dimming",
            "C) Variable refresh rate",
            "D) Quantum dots",
        ],
        "answers": ["A"],
    },
    {
        "text": "11) Which techniques collectively harden TLS sessions against key compromise? (Choose 2 answers)",
        "options": [
            "A) Perfect forward secrecy",
            "B) Allowing export-grade ciphers",
            "C) OCSP stapling with short-lived certs",
            "D) Disabling certificate validation",
        ],
        "answers": ["A", "C"],
    },
    {
        "text": "12) Which storage strategies balance performance and redundancy for production databases? (Choose 2 answers)",
        "options": [
            "A) RAID 0 striping only",
            "B) RAID 10 (striped mirrors)",
            "C) Single large consumer SSD",
            "D) RAID 1 mirroring",
        ],
        "answers": ["B", "D"],
    },
]


def normalize_answers(raw):
    """Turn comma/space separated user input into a list of uppercase options."""
    cleaned = raw.replace(",", " ")
    parts = cleaned.upper().split()
    unique = []
    for part in parts:
        if part and part not in unique:
            unique.append(part)
    return unique


def answers_match(user_answers, correct_answers):
    """Return True when the same options are chosen, regardless of order."""
    if len(user_answers) != len(correct_answers):
        return False
    for answer in correct_answers:
        if answer not in user_answers:
            return False
    for answer in user_answers:
        if answer not in correct_answers:
            return False
    return True


def ask_question(question, number, total):
    """Show one question, get input, and return True if the answer is correct."""
    print("\n------------------------------")
    print(f"Question {number} of {total}")
    print("------------------------------")
    print(question["text"])
    print()

    for option in question["options"]:
        print(option)

    correct_answers = [option.upper() for option in question["answers"]]
    is_multi = len(correct_answers) > 1

    if is_multi:
        prompt = (
            f"\nEnter {len(correct_answers)} answers separated by commas or spaces "
            "(e.g., A,C): "
        )
    else:
        prompt = "\nYour answer (A/B/C/D): "

    valid_choices = ["A", "B", "C", "D"]
    while True:
        user_answers = normalize_answers(input(prompt))

        if not user_answers:
            print("Please enter at least one option.")
            continue

        has_invalid = False
        for choice in user_answers:
            if choice not in valid_choices:
                has_invalid = True
        if has_invalid:
            print("Please choose only A, B, C, or D.")
            continue

        if not is_multi and len(user_answers) != 1:
            print("Please enter exactly one option for this question.")
            continue

        if is_multi and len(user_answers) != len(correct_answers):
            print(f"Please select exactly {len(correct_answers)} options.")
            continue

        break

    if answers_match(user_answers, correct_answers):
        print(f"{emojize('correct')} Correct!")
        return True
    else:
        formatted = ", ".join(correct_answers)
        print(f"{emojize('wrong')} Wrong! The correct answer(s): {formatted}.")
        return False


def show_results(score, total):
    """Display final score and simple feedback."""
    percent = (score / total) * 100
    print("\n===================================")
    print("            Quiz Finished          ")
    print("===================================")
    print(f"You got {score} out of {total} correct.")
    print(f"Your score: {percent:.1f}%")

    if percent == 100:
        print(f"{emojize('trophy')} Perfect score! Amazing!")
    elif percent >= 70:
        print(f"{emojize('thumbs')} Great work, keep it up!")
    elif percent >= 40:
        print(f"{emojize('seed')} Not bad - practice a bit more and try again.")
    else:
        print(f"{emojize('bulb')} Keep studying and give it another go!")


def run_quiz():
    """Run the quiz loop and handle scoring."""
    print("===================================")
    print("        Welcome to the Quiz        ")
    print("===================================")
    print(f"There are {len(QUESTIONS)} questions.\n")

    score = 0
    for index, question in enumerate(QUESTIONS, start=1):
        if ask_question(question, index, len(QUESTIONS)):
            score += 1

    show_results(score, len(QUESTIONS))


if __name__ == "__main__":
    run_quiz()
