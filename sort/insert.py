#!/usr/bin/env python
# encoding: utf-8


def insert_sort(lst):
    for i in range(1, len(lst)):
        j = i -1
        tmp = lst[i]
        while j >= 0 and lst[i] < lst[j]:
            lst[j +1] = lst[j]
            j -=1
        lst[j +1] = tmp
    return lst

if '__main__' == __name__:
    print insert_sort([1, 4, 2, 5, 10])
