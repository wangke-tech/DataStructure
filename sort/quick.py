#!/usr/bin/env python
# encoding: utf-8

"""快速排序
"""


def partition(lst, low, high):
    pivotkey = lst[low]
    while(low <high):
        while(low <high and pivotkey <=lst[high]):
            high -=1
        lst[low], lst[high] = lst[high], lst[low]
        while(low <high and lst[low] <=pivotkey):
            low +=1
        lst[low], lst[high] = lst[high], lst[low]
    return low


def quick_sort(lst, low, high):
    if low <high:
        pivot = partition(lst, low, high)
        quick_sort(lst, low, pivot -1)
        quick_sort(lst, pivot +1, high)
        return lst

if '__main__' == __name__:
    lst = [23, 10, 7, 2, 12, 42, 1, 29, 6]
    low, high = 0, len(lst) -1
    print quick_sort(lst, low, high)
