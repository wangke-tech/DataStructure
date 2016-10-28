#!/usr/bin/env python
# encoding: utf-8

"""
动态规划问题 1:

有n级台阶，一个人每次上1级或2级，问有多少种走完n级台阶的方法？
"""


def f(n):
    if n <=0:
        return 0
    if 0 < n <=2:
        return n
    else:
        return f(n -1) + f(n -2)

print __doc__

n =int(raw_input('input a num:\n'))

print '\nresult:\n', f(n)
