#!/usr/bin/python
# -*- coding: utf-8 -*-


# 邻接表 []
# 邻接矩阵 [[]]

class Vertex:
    def __init__(self, data, index):
        self.edges = []
        self.visited = False

    def add_edge(self, edge: "Edge"):
        self.edges.append(edge)


class Edge:
    _from: Vertex
    _to: Vertex
    _weight: float


"""
当然，当有向图含有环的时候才需要visited数组辅助，如果不含环，连visited数组都省了，基本就是多叉树的遍历。
一般使用邻接表即可满足需求，邻接矩阵会有浪费空间的问题
"""


class Graph:
    def __init__(self, nodes, relation):
        self.nodes = nodes
        self.relations = relation
        self.visit = []
        self.data = {}

    def build(self):
        # 有向无环
        node_list = []
        for i, node in enumerate(self.nodes):
            neighs = self.relations[i]
            node_list.append(Vertex(node, neighs))
        return node_list

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, negi):
        self.relations.append()

    def traverse(self, s):
        if self.visit[s]:
            return False

        self.visit[s] = True
        for neighbor in s.neighbors:
            self.traverse(neighbor)

        self.visit[s] = False


class NoDirGraph:
    def __init__(self):
        pass

    def build(self):
        pass


if __name__ == '__main__':
    graph = Graph([0, 1, 2, 3], [[1, 2], [3], [3], []])
    print(graph.build())
