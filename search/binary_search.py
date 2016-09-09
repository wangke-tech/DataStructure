#!/usr/bin/env python
# encoding: utf-8


def medium_index(low, high):
    return (low + high) /2 if 0==(low +high) %2 else (low +high) /2 +1


def binary_search(val, lst, low, high):

    index = medium_index(low, high)

    if val == lst[index]:
        print 'Find index', index

    elif val == lst[low]:
        index = low
        print 'Find index', index

    elif val == lst[high]:
        index = high
        print 'Find index', index

    elif lst[low] < val < lst[index]:
        high = index
        index = binary_search(val, lst, low, high)

    elif lst[index] < val < lst[high]:
        low = index
        index = binary_search(val, lst, low, high)

    return index


def binary_search_nonrec(val, lst):
    low, high = 0, len(lst) -1
    index = medium_index(low, high)

    while val != lst[index]:
        while lst[low] <= val < lst[index]:
            index = medium_index(low, index)
        while lst[index] < val <= lst[high]:
            index = medium_index(index, high)
    return index

if '__main__' == __name__:
    val = 12
    lst = [2, 10, 12, 23, 42, 53]
    low, high = 0, len(lst) -1
    index1 = binary_search(val, lst, low, high)
    index2 = binary_search_nonrec(val, lst)
    print index1, index2
