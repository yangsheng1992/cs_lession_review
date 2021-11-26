#!/usr/bin/python
# -*- coding: utf-8 -*-


# 并查集
# 动态连通性
"""
这里所说的「连通」是一种等价关系，也就是说具有如下三个性质：

1、自反性：节点p和p是连通的。

2、对称性：如果节点p和q连通，那么q和p也连通。

3、传递性：如果节点p和q连通，q和r连通，那么p和r也连通。

"""


class UF:
    def union(self, p, q):
        "q p 相连"
        pass

    def find(self):
        "判断p q是否联通"
        pass

    def count(self):
        "返回图中有多少个连通分量"
        pass
