import random

JOKES = (
    "I only know 25 letters of the alphabet. I don't know y.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "I used to hate facial hair, but then it grew on me.",
    "What do you call fake spaghetti? An impasta.",
    "I am reading a book about anti-gravity. It is impossible to put down.",
)


def select_joke() -> str:
    return random.choice(JOKES)