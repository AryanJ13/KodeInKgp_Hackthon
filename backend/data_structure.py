class Order:
    def __init__(self) -> None:
        self.id: int
        self.buyOrSell: bool
        self.limit: int
        self.entryTime: int
        self.eventTime: int
        self.nextOrder: Order
        self.prevOrder: Order
        self.parentLimit: Limit


class Limit:
    def __init__(self) -> None:
        self.limitPrice: int
        self.size: int
        self.totalVolume: int
        self.parent: Limit
        self.leftChild: Limit
        self.rightChild: Limit
        self.headOrder: Order
        self.tailOrder: Order


class Book:
    def __init__(self) -> None:
        self.buyTree: Limit
        self.sellTree: Limit
        self.lowestSell: Limit
        self.highestBuy: Limit
