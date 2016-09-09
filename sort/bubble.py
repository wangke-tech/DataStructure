#!/usr/bin/env python
# encoding: utf-8


"""冒泡排序
"""


def bubble(lst):
    flag = True
    for i in range(len(lst)):   # i=第i个冒出的气泡
        if flag:   # 如果前一个气泡在冒泡过程中，没有交换顺序
            flag = False
            j = len(lst) -2
            while(i <=j):
                if lst[j] > lst[j +1]:
                    lst[j], lst[j +1] = lst[j +1], lst[j]
                    flag = True
                j -=1
            i +=1
    return lst

if '__main__' == __name__:
    print bubble([5,8,2,2,1,3,4,5,6])
