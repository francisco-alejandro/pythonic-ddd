from dataclasses import dataclass

from src.wallet import Wallet


@dataclass
class User:
    email: str
    money: Wallet

    def __init__(self, email, money):
        self.email = email
        self.money = money
