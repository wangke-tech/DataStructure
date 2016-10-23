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
    if type(bt) in (int, str):
        print bt
    else:
        print bt.data


def Q(bt):
    """
    elem: Node to be print.
    last: Point to the end Node in printing level.
    nlast:Point to the end Node in the level behind printing level.
    """

    q.put(bt)
    result = []
    atbegining =1

    while not q.empty():
        # Get the element to be printed.
        elem = q.get()

        if atbegining:
            # Init the LAST Pointer.
            last = elem
            atbegining =0

        if not elem:
            continue

        # Add the element to queue.
        result.append(elem if int ==type(elem) else elem.data)

        # Add the left children to the queue.
        if hasattr(elem, 'left'):
            q.put(elem.left)
            # Move NLAST Pointer to the lasted inserted node.
            nlast = elem.left

        # Add the right children to the queue.
        if hasattr(elem, 'right'):
            q.put(elem.right)
            # Move NLAST Pointer to the lasted inserted node.
            nlast = elem.right

        # add \n at each end of level in the binary tree.
        if last == elem:
            result.append('\n')
            last =nlast

    return '\n'.join(ch.lstrip() for ch in ' '.join(str(num) for num in result).split('\n'))


def S(bt):
    visitor(bt)
    if hasattr(bt, 'right'):
        s.append(bt.right)
    if hasattr(bt, 'left'):
        s.append(bt.left)

print ("\n#Travel by Width:\n"), Q(bt)

#while not q.empty():
#    print q.get()

print ("\n#Travel by Deepth:\n")

S(bt)
while s:
    S(s.pop())
