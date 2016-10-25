#!/usr/bin/env python
# encoding: utf-8


"""
问题描述:
    有一个整形数组arr和一个大小为w的窗口从数组最左端滑倒数组最右端，窗口每次向右滑动一个位置。
返回:
    一个长度为n -w +1 的数组res，res[i]表示每个窗口状态下的最大值。

时间复杂度:
    O(N)

eg:

Input:
    [4, 3, 5, 4, 3, 3, 6, 7]

Output:
    [5, 5, 5, 4, 6, 7]

Process:
    max([4, 3, 5]) => 5
    max([3, 5, 4]) => 5
    max([5, 4, 3]) => 5
    max([4, 3, 3]) => 4
    max([3, 3, 6]) => 6
    max([3, 6, 7]) => 7

"""
solution = """

    # if 队列为空:
        # 直接入队
    # elif  第i个数 > 队列中最后一个数
        # 删除队列中的这个数，直到不满足条件
        # 入队
    # elif n <= 队列中的一个数:
        # 入队

    # 入队检测条件:
        # 设置超时
        #即 如果队头坐标为 i-w
            # 弹出队头
"""


def isQ4(Q, indexcurrent, lenwindow):

    if not Q:
        return False

    return Q[0] == indexcurrent -lenwindow

if '__main__' == __name__:
    data = '4 3 5 4 3 3 6 7'
    lenwindow = 3

    data = [int(n) for n in data.split(' ')]
    maxBQ = list()
    result = list()

    for i in range(len(data)):
        last = len(maxBQ) -1

        while maxBQ and data[i] > data[maxBQ[last]]:
                maxBQ.pop()
                last -=1

        if isQ4(maxBQ, i, lenwindow):
            del maxBQ[0]

        maxBQ.append(i)

        if i +1 >= lenwindow:
            result.append(data[maxBQ[0]])
    print result
