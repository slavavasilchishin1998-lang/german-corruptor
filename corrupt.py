
import random
import re
import argparse

ARTICLES = [
    "der", "die", "das", "den", "dem", "des",
    "ein", "eine", "einen", "einem", "einer"
]

def corrupt_word(word):
    if len(word) < 3:
        return word

    chars = list(word)

    action = random.choice([
        "shuffle", "replace", "duplicate", "reverse"
    ])

    if action == "shuffle":
        middle = chars[1:-1]
        random.shuffle(middle)
        chars = [chars[0]] + middle + [chars[-1]]

    elif action == "replace":
        chars[random.randrange(len(chars))] = random.choice(
            "abcdefghijklmnopqrstuvwxyzäöüß"
        )

    elif action == "duplicate":
        i = random.randrange(len(chars))
        chars.insert(i, chars[i])

    elif action == "reverse":
        chars.reverse()

    return "".join(chars)


def corrupt_text(text, chaos=100):
    words = re.findall(r'\w+|[^\w\s]+|\s+', text)

    result = []

    for word in words:
        if word.lower() in ARTICLES and random.randint(1, 100) <= chaos:
            word = random.choice(ARTICLES)

        elif word.isalpha() and random.randint(1, 100) <= chaos:
            word = corrupt_word(word)

        result.append(word)

    output = "".join(result)

    if chaos >= 75:
        parts = output.split()
        random.shuffle(parts)
        output = " ".join(parts)

    return output


def main():
    parser = argparse.ArgumentParser(
        description="GERMAN TEXT CORRUPTOR"
    )

    parser.add_argument("text", help="German text to corrupt")
    parser.add_argument(
        "--chaos", type=int, default=100,
        help="Chaos level from 0 to 100"
    )

    args = parser.parse_args()

    chaos = max(0, min(100, args.chaos))

    print("\n💥 ORIGINAL:")
    print(args.text)

    print("\n☠️ CORRUPTED:")
    print(corrupt_text(args.text, chaos))


if __name__ == "__main__":
    main()
