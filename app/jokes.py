import random

CATEGORIES = ("classic", "programming", "school")

JOKES = {
    "classic": (
        "I only know 25 letters of the alphabet. I don't know y.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "I used to hate facial hair, but then it grew on me.",
        "What do you call fake spaghetti? An impasta.",
        "I am reading a book about anti-gravity. It is impossible to put down.",
        "What do you call a bear with no teeth? A gummy bear.",
        "Why did the tomato blush? Because it saw the salad dressing.",
        "What did one wall say to the other? I'll meet you at the corner.",
        "Why don't eggs tell jokes? They might crack each other up.",
        "What do you call cheese that is not yours? Nacho cheese.",
    ),
    "programming": (
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "There are 10 kinds of people: those who understand binary and those who don't.",
        "Why was the JavaScript developer sad? Because they didn't know how to Node.",
        "A SQL query walks into a bar and asks: Can I join you?",
        "Why did the developer go broke? Because they used up all their cache.",
        "I would tell you a UDP joke, but you might not get it.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "A programmer's spouse says: Get milk. If they have eggs, get six. They return with  six milks.",
        "Why did the function return early? It had a pressing deadline.",
        "The developer quit their job because they didn't get arrays.",
    ),
    "school": (
        "Why did the student eat their homework? The teacher said it was a piece of cake.",
        "Why was the math book sad? It had too many problems.",
        "Why did the teacher wear sunglasses? Her students were so bright.",
        "What is a snake's favorite subject? Hiss-tory.",
        "Why did the student bring a ladder to school? They wanted to go to high school.",
        "What did the pencil say to the paper? I dot my i's on you.",
        "Why did the clock get sent to the principal? It was tocking too much.",
        "What is a teacher's favorite nation? Explanation.",
        "Why did the notebook go to the doctor? It had a bad case of writer's block.",
        "Why was the school cafeteria so noisy? Because the students were lunching their opinions.",
    ),
}

ALL_JOKES = tuple(joke for category in CATEGORIES for joke in JOKES[category])


def select_joke(category: str | None = None) -> tuple[str, str]:
    if category is not None and category not in JOKES:
        raise KeyError(category)

    selected_category = category or random.choice(CATEGORIES)
    return selected_category, random.choice(JOKES[selected_category])