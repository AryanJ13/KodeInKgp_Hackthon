from re import L
from typing_extensions import Self
import time


# buyOrSell: True == Buy, False == Sell
class Order:
    def __init__(self, id, buyOrSell, price, size, placer: int, time) -> None:
        self.id: int = id
        self.buyOrSell: bool = buyOrSell
        self.price: int = price
        self.placer: int = placer
        self.time: int = time
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
            return -1
        elif self.prevOrder == None:
            self = self.nextOrder
        else:
            self.prevOrder.nextOrder = self.nextOrder
        return 0


class Limit:
    def __init__(self, order: Order) -> None:
        self.limitPrice: int = order.price
        self.size: int = order.quantity
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
        if parent == None:
            self = None
            return
        if self == parent.leftChild:
            parent.leftChild = None
        else:
            parent.rightChild = None
        self.parent = None
        return 0


class Book:
    def __init__(self) -> None:
        self.buyTree: Limit = None
        self.sellTree: Limit = None
        self.lowestSell: Limit = None
        self.highestBuy: Limit = None
        self.ordersBuy = dict()
        self.limitsBuy = dict()
        self.ordersSell = dict()
        self.limitsSell = dict()

    def insert(self, order: Order):
        if order.buyOrSell:
            limit =  self.limitsBuy[order.price] if order.price in self.limitsBuy else None
            if limit != None:
                limit.headOrder.insert_order(order)
            else:
                limit = Limit(order)
                if self.buyTree != None:
                    self.buyTree.insert_limit(limit)
                else: 
                    self.buyTree = limit
                self.ordersBuy[order.id] = order
                self.limitsBuy[order.price] = limit
        else:
            limit = self.limitsSell[order.price] if order.price in self.limitsSell else None
            if limit != None:
                limit.headOrder.insert_order(order)
            else:
                limit = Limit(order)
                self.buyTree.insert_limit(limit)
                self.ordersSell[order.id] = order
                self.limitsSell[order.price] = limit

    def get_lowestSell(self, node: Limit):
        if node.leftChild == None:
            self.lowestSell = node
            return
        return self.get_lowestSell(node.leftChild)

    def get_highestBuy(self, node: Limit):
        if node.rightChild == None:
            self.highestBuy = node
            return
        return self.get_highestBuy(node.rightChild)

    # Returns lowestSell
    def buy(self, quantity: int) -> list[Order]:
        head: Limit
        head = self.lowestSell
        # if quantity>= self.ordersBuy[head.headOrder.id]:
        orders = []
        orders = None
        node = None if head == None else head.headOrder
        while node != None:
            if quantity == 0:
                break
            elif quantity >= node.quantity:
                orders.append(node)
                quantity = quantity - node.quantity
                if node.remove_order() == -1:
                    self.get_highestBuy(self.buyTree)
                    self.get_lowestSell(self.buyTree)
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
        head = self.highestBuy
        orders = []
        node = None if head == None else head.headOrder
        while node != None:
            if quantity == 0:
                break
            elif quantity >= node.quantity:
                orders.append(node)
                quantity = quantity - node.quantity
                if node.remove_order() == -1:
                    self.get_highestBuy(self.buyTree)
                    self.get_lowestSell(self.buyTree)
            else:
                orders.append(node)
                quantity = 0
                node.quantity = node.quantity - quantity
            node = node.nextOrder
        return orders
        # pass


import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_insert_cancel(self):
        user = 1
        o1, o2, o3 = [
            Order(1, True, 110, 10, user, time.time()),
            Order(2, True, 120, 10, user, time.time()),
            Order(3, True, 110, 10, user, time.time()),
        ]
        l1, l2, l3 = [Limit(o1), Limit(o2), Limit(o3)]
        l1.insert_limit(l2)
        l1.insert_limit(l3)
        o2.remove_order()
        self.assertTrue(l1.leftChild == None)
        self.assertTrue(l1.rightChild == None)
        self.assertTrue(l1.headOrder == o1 or l1.headOrder == o3)
        self.assertTrue(o1.nextOrder == o3 or o3.nextOrder == o1)


if __name__ == "__main__":
    unittest.main()
