#!/usr/bin/env python
# encoding: utf-8

"""二叉树
"""


class binTNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


# 统计节点个数
def count_binTNodes(bin_tree):
    if not bin_tree:
        return 0
    else:
        return 1 + count_binTNodes(bin_tree.left) + count_binTNodes(bin_tree.right)


# 统计节点数据和
def sum_binTNodes(bin_tree):
    if not bin_tree:
        return 0
    else:
        return bin_tree.data + sum_binTNodes(bin_tree.left) + sum_binTNodes(bin_tree.right)


# 递归先序遍历
def pre_order(bin_tree, lst=[]):
    if not bin_tree:
        return
    else:
        lst.append(bin_tree.data)
        pre_order(bin_tree.left)
        pre_order(bin_tree.right)
    return lst


# 递归中序遍历
def mid_order(bin_tree, lst=[]):
    if not bin_tree:
        return
    else:
        mid_order(bin_tree.left)
        lst.append(bin_tree.data)
        mid_order(bin_tree.right)
    return lst

# 宽度优先遍历
#from SQueue import *
from  collections import deque

def levelorder(t, proc):
    qu = deque()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(data)


# 非递归先序遍历
def pre_order_nonrec(bin_tree, lst=[]):
    stack = []
    while bin_tree or stack:
        while bin_tree:
            lst.append(bin_tree.data)
            stack.append(bin_tree.right)
            bin_tree = bin_tree.left
        print 'stack',stack
        print 'stack is not None',stack is not None
        print 'stack',stack
        bin_tree = stack.pop()
        print 'bin_tree',bin_tree

    return lst

if '__main__' == __name__:
    t = binTNode(2, binTNode(4, binTNode(1, binTNode(3))), binTNode(5))
    print '节点数', count_binTNodes(t)
    print '节点和', sum_binTNodes(t)
    print '先序遍历结果', pre_order(t)
    print '中序遍历结果', mid_order(t)
    print '非递归先序遍历结果', pre_order_nonrec(t)

