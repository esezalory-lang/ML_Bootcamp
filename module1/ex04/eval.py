
class Evaluator:
    def __init__(self: "Evaluator"):
        pass

    @staticmethod
    def zip_evaluate(coefs: list, words: list) -> int | float:
        if len(words) != len(coefs):
            return -1
        if not (isinstance(i, (int, float)) for i in words):
            raise TypeError("ERROR: wrong type in word list")
        if not (isinstance(i, (int, float)) for i in coefs):
            raise TypeError("ERROR: wrong type in word list")
        combined_list = list(zip(words, coefs))
        eval = sum(len(i[0]) * i[1] for i in combined_list)
        return eval

    @staticmethod
    def enumerate_evaluate(coefs: list, words: list) -> int | float:
        eval = 0
        if len(words) != len(coefs):
            return -1
        if not (isinstance(i, (int, float)) for i in words):
            raise TypeError("ERROR: wrong type in word list")
        if not (isinstance(i, (int, float)) for i in coefs):
            raise TypeError("ERROR: wrong type in word list")
        for i, ele in enumerate(coefs):
            eval += ele * len(words[i])
        return eval
