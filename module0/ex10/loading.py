from tqdm import tqdm
from time import sleep


def ft_progress(lst: range) -> None:
    return tqdm(lst, colour="blue", ascii=" ||")


if __name__ == "__main__":
    listy = range(1000)
    print(listy)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.005)
    print()
    print(ret)
