import random
import re

print("German Corruptor initialized.")
print("WARNING: German may become 400% more German.")

ARTICLES = [
    "der",
    "die",
    "das",
    "dem",
    "den"
]

LONG_SUFFIXES = [
    "verwaltung",
    "versicherung",
    "anleitung",
    "gesellschaft",
    "benutzung",
    "verordnung",
    "überwachung",
    "zuständigkeit",
    "bearbeitung"
]

def corrupt_word(word):
    # Skip punctuation and short words
    if len(word) < 4 or not word.isalpha():
        return word

    # Add random article
    if random.random() < 0.15:
        word = random.choice(ARTICLES) + " " + word

    # Add fake bureaucratic suffix
    if random.random() < 0.30:
        word += random.choice(LONG_SUFFIXES)

    # Rare mega-compound mode
    if random.random() < 0.10:
        word += random.choice(LONG_SUFFIXES)
        word += random.choice(LONG_SUFFIXES)

    return word

def german_corruptor(text):
    tokens = re.findall(r"\w+|[^\w\s]", text)

    corrupted = [corrupt_word(token) for token in tokens]

    # Randomly inject article
    if random.random() < 0.50:
        pos = random.randint(0, len(corrupted))
        corrupted.insert(pos, random.choice(ARTICLES))

    return " ".join(corrupted)

if __name__ == "__main__":
    while True:
        user_input = input("\nText> ")

        if user_input.lower() in ["quit", "exit"]:
            print("Corruptor shutting down.")
            break

        print("\nCorrupted:")
        print(german_corruptor(user_input))
