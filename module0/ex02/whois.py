import sys


def whois(args: list[str]) -> None:
    if len(args) != 2:
        raise Exception("AssertionError: more than one argument is provided")
    else:
        try:
            number = int(args[1])
        except Exception:
            print("AssertionError: argument is not an integer")
            return
        if number == 0:
            print("I'm Zero.")
        else:
            if number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")


if __name__ == "__main__":
    try:
        whois(sys.argv)
    except Exception as e:
        print(f"{e}")
