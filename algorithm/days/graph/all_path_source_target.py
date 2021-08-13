#!/usr/bin/python
# -*- coding: utf-8 -*-


# leetcode 797


"""
题目输入一幅有向无环图，这个图包含n个节点，标号为0, 1, 2,..., n - 1，请你计算所有从节点0到节点n - 1的路径
"""

res = []


def traverse(graph, s, path: list):
    path.append(s)

    n = len(graph)

    if s == n - 1:
        res.append(path.copy())
        path.remove(s)

        return

    for i in graph[s]:
        traverse(graph, i, path)

    path.remove(s)


def solution(graph: list[list]):

    path = []
    traverse(graph, 0, path)
    return


if __name__ == '__main__':
    solution([[1, 2], [3], [3], []])
    print(res)