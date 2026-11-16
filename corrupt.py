
import random
import re
import sys
import time

# ==========================================
#       GERMAN DESTROYER V3
#          TOTAL ALEMAN CHAOS
# ==========================================

VERSION = "3.0"

ARTICLES = [
    "der", "die", "das", "den", "dem", "des",
    "ein", "eine", "einen", "einem", "einer",
    "eines"
]

UMLAUTS = {
    "ä": ["ae", "a", "e"],
    "ö": ["oe", "o", "e"],
    "ü": ["ue", "u", "i"],
    "ß": ["ss", "s", "z"]
}

LETTERS = "abcdefghijklmnopqrstuvwxyzäöüß"
VOWELS = "aeiouäöü"


def banner():
    print("\033[96m")
    print("=" * 48)
    print("          GERMAN DESTROYER V3")
    print("            ALEMAN CHAOS")
    print("=" * 48)
    print("\033[0m")


def destroy_umlauts(word):
    result = ""

    for char in word:
        lower = char.lower()

        if lower in UMLAUTS and random.random() < 0.8:
            replacement = random.choice(UMLAUTS[lower])

            if char.isupper():
                replacement = replacement.upper()

            result += replacement
        else:
            result += char

    return result


def mutate_word(word, chaos):
    if len(word) < 2:
        return word

    if random.randint(1, 100) > chaos:
        return word

    operations = [
        "replace",
        "duplicate",
        "shuffle",
        "reverse",
        "delete",
        "umlaut",
        "extra"
    ]

    operation = random.choice(operations)
    chars = list(word)

    if operation == "replace":
        i = random.randrange(len(chars))
        chars[i] = random.choice(LETTERS)

    elif operation == "duplicate":
        i = random.randrange(len(chars))
        chars.insert(i, chars[i])

    elif operation == "shuffle":
        random.shuffle(chars)

    elif operation == "reverse":
        chars.reverse()

    elif operation == "delete" and len(chars) > 2:
        del chars[random.randrange(len(chars))]

    elif operation == "umlaut":
        return destroy_umlauts(word)

    elif operation == "extra":
        chars.insert(
            random.randrange(len(chars) + 1),
            random.choice(LETTERS)
        )

    result = "".join(chars)

    return result


def destroy_article(word, chaos):
    if word.lower() not in ARTICLES:
        return word

    if random.randint(1, 100) <= chaos:
        replacement = random.choice(ARTICLES)

        if word[0].isupper():
            replacement = replacement.capitalize()

        return replacement

    return word


def corrupt_words(text, chaos):
    tokens = re.findall(r'\w+|[^\w\s]+|\s+', text)

    result = []

    for token in tokens:
        if token.isalpha():
            token = destroy_article(token, chaos)
            token = mutate_word(token, chaos)

        result.append(token)

    return "".join(result)


def scramble_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)

    result = []

    for sentence in sentences:
        words = sentence.split()

        if len(words) > 2:
            random.shuffle(words)

        result.append(" ".join(words))

    return " ".join(result)


def nuclear_destroy(text):
    result = text

    for _ in range(5):
        result = corrupt_words(result, 100)

    result = scramble_sentence(result)

    return result


def destroy(text, chaos):
    result = corrupt_words(text, chaos)

    if chaos >= 40:
        result = scramble_sentence(result)

    return result


def print_result(original, corrupted):
    print("\n" + "=" * 48)
    print("ORIGINAL:")
    print(original)

    print("\nDESTROYED:")
    print("\033[91m" + corrupted + "\033[0m")
    print("=" * 48)


def get_chaos():
    while True:
        value = input("Chaos level (0-100): ").strip()

        try:
            number = int(value)

            if 0 <= number <= 100:
                return number

            print("Enter a number between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def interactive():
    while True:
        print("\n")
        print("========= MAIN MENU =========")
        print("1. Normal destruction")
        print("2. Article destroyer")
        print("3. Word destroyer")
        print("4. Umlaut destroyer")
        print("5. Grammar chaos")
        print("6. NUCLEAR MODE")
        print("7. INFINITE MODE")
        print("8. Change chaos level")
        print("9. Exit")
        print("=============================")

        choice = input("\nChoose mode: ").strip()

        if choice == "9":
            print("\nGERMAN DESTROYER shutting down.")
            break

        if choice == "8":
            chaos = get_chaos()
            print(f"Chaos level selected: {chaos}")
            continue

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Try again.")
            continue

        text = input("\nEnter German text: ")

        if not text.strip():
            print("Empty text! Try again.")
            continue

        try:
            if choice == "1":
                chaos = get_chaos()
                result = destroy(text, chaos)

            elif choice == "2":
                result = text
                tokens = re.findall(r'\w+|[^\w\s]+|\s+', text)
                result = "".join(
                    destroy_article(t, 100) if t.isalpha() else t
                    for t in tokens
                )

            elif choice == "3":
                result = corrupt_words(text, 100)

            elif choice == "4":
                result = destroy_umlauts(text)

            elif choice == "5":
                result = scramble_sentence(text)

            elif choice == "6":
                result = nuclear_destroy(text)

            elif choice == "7":
                print("\nINFINITE MODE")
                print("Press CTRL+C to stop.")

                while True:
                    print("\n" + nuclear_destroy(text))
                    time.sleep(0.7)

                continue

            print_result(text, result)

        except KeyboardInterrupt:
            print("\nOperation stopped.")
        except Exception as error:
            print(f"\nSomething went wrong: {error}")

        input("\nPress ENTER to return to menu...")


def main():
    try:
        banner()
        interactive()

    except KeyboardInterrupt:
        print("\n\nProgram stopped safely.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")

    finally:
        print("\nThanks for using GERMAN DESTROYER V3.")


if __name__ == "__main__":
    main()
