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
        "text": "1) In CPython, which operations reliably release the GIL so other threads can run? (Choose 2 answers)",
        "options": [
            "A) A blocking socket.recv() call",
            "B) A tight CPU-bound loop in pure Python",
            "C) time.sleep() for any duration",
            "D) A list comprehension that fits in L3 cache",
        ],
        "answers": ["A", "C"],
    },
    {
        "text": "2) In asyncio, which options offload CPU-heavy work without freezing the event loop? (Choose 2 answers)",
        "options": [
            "A) await loop.run_in_executor(None, cpu_heavy_fn)",
            "B) await asyncio.to_thread(cpu_heavy_fn)",
            "C) await cpu_heavy_fn() inside the coroutine",
            "D) await asyncio.sleep(0) before calling cpu_heavy_fn()",
        ],
        "answers": ["A", "B"],
    },
    {
        "text": "3) Which dataclass configurations produce hashable instances by default? (Choose 2 answers)",
        "options": [
            "A) @dataclass(frozen=True)",
            "B) @dataclass(eq=True, frozen=False)",
            "C) @dataclass(unsafe_hash=True)",
            "D) @dataclass(order=True, frozen=False)",
        ],
        "answers": ["A", "C"],
    },
    {
        "text": "4) Which statement about __getattribute__ and __getattr__ is correct?",
        "options": [
            "A) __getattribute__ runs for every attribute access before __getattr__ is considered.",
            "B) __getattr__ is invoked for all lookups before __getattribute__.",
            "C) __getattr__ is skipped if the class defines __slots__.",
            "D) Defining __getattribute__ disables the descriptor protocol for properties.",
        ],
        "answers": ["A"],
    },
    {
        "text": "5) How do context variables behave with asyncio tasks? (Choose 2 answers)",
        "options": [
            "A) A new asyncio.Task copies the current context at creation time.",
            "B) Context variables are shared globally per thread, ignoring tasks.",
            "C) asyncio.create_task always starts with an empty default context.",
            "D) contextvars.copy_context().run(fn) executes with the captured context even across thread switches.",
        ],
        "answers": ["A", "D"],
    },
    {
        "text": "6) With the multiprocessing 'spawn' start method on Windows, which statement is accurate?",
        "options": [
            "A) Guarding code with if __name__ == '__main__' is required to avoid recursive child creation.",
            "B) Child processes share memory pages with the parent via copy-on-write.",
            "C) Open file descriptors are inherited automatically without pickling.",
            "D) Module-level globals are preserved without re-importing the module.",
        ],
        "answers": ["A"],
    },
    {
        "text": "7) Which statements about typing.Protocol are true? (Choose 2 answers)",
        "options": [
            "A) Applying @runtime_checkable enables isinstance checks for structural conformance.",
            "B) Classes must explicitly inherit from a Protocol to satisfy it.",
            "C) An empty Protocol is satisfied by every object.",
            "D) Protocols cannot define @final methods.",
        ],
        "answers": ["A", "C"],
    },
    {
        "text": "8) How can you ensure generators release resources promptly? (Choose 2 answers)",
        "options": [
            "A) Wrap them with contextlib.closing(...) inside a with block.",
            "B) Send None once to the generator to force closure.",
            "C) Rely on immediate garbage collection after function return.",
            "D) Call generator.close() so GeneratorExit triggers finally blocks.",
        ],
        "answers": ["A", "D"],
    },
    {
        "text": "9) Which statements about functools.lru_cache are correct? (Choose 2 answers)",
        "options": [
            "A) Setting maxsize=None makes the cache unbounded.",
            "B) Decorating a coroutine automatically caches awaited results instead of coroutine objects.",
            "C) cache_info().hits counts calls even when the wrapped function raised an exception.",
            "D) typed=True distinguishes between 1 and True as separate keys.",
        ],
        "answers": ["A", "D"],
    },
    {
        "text": "10) Which approaches keep a CLI tool's dependencies isolated from the system interpreter? (Choose 2 answers)",
        "options": [
            "A) python -m venv .venv followed by pip install inside that environment",
            "B) pip install --user inside the base interpreter",
            "C) Installing the CLI with pipx to give it its own virtual environment",
            "D) Installing directly into the system site-packages with pip",
        ],
        "answers": ["A", "C"],
    },
    {
        "text": "11) Which pathlib.Path operation is atomic when source and target are on the same filesystem?",
        "options": [
            "A) Path('old').replace('new')",
            "B) Path('file').write_text('data')",
            "C) Path('file').unlink(missing_ok=True)",
            "D) Path('dir').mkdir(parents=True, exist_ok=True)",
        ],
        "answers": ["A"],
    },
    {
        "text": "12) How does itertools.tee manage duplicated iterators? (Choose 2 answers)",
        "options": [
            "A) It buffers values so slower iterators can still consume earlier items.",
            "B) It duplicates the source iterator without any additional memory cost.",
            "C) Exhausting one tee iterator advances the shared source; others read from buffered items.",
            "D) tee iterators are thread-safe for concurrent use without locks.",
        ],
        "answers": ["A", "C"],
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
