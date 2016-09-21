#!/usr/bin/env python
# encoding: utf-8


class BinaryTree(object):
    def __init__(self, root=None, left=None, right=None):
        self.root =root
        self.left =left
        self.right =right

    def insert_left(self, newnode):
        newnode = BinaryTree(newnode) if not isinstance(newnode, BinaryTree) else newnode
        if not self.left:
            self.left = newnode
        else:
            tree = newnode
            tree.left = self.left
            self.left = tree

    def insert_right(self, newnode):
        newnode = BinaryTree(newnode) if not isinstance(newnode, BinaryTree) else newnode
        if not self.right:
            self.right = newnode
        else:
            tree = BinaryTree(newnode)
            tree.left = self.left
            self.left = tree

    def get_left(self):
        return self.left

    def get_root(self):
        return self.root

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root

"""
r = BinaryTree('a')
print r.get_root_val()
r.insert_left('b')
print r.get_left()
print r.get_left().get_root_val()
r.insert_right('c')
print r.get_right()
print r.get_right().get_root_val()
r.get_right().set_root_val('hello')
print r.get_right().get_root_val()
print r.get_root_val()
"""

"""
                  a
                /   \
               b     c
              / \      \
             d   e      f
1、前序遍历
   a b d e c f


"""
tree = BinaryTree('a', BinaryTree('b'), BinaryTree('c'))
tree.get_left().insert_left('d')
tree.get_left().insert_right('e')
tree.get_right().insert_right('f')

