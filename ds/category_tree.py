#-*- coding:utf-8 -*-
class CatagoryTree(object):
    def __init__(self):
        self.tree = []
    class Node(object):
        def __init__(self,base,parent=(None),children=[]):#parent只能有一个，应该是Tuple类型。而children长度是可变的，应该是List类型
            self.base= base
            self.parent = parent
            self.children = children
    def add_catagory(self,a,b):
        #当b为None时，将a作为tree的根节点
        if b is None:
            a = self.Node(a)
            self.tree.append(a)
        else:
            #不然的话，就遍历tree
            flag = False
            for _ in self.tree:
                #当找到b时，将a插入b的孩子节点中
                if _.base ==b:
                    a = self.Node(a)
                    _.children.append(a)
                    a.parent = _.base
                    flag = True
                #当找不到b时，抛异常
            if not flag:
                print 'Parent Node %s is not exist!'%a


    def get_children(self,a):
        #遍历tree找a
            #if 找到:
                #return a.children
            #else:
                #return 'a is not exist.'
        it = iter(self.tree)
        while(True):
            try:
                _ = next(it)
                if _.base==a:
                    return [__.base for __ in _.children]
            except StopIteration:
                print 'Base Node %s !exist'%a
                break

if __name__== '__main__':
    c = CatagoryTree()
    c.add_catagory('A',None)
    c.add_catagory('B','A')
    c.add_catagory('C','A')
    print ','.join(c .get_children('A'))
    c.get_children('D')
    c.add_catagory('C','D')

