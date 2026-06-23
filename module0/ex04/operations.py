import sys
import math


def operation(arg1: int, arg2: int) -> None:
    sum = 0
    diff = 0
    product = 0
    quotient = 0
    remainder = 0

    sum = arg1 + arg2
    print(f"Sum:\t\t{sum}")
    diff = arg1 - arg2
    print(f"Difference:\t{diff}")
    product = arg1 * arg2
    print(f"Product:\t{product}")
    try:
        quotient = arg1 / arg2
        if math.isinf(arg1 / arg2) is True:
            print(f"Quotient:\t{round(quotient, 4)}...")
        else:
            print(f"Quotient:\t{round(quotient, 4)}")
    except ZeroDivisionError:
        print("Quotient:\tERROR (division by zero)")
    try:
        remainder = arg1 % arg2
        print(f"Remainder:\t{remainder}")
    except ZeroDivisionError:
        print("Remainder:\tERROR (modulo by zero)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("AssertionError: too many arguments")
    else:
        try:
            arg1 = int(sys.argv[1])
            arg2 = int(sys.argv[2])
        except TypeError:
            print("AssertionError: only integers")
        operation(arg1, arg2)
