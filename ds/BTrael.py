#!/usr/bin/env python
# encoding: utf-8

from Queue import Queue
Stack = list


class BTree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

q, s = Queue(), Stack()

bt = BTree(1, BTree(2, 4, None), BTree(3, 5, 6))


def visitor(bt):
    if bt is None:
        return
    if int==type(bt):
        print bt
    else:
        print bt.data


def Q(bt):
    visitor(bt)
    if hasattr(bt, 'left'):
        q.put(bt.left)
    if hasattr(bt, 'right'):
        q.put(bt.right)


def S(bt):
    visitor(bt)
    if hasattr(bt, 'right'):
        s.append(bt.right)
    if hasattr(bt, 'left'):
        s.append(bt.left)

print ("\n#Travel by Width:\n")

Q(bt)
while not q.empty():
    Q(q.get())

print ("\n#Travel by Deepth:\n")

S(bt)
while s:
    S(s.pop())
