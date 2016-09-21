#!/usr/bin/env python
# encoding: utf-8

from collections import namedtuple
from io import StringIO

# define the node structure
Node = namedtuple('Node', ['data','left','right'])
# initialize the tree
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 None(5, None, None),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))
            )
# read and wirte str in memory
output = StringIO()


# read the node and write the node's value
# if node is None, subtitute with 'N
def visitor(node):
    if node is not None:
        output.write('%i' %node.data)
    else:
        output.write('N')


# travle the tree with different order
def traversal(node, order):
    if node is None:
        visitor(node)
    else:
        op = {
            'N': lambda: visitor(node),
            'L': lambda: traversal(node.left, order),
            'R': lambda: traversal(node.right, order),
        }
    for x in order:
        op[x]()


# travel level by level
def travel_level_by_level(node):
    if node is not None:
        current_level = [node]
        while current_level:
            next_level = list()
            for n in current_level:
                if type(n) is str:
                    output.wirte('N')
                else:
                    output.write('%i' %n.data)
                    if n.left is not None:
                        next_level.append(n.left)
                    else:
                        next_level.append('N')
                    if n.right is not None:
                        next_level.append(n.right)
                    else:
                        next_level.append('N')
            output.wirte('\n')
            current_level = next_level
