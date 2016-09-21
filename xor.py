#!/usr/bin/env python
# encoding: utf-8

""" xor 抑或运算
    输入: 两个十进制数
    输出: 两数的抑或运算
    思路：
          两个 10进制数 -> 2进制数
          把两个 2进制数 从尾到头(从较大数的最后一位到较小数的第一位)倒序比较
              如果相等:
                  修改较大数的当前位为0
              否则：
                  修改较大数的当前位为1
          较大数 -> 10进制
          返回 较大数

"""


def t_2_b(num):
    div, mod = num, -1
    lst = list()

    while 0 != div:
        mod = div %2
        div = div /2
        lst.append(mod)
    lst = [str(n) for n in reversed(lst)]
    return int(''.join(lst))


def b_2_t(num):
    lst = [int(_) for _ in str(num)]
    lenlst = len(lst)
    result = 0
    for index, value in enumerate(lst):
        result = result +(2 **(lenlst -index -1) if value and index != lenlst -1 else 0)
        result += lst[-1] if index == len(lst) -1 else 0

    return result


def xor(num1, num2):
    num1, num2 = t_2_b(num1), t_2_b(num2)
    lst1, lst2 = [n for n in str(num1)], [n for n in str(num2)]
    big_lst = lst1 if len(lst1) >= len(lst2) else lst2
    small_lst = lst2 if len(lst1) >= len(lst2) else lst1

    di = len(big_lst) - len(small_lst)
    for i in range(len(small_lst)):
        j = i +di
        big_lst[j] = 0 if big_lst[j] == small_lst[i] else 1
    big_lst[:j -1] = [1] * i

    return b_2_t(int(''.join(str(n) for n in big_lst)))

if '__main__' == __name__:
    print __doc__, '\n'
    num1, num2 = input('input num1:\n'), input('input num2:\n')
    print '\n\n#the binary from of num1(%d):bin(%d) \n' %(num1, t_2_b(num1))
    print '#the binary from of num2(%d):bin(%d) \n' %(num2, t_2_b(num2))
    print '\n\n*RESULT:   %d xor %d = %d\n\n' %(num1, num2, xor(num1, num2))
