class BitSequence:
    """
    Клас для зберігання та обробки бітових послідовностей

    :param data: Бітова послідовність
    """

    def __init__(self, data: bytes):
        self.data = data
        self.num_zeros = 0
        self.num_ones = 0

    """
    Підраховує кількість одиниць у бітовій послідовності
    """

    def count_ones(self):
        for byte in self.data:
            self.num_ones += byte.count(1)

    """
    Підраховує кількість нулів у бітовій послідовності
    """

    def count_zeros(self):
        self.num_zeros = len(self.data) - self.num_ones

    """
    Перевіряє, чи є бітову послідовність випадковою

    :return: True, якщо послідовність випадкова, False в іншому випадку
    """

    def is_random(self):
        """
        Перевіряє, чи знаходиться кількість одиниць у діапазоні (9654, 10346)
        """
        return 9654 <= self.num_ones <= 10346

    def __len__(self):
        """
        Повертае довжину бітової послідовністі
        """
        return len(self.data)

    def __getitem__(self, index: int) -> int:
        """
        poker test work pls
        thx
        """
        return self.data[index]
