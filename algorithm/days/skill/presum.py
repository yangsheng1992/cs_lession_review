#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

前缀和
"""


def _sum_interface(nums, i, j):
    """
    demand: O(1)
    :param nums: array
    :param i: index
    :param j: index
    :return: sum(array i...j)
    """


def build_pre_sum_array(nums):
    n = len(nums)
    pre_nums = [0] * (n + 1)
    for i in range(n):
        pre_nums[i + 1] = pre_nums[i] + nums[i]

    return pre_nums


def sub_array_sum(arrays, k):
    """
    给定一个子数组和一个整数k, 找到该数组中的和为K的连续的子数组的个数
    :return:
    """
    new_arrays = build_pre_sum_array(nums=arrays)
    n = len(arrays)

    res = []
    for i in range(1, n + 1):
        for j in range(i):
            if new_arrays[i] - new_arrays[j] == k:
                res.append((i, j))

    return res


def sub_array_sum_priority(arrays, k):
    """
    给定一个子数组和一个整数k, 找到该数组中的和为K的连续的子数组的个数
    :return:
    """

    n = len(arrays)
    pre_sum = {0: 1}

    ans = 0
    sum_i = 0
    for i in range(n):
        sum_i += arrays[i]

        sum_j = sum_i - k
        if pre_sum.get(sum_j):
            ans += pre_sum.get(sum_j)

        pre_sum[sum_i] = pre_sum.get(sum_i, 0) + 1
    print(pre_sum)
    return ans


def pre_sum_matrix(matrix):
    """
    二维矩阵中的前缀和
    这道题让你计算二维矩阵中子矩阵的元素之和
    :return: leetcode 304
    """

    def num_matrix():
        m, n = len(matrix), len(matrix[0])
        preSum = [[0] * (m+1) for i in range(n+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] + matrix[i-1][j-1] - preSum[i-1][j-1]

        print(preSum)
        return preSum

    def sum_region(x1, x2, y1, y2, preSum):
        return preSum[x2+1][y2+1] - preSum[x1][y2+1] - preSum[x2+1][y1] + preSum[x1][y1]

    print(sum_region(1, 2, 1, 2, num_matrix()))


if __name__ == '__main__':
    # results = sub_array_sum_priority([3, 5, 2, -2, 4, 1], 5)
    # print(results)
    pre_sum_matrix(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
         ]
    )