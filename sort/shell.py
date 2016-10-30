#!/usr/bin/env python
# encoding: utf-8


def shell_sort(lst):
    lenLst = len(lst)
    gap = int(round(lenLst /2))
    while gap >0:
        for i in range(gap, lenLst):
            tmp = lst[i]
            j =i
            while j >= gap and tmp <lst[j -gap]:
                lst[j] = lst[j -gap]
                j -=gap
            lst[j] = tmp
        gap = int(round(gap /2))
    return lst

if '__main__' == __name__:
    lst0 = [1, 4, 2, 5, 6, 3, 9, 8, 0, 0, -1]
    lst1 = [0]
    for lst in [lst0, lst1]:
        print shell_sort(lst)
