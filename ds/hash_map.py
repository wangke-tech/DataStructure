#!/usr/bin/env python
# encoding: utf-8


keys = []
diarr = []

di = 0


def get_key(hasharr, value, di=0, arr_len=10):
    # 计算key
    # (value + di ) % arr_len
    key = (value + di) % 10
    if key <= arr_len -1 and not hasharr[key]:
        pass
    elif key <= arr_len -1 and hasharr[key]:
        di +=1
        key, di = get_key(hasharr, value, di)
    else:
        raise KeyError
    return key, di


def read(hasharr, value, di=0, arr_len=10):
    key = (value + di) % 10
    while value != hasharr[key]:
        di +=1
        key, di = read(hasharr, value,di)
    return key, di


def get_hash_table(arr):
    # 重复下列步骤，直到arr最后一个元素
        # 计算key
        #  直到arr 的key位置为空
            # 计算key(添加限定条件，实在算不出key来就抛异常)

        # hash_arr[key] = value (此时，arr[key]为空)
    # 返回 hash_arr
    lenarr = len(arr)

    hasharr = [False] *10
    for di in range(lenarr):

        value = arr[di]
        key, di = get_key(hasharr, value, di)
        flag = True
        while hasharr[key] and flag:
            flag = False
            key, di = get_key(hasharr, value, di)
        if flag is False:
            continue
        hasharr[key] = value
        diarr.append(di)
    return hasharr


def find(hasharr, value,di=0):
    # arr = [81, 45, 11, 23, 93, 15]
    key, di = read(hasharr, value)
    i = 0
    while value != hasharr[key] and i <10:
        di +=1
        key, di = read(hasharr, value, di)
        print 73, key
        i +=1
    return key


if '__main__' == __name__:

    arr = [81, 45, 11, 23, 93, 15]
    print 'originarr', arr

    hasharr = get_hash_table(arr)
    print 'hasharr', hasharr

    print hasharr[find(hasharr, 23)]
