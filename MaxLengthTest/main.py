#
#  Зробив
#  Севастьянов Данило Сергійович
#  кн-20-2 ДУАН
#
from random import randbytes
from MaxLengthTest.MaxLength import max_run_length_test
from BitSequence import BitSequence


def main():
    sequence = BitSequence(randbytes(20000))
    if max_run_length_test(sequence):
        print("Послідовність випадкова")
    else:
        print("Послідовність не випадкова")


if __name__ == "__main__":
    main()
