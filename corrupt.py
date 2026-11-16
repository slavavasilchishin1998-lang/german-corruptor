import random
import re
import argparse
import time

# =====================================
# GERMAN CORRUPTOR V2
# =====================================

ARTICLES = [
    "der", "die", "das", "den", "dem", "des",
    "ein", "eine", "einen", "einem", "einer",
    "eines", "einer"
]

GERMAN_WORDS = [
    "Haus", "Hund", "Katze", "Mensch", "Schule",
    "Auto", "Wasser", "Brot", "Freund", "Sprache",
    "Deutschland", "Computer", "Buch", "Baum"
]

VOWELS = "aeiouäöü"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def random_letter():
    return random.choice("abcdefghijklmnopqrstuvwxyzäöüß")


def destroy_umlauts(word):
    replacements = {
        "ä": random.choice(["ae", "a", "e"]),
        "ö": random.choice(["oe", "o", "e"]),
        "ü": random.choice(["ue", "u", "i"]),
        "ß": random.choice(["ss", "s", "z"])
    }

    for old, new in replacements.items():
        if old in word.lower():
            word = re.sub(
                old,
                new,
                word,
                flags=re.IGNORECASE
            )

    return word


def destroy_word(word, chaos):
    if len(word) < 2:
        return word

    if random.randint(1, 100) > chaos:
        return word

    operation = random.choice([
        "shuffle",
        "replace",
        "duplicate",
        "reverse",
        "remove",
        "umlaut"
    ])

    chars = list(word)

    if operation == "shuffle" and len(chars) > 3:
        middle = chars[1:-1]
        random.shuffle(middle)
        chars = [chars[0]] + middle + [chars[-1]]

    elif operation == "replace":
        i = random.randrange(len(chars))
        chars[i] = random_letter()

    elif operation == "duplicate":
        i = random.randrange(len(chars))
        chars.insert(i, chars[i])

    elif operation == "reverse":
        chars.reverse()

    elif operation == "remove" and len(chars) > 2:
        del chars[random.randrange(len(chars))]

    elif operation == "umlaut":
        return destroy_umlauts(word)

    return "".join(chars)


def destroy_article(word, chaos):
    if word.lower() not in ARTICLES:
        return word

    if random.randint(1, 100) <= chaos:
        replacement = random.choice(ARTICLES)

        if word[0].isupper():
            replacement = replacement.capitalize()

        return replacement

    return word


def destroy_sentence(text):
    words = text.split()

    if len(words) > 2:
        random.shuffle(words)

    return " ".join(words)


def corrupt(text, chaos):
    # Protect punctuation and whitespace
    tokens = re.findall(r'\w+|[^\w\s]+|\s+', text)

    result = []

    for token in tokens:
        if token.isalpha():
            token = destroy_article(token, chaos)
            token = destroy_word(token, chaos)

        result.append(token)

    output = "".join(result)

    if chaos >= 75:
        sentences = re.split(r'(?<=[.!?])\s+', output)
        random.shuffle(sentences)
        output = " ".join(sentences)

    return output


def nuclear_mode(text):
    result = text

    for _ in range(3):
        result = corrupt(result, 100)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="GERMAN CORRUPTOR - ALEMAN DESTROYER"
    )

    parser.add_argument(
        "text",
        nargs="?",
        help="German text to corrupt"
    )

    parser.add_argument(
        "--chaos",
        type=int,
        default=100,
        help="Corruption level (0-100)"
    )

    parser.add_argument(
        "--nuclear",
        action="store_true",
        help="Maximum corruption"
    )

    parser.add_argument(
        "--infinite",
        action="store_true",
        help="Generate corruption repeatedly"
    )

    args = parser.parse_args()

    print("=" * 45)
    print("       GERMAN CORRUPTOR V2")
    print("          ALEMAN DESTROYER")
    print("=" * 45)

    if not args.text:
        args.text = input("\nEnter German text: ")

    chaos = max(0, min(100, args.chaos))

    print("\nORIGINAL:")
    print(args.text)

    if args.infinite:
        print("\nINFINITE CHAOS - Press CTRL+C to stop")

        try:
            while True:
                print("\n" + corrupt(args.text, chaos))
                time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n\nChaos stopped!")

    elif args.nuclear:
        print("\nNUCLEAR RESULT:")
        print(nuclear_mode(args.text))

    else:
        print("\nCORRUPTED RESULT:")
        print(corrupt(args.text, chaos))

    print("\nGERMAN CORRUPTOR FINISHED.")


if __name__ == "__main__":
    main()
