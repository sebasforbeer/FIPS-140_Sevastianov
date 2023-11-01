from collections import defaultdict
import BitSequence


def poker_test(sequence: BitSequence, m: int):
    """
    Тест Поккера

    :param sequence: Бітова послідовність
    :param m: Довжина блоку Поккера
    :return: True, якщо послідовність випадкова, False в іншому випадку
    """

    k = len(sequence) // m
    block_counts = defaultdict(int)

    for i in range(0, len(sequence), m):
        block = sequence[i: i + m]
        block_counts[block] += 1

    expected_count = k / 2 ** m
    x3 = 0
    for block, count in block_counts.items():
        x3 += (count - expected_count) ** 3

    return 1.03 <= x3 <= 57.4
