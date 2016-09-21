#!/usr/bin/env python
# encoding: utf-8


class Node(object):

    __slots__ = ['_item', '_next']

    def __init__(self, item):
        self._item = item
        self._next = None

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setItem(self, newitem):
        self._item =newitem

    def setNext(self, newnext):
        self._next = newnext


class SingleLinkedlist():

    def __init__(self):
        self._head=None

    def isEmpty(self):
        return self._head==None

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count +=1
            current = current.getNext()
        return count

    def travel(self):
        current = self._head
        while current is not None:
            print current.getItem()
            current = current.getNext()

    def add(self, item):
        temp = Node(item)
        temp.setNext(self._head)

    def append(self, item):
        temp = Node(item)
        if self.isEmpty():
            self._head = temp
        else:
            current = self._head
            while current.getNext() is not  None:
                current = current.getNext()
            current.setNext(temp)

    def search(self, item):
        current = self._head
        founditem = False
        while current is not None and not founditem:
            if item == current.getItem():
                founditem = True
            else:
                current = current.getNext()

    def index(self, item):
        current = self._head
        count =0
        found =None
        while current is not None and not found:
            count +=1
            if current.getItem() == item:
                found = True
            else:
                current=current.getNext()
            if found:
                return count
            else:
                raise ValueError,'%s is not in linkedlist' %item

    def remove(self, item):
        current = self._head
        pre = None
        while current is not None:
            if item == current.getItem():
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()








