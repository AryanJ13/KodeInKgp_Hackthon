
class User:
    def __init__(self, id) -> None:
        self.balance = 0
        self.qty = 0
        self.id = id

    def change_balance(self, x: int):
        self.balance += x

    def change_qty(self, x: int):
        self.qty += x
