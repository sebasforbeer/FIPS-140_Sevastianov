from BitSequence import BitSequence
from collections import defaultdict


def runs_test(sequence: BitSequence):
    """
    Тест довжин серій

    :param sequence: Бітова послідовність
    :return: True, якщо послідовність випадкова, False в іншому випадку
    """

    lengths = defaultdict(int)

    for i in range(len(sequence)):
        current_length = 1
        while i + current_length < len(sequence) and sequence[i] == sequence[i + current_length]:
            current_length += 1
        lengths[current_length] += 1

    for length in range(1, 7):
        if not 0.001 <= lengths[length] / len(sequence) <= 0.099:
            return False

    for length in range(1, 7):
        if not 0.001 <= lengths[-length] / len(sequence) <= 0.099:
            return False

    return True
