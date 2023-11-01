#
#  Зробив
#  Севастьянов Данило Сергійович
#  кн-20-2 ДУАН
#
from random import randbytes
from BitSequence import BitSequence


def monobit_test(sequence: BitSequence):
    return sequence.is_random()


def main():
    sequence = BitSequence(randbytes(20000))

    if monobit_test(sequence):
        print("Послідовність випадкова")
    else:
        print("Послідовність не випадкова")


if __name__ == "__main__":
    main()
