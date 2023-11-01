#
#  Зробив
#  Севастьянов Данило Сергійович
#  кн-20-2 ДУАН
#
from random import randbytes
from BitSequence import BitSequence
from PokerTest.poker_test import poker_test


def main():
    sequence = BitSequence(randbytes(20000))

    if poker_test(sequence, 4):
        print("Послідовність випадкова")
    else:
        print("Послідовність не випадкова")


if __name__ == "__main__":
    main()
