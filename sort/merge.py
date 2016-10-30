#!/usr/bin/env python
# encoding: utf-8


def merge_sort(lst):
    if len(lst) <=1:
        return lst
    num = int(len(lst) //2)
    left = merge_sort(lst[ :num])
    right = merge_sort(lst[num:])
    return merge(left, right)


def merge(left, right):
    l, r =0, 0
    result = []
    while l <len(left) and r <len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l +=1
        else:
            result.append(right[r])
            r +=1

    result += left[l:]
    result += right[r:]
    return result

if '__main__' == __name__:
    lst0 = []
    lst1 = [1, ]
    lst2 = [1, -1, 0, 2, 3, 7, 3, 4, 2, 5]
    for lst in [lst0, lst1, lst2]:
        print merge_sort(lst)
