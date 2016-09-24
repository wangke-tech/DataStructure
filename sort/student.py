#!/usr/bin/env python
# encoding: utf-8
"""网易笔试题
   Student类里有name 和score，根据分数排名
   如果分数相同就按照原来顺序输出
"""


class Student(object):
    def __init__(self, name, score=0):
        self.__name = name
        self.__score = score

    def setName(self, name):
        self.__name = name

    def setScore(self, score):
        self.__score = score

    def getName(self):
        return self.__name

    def getScore(self):
        return self.__score


class Sort(object):
    def __init__(self, lst):
        self.lst = lst

    def devision(self, lst, low, high):
        privot = lst[low].getScore()
        while low <high:
            while low < high and privot <= lst[high].getScore():
                high -=1
            lst[low], lst[high] = lst[high], lst[low]
            while low < high and lst[low].getScore() <= privot:
                low +=1
            lst[low], lst[high] = lst[high], lst[low]
        return low

    def quick(self, lst, low, high):
        if low <high:
            privot = self.devision(self.lst, low, high)
            self.quick(self.lst, low, privot -1)
            self.quick(self.lst, privot +1, high)
            return self.lst

    def sort(self):
        objLst = self.quick(self.lst, 0, len(self.lst) -1)
        return [stu.getName() for stu in objLst]


s1 = Student('小明', 93)
s2 = Student('小张', 39)
s3 = Student('小红', 98)
s4 = Student('小芳', 98)

stuLst = Sort([s1, s2, s3, s4])
result = stuLst.sort()
print result
