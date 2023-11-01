#
#  Зробив
#  Севастьянов Данило Сергійович
#  кн-20-2 ДУАН
#
from random import randbytes
from BitSequence import BitSequence
from SeriesLengthTest.SeriesLength import runs_test


def main():
    sequence = BitSequence(randbytes(20000))

    if runs_test(sequence):
        print("Послідовність випадкова")
    else:
        print("Послідовність не випадкова")


if __name__ == "__main__":
    main()
