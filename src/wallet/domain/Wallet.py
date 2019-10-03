from dataclasses import dataclass


@dataclass
class Wallet:
    currency: str
    value: float

    def __init__(self, currency: str, value):
        self.currency = currency
        self.value = float(value)

    def __add__(self, value):
        self.value = float(self.value) + value

        return self

    def __sub__(self, value):
        self.value = float(self.value) - value

        return self

    def __lt__(self, value):
        return self.value < value

    def __le__(self, value):
        return self.value <= value

    def __gt__(self, value):
        return self.value > value

    def __ge__(self, value):
        return self.value > value
