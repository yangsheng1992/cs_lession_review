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


if __name__ == '__main__':
    results = sub_array_sum_priority([3, 5, 2, -2, 4, 1], 5)
    print(results)
