import random


def generator(text: str, sep: str = "", option: str = None):
    options = ["shuffle", "unique", "ordered"]
    if not isinstance(text, str) and option not in options:
        return print("ERROR")
    substrings = text.split(sep)
    if option is None:
        for i in substrings:
            yield i
    elif option == options[0]:
        random.shuffle(substrings)
        for i in substrings:
            yield i
    elif option == options[1]:
        unique = list(dict.fromkeys(substrings))
        for i in unique:
            yield i
    elif option == options[2]:
        alphabetical = sorted(substrings)
        for i in alphabetical:
            yield i


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)

    print("\nShuffled:")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)

    print("\nAlphabetical:")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)

    print("\nUnique:")
    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)

    print()
    text = 1.0
    for word in generator(text, sep="."):
        print(word)
