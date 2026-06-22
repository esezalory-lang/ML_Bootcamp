import string
import sys


def text_analyzer(argument: str = "") -> None:
    """\n\tThis function counts the number of upper characters,
    \tlower characters,punctuation and spaces in a given text."""

    text = ""
    printable = 0
    upper = 0
    lower = 0
    punctuation = 0
    space = 0

    if argument.isdigit():
        print("AssertionError: argument is an integer")
        return
    if argument == "":
        print("What is the text to analyze?")
        text = input()
    else:
        text = argument
    for i in text:
        if i in string.punctuation:
            punctuation += 1
        if i.isprintable():
            printable += 1
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i.isspace():
            space += 1

    print(f"The text contains {printable} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {space} spaces(s)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
    else:
        text_analyzer(sys.argv[1])
