import sys


def exec(args: list[str]) -> None:
    args.reverse()
    for sentence in args[:-1:]:
        new_word = ""
        for i in sentence[::-1]:
            swap = i.swapcase()
            new_word += swap
        print(new_word, end=" ")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print()
    else:
        try:
            exec(sys.argv)
        except Exception as e:
            print(f"{e}")
