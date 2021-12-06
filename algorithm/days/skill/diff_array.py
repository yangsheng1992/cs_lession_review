#!/usr/bin/python
# -*- coding: utf-8 -*-


# 差分数组
# 适用于 频繁对原始数组的某个区间进行增减

def prefix_num(nums):
    n = len(nums)

    diff = [nums[0]]
    for i in range(1, n):
        diff.append(nums[i] - nums[i-1])

    print(diff)
    return diff


class Difference:
    def __init__(self, nums):
        self.prefix_nums = prefix_num(nums)

    def increment(self, i, j, val):
        self.prefix_nums[i] += val
        if j + 1 < len(self.prefix_nums):
            self.prefix_nums[j+1] -= val

    def result(self):
        res = [self.prefix_nums[0]]
        for i in range(1, len(self.prefix_nums)):
            res.append(res[i-1] + self.prefix_nums[i])
        return res

    @property
    def diff(self):
        return self.prefix_nums

    def __str__(self):
        print('diff nums:', self.prefix_nums)
        print('recovery: ', self.result())
        return '-----'


if __name__ == '__main__':
    # prefix_num([1,2,3])
    diff = Difference([1, 2, 3, 4, 5, 6, 7])
    print(diff)
    diff.increment(1, 4, 2)
    print(diff)
    diff.increment(2, 3, -2)
    print(diff)