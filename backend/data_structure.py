from re import L
from typing_extensions import Self

from backend.user import User


# buyOrSell: True == Buy, False == Sell
class Order:
    def __init__(self, id, buyOrSell, price, size, placer: User) -> None:
        self.id: int = id
        self.buyOrSell: bool = buyOrSell
        self.price: int = price
        self.placer: User = placer
        self.quantity: int = size
        self.nextOrder: Order = None
        self.prevOrder: Order = None
        self.parentLimit: Limit = None

    def insert_order(self, next_order: Self):
        next_order.nextOrder = self.nextOrder
        self.nextOrder = next_order

    def remove_order(self):
        # self.nextOrder = None
        if self.nextOrder == None and self.prevOrder == None:
            self.parentLimit.remove_limit()
        elif self.prevOrder == None:
            self = self.nextOrder
        else:
            self.prevOrder.nextOrder = self.nextOrder


class Limit:
    def __init__(self, limitPrice, size, order) -> None:
        self.limitPrice: int = limitPrice
        self.size: int = size
        self.parent: Limit = None
        self.leftChild: Limit = None
        self.rightChild: Limit = None
        self.headOrder: Order = order
        self.headOrder.parentLimit = self

    def insert_limit(self, limit: Self):
        if self.limitPrice < limit.limitPrice:
            if self.rightChild != None:
                self.rightChild.insert_limit(limit)
            else:
                self.rightChild = limit
                limit.parent = self
        elif self.limitPrice > limit.limitPrice:
            if self.leftChild != None:
                self.leftChild.insert_limit(limit)
            else:
                self.rightChild = limit
                limit.parent = self
        else:
            limit.headOrder.parentLimit = self
            self.headOrder.insert_order(limit.headOrder)

    def remove_limit(self):
        parent = self.parent
        if self == parent.leftChild:
            parent.leftChild = None
        else:
            parent.rightChild = None
        self.parent = None


class Book:
    def __init__(self) -> None:
        self.buyTree: Limit = None
        self.sellTree: Limit = None
        self.lowestSell: Limit = None
        self.highestBuy: Limit = None
        self.ordersBuy: dict[int, Order] = dict()
        self.limitsBuy: dict[int, Limit] = dict()
        self.ordersSell: dict[int, Order] = dict()
        self.limitsSell: dict[int, Limit] = dict()

    def insert(self, order: Order):
        if order.buyOrSell:
            limit = self.limitsBuy[order.price]
            if limit != None:
                limit.headOrder.insert_order(order)
            else:
                limit = Limit(order.price, order.quantity, order)
                self.buyTree.insert_limit(limit)
                self.ordersBuy[order.id] = order
                self.limitsBuy[order.price] = limit
        else:
            limit = self.limitsSell[order.price]
            if limit != None:
                limit.headOrder.insert_order(order)
            else:
                limit = Limit(order.price, order.quantity, order)
                self.buyTree.insert_limit(limit)
                self.ordersSell[order.id] = order
                self.limitsSell[order.price] = limit

    def lowestSell(self, node: Limit):
        if node.leftChild == None:
            return node
        return self.lowestSell(node.leftChild)

    def largestBuy(self, node: Limit):
        if node.rightChild == None:
            return node
        return self.LargestBuy(node.rightChild)

    # Returns lowestSell
    def buy(self, quantity: int) -> list[Order]:
        head: Limit
        head = self.lowestSell(self, self.SellTree)
        # if quantity>= self.ordersBuy[head.headOrder.id]:
        orders = []
        orders = None
        node = head.headOrder
        while node != None:
            if quantity == 0:
                break
            elif quantity >= node.quantity:
                orders.append(node)
                quantity = quantity - node.quantity
                head.headOrder.remove_order(node)
            else:
                orders.append(node)
                quantity = 0
                node.quantity = node.quantity - quantity
            node = node.nextOrder
        return orders
        # pass

    # Return highestBuy
    def sell(self, quantity: int) -> list[Order]:
        head: Limit
        head = self.largestBuy(self, self.BuyTree)
        orders = []
        orders = None
        node = head.headOrder
        while node != None:
            if quantity == 0:
                break
            elif quantity >= node.quantity:
                orders.append(node)
                quantity = quantity - node.quantity
                head.headOrder.remove_order(node)
            else:
                orders.append(node)
                quantity = 0
                node.quantity = node.quantity - quantity
            node = node.next
        return orders
        # pass


import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_insert_cancel(self):
        o1, o2, o3 = [Order(1, True, 110), Order(2, True, 120), Order(3, True, 110)]
        l1, l2, l3 = [Limit(110, 10, o1), Limit(120, 10, o2), Limit(110, 5, o3)]
        l1.insert_limit(l2)
        l1.insert_limit(l3)
        o2.remove_order()
        self.assertTrue(l1.leftChild == None)
        self.assertTrue(l1.rightChild == None)
        self.assertTrue(l1.headOrder == o1 or l1.headOrder == o3)
        self.assertTrue(o1.nextOrder == o3 or o3.nextOrder == o1)


if __name__ == "__main__":
    unittest.main()
