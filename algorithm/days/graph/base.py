#!/usr/bin/python
# -*- coding: utf-8 -*-


class Vertex:
    def __init__(self, _id, neighbors : list):
        self.id = _id
        self.neighbors = neighbors

"""
当然，当有向图含有环的时候才需要visited数组辅助，如果不含环，连visited数组都省了，基本就是多叉树的遍历。
"""
class Graph:
    def __init__(self):
        self.visit = []

    def traverse(self, graph, s):
        if self.visit[s]:
            return False

        self.visit[s] = True
        for neighbor in graph.neighbors:
            self.traverse(neighbor)

        self.visit[s] = False
