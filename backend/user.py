class User:
    def __init__(self, id) -> None:
        self.balance = 0
        self.qty = dict()
        self.id = id

    def change_balance(self, x: int):
        self.balance += x

    def change_qty(self, stock_name: str, x: int):
        self.qty[stock_name] += x
