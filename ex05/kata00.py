# Put this at the top of your kata00.py file
kata = (19, 42, 21)

if __name__ == "__main__":
    length = len(kata)
    print(f"The {length} numbers are :", end=" ")
    print(*kata, sep=", ")
