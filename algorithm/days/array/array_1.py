#!/usr/bin/python
# -*- coding: utf-8 -*-


# 定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ O(n) 时间 O(1)空间

def find_only_one_in_array(nums):
    res = nums[0]
    for num in nums[1:]:
        res ^= num

    print(res)
    return res


# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
def find_only_one_in_array_three(nums):
    one = 0
    two = 0

    for x in nums:
        one = one ^ x & ~two
        two = two ^ x & ~one

    print(one)
    return one


if __name__ == '__main__':
    find_only_one_in_array([1, 2, 2, 1, 3])
    find_only_one_in_array_three([1, 1, 1, 3, 3, 4, 3])