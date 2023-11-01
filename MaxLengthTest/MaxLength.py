import BitSequence


def max_run_length_test(sequence: BitSequence):
    """
    Тест на максимальну довжину серії

    :param sequence: Бітова послідовність
    :return: True, якщо послідовність випадкова, False в іншому випадку
    """

    max_run_length_zeros = 0
    max_run_length_ones = 0

    for i in range(len(sequence.data)):
        run_length_zeros = 1
        run_length_ones = 1
        while i + run_length_zeros < len(sequence.data) and sequence.data[i] == sequence.data[i + run_length_zeros]:
            run_length_zeros += 1
        while i + run_length_ones < len(sequence.data) and sequence.data[i] != sequence.data[i + run_length_ones]:
            run_length_ones += 1

        max_run_length_zeros = max(max_run_length_zeros, run_length_zeros)
        max_run_length_ones = max(max_run_length_ones, run_length_ones)

    return max_run_length_zeros <= 36 and max_run_length_ones <= 36