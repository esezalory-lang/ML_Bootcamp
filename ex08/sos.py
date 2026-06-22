import sys


def convert_char(norm: str) -> str:
    morse_dict = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----'}

    for key, value in morse_dict.items():
        if key == norm:
            return value


def morse(arguments: list[str]) -> None:
    word = " ".join(arguments[1:])
    morse = ""
    uppercase = ""
    for char in word:
        if not (char.isalnum() or char.isspace()):
            print("ERROR")
            return
        if char == " ":
            uppercase += "/ "
        else:
            uppercase += convert_char(char.upper())
            uppercase += " "
    morse += uppercase
    print(morse)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("ERROR")
    else:
        morse(sys.argv)
