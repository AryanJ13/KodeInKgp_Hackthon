from typing import List
import numpy as np


class MinHeap:
    def __init__(self, depth: int):
        self.data = np.zeros((1 << depth,), dtype=np.int32)
        self.counter = -1

    def push(self, val):
        self.counter += 1
        self.data[self.counter] = val
        n = self.counter
        n_parent = (n - 1) // 2
        while n != 0 and self.data[n_parent] < val:
            self.data[n] = self.data[n_parent]
            self.data[n_parent] = val
            n = n_parent
            n_parent = (n - 1) // 2

    def pop(self):
        root = self.data[0]
        self.data[0] = self.data[self.counter]
        self.counter -= 1
        n = 0
        temp = self.data[0]
        c1 = n * 2 + 1
        c2 = n * 2 + 2
        while n <= self.counter:
            if c1 > self.counter:
                break
            if c2 <= self.counter and self.data[c1] < self.data[c2]:
                c1 = c2
            if self.data[c1] > temp:
                self.data[n] = self.data[c1]
                self.data[c1] = temp
                n = c1
                c1 = n * 2 + 1
                c2 = n * 2 + 2
            else:
                break
        return root

    def serialize(self) -> List:
        return self.data.tolist()


class MaxHeap:
    def __init__(self, depth: int):
        self.data = np.zeros((1 << depth,), dtype=np.int32)
        self.counter = -1

    def push(self, val):
        self.counter += 1
        self.data[self.counter] = val
        n = self.counter
        n_parent = (n - 1) // 2
        while n != 0 and self.data[n_parent] > val:
            self.data[n] = self.data[n_parent]
            self.data[n_parent] = val
            n = n_parent
            n_parent = (n - 1) // 2

    def pop(self):
        root = self.data[0]
        self.data[0] = self.data[self.counter]
        self.counter -= 1
        n = 0
        temp = self.data[0]
        c1 = n * 2 + 1
        c2 = n * 2 + 2
        while n <= self.counter:
            if c1 > self.counter:
                break
            if c2 <= self.counter and self.data[c1] < self.data[c2]:
                c1 = c2
            if self.data[c1] > temp:
                self.data[n] = self.data[c1]
                self.data[c1] = temp
                n = c1
                c1 = n * 2 + 1
                c2 = n * 2 + 2
            else:
                break
        return root

    def serialize(self) -> List:
        return self.data.tolist()
