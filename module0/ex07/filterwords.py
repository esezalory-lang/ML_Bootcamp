import sys
import string


def filterwords(sentence: str, length: int) -> None:
    word_list = []
    filtered = []
    clean = ''.join([char for char in sentence
                     if char not in string.punctuation])
    word_list = clean.split()
    filtered = [i for i in word_list if len(i) > length]
    print(filtered)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        if sys.argv[1].isdigit():
            print("ERROR")
        else:
            filterwords(sys.argv[1], int(sys.argv[2]))
