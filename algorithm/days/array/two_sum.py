#!/usr/bin/python
# -*- coding: utf-8 -*-


"""无序数组"""


class NotSortArray:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def solution_ont(self):
        """暴力"""
        lenght = len(self.nums)
        for i in range(lenght):
            for j in range(i+1, lenght):
                if self.nums[i] + self.nums[j] == self.target:
                    return (i, j)

        return ()

    def solution_two(self):
        """map"""
        contains = {}
        for ind, num in enumerate(self.nums):
            if self.target - num in contains:
                return (contains[self.target - num], ind)
            contains[num] = ind

        return ()


# 有序数组

class SortArray:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def solution_one(self):
        n = len(self.nums)
        for i in range(n):
            target = self.target - self.nums[i]
            left, right = i + 1, n

            while left < right:
                mid = (right - left ) // 2 + left
                if self.nums[mid] == target:
                    return [i, mid]
                elif self.nums[mid] > target:
                    right = mid
                else:
                    left += 1
        return []

    def solution_two(self):
        low, high = 0, len(self.nums) - 1
        while low < high:
            total = self.nums[low] + self.nums[high]

            if total > self.target:
                high -= 1
            elif total < self.target:
                low += 1
            else:
                return [low, high]

        return []


if __name__ == '__main__':
    obj = NotSortArray([1, 4, 3, 6, 9], 8)
    print(obj.solution_two())
    print(obj.solution_ont())

    obj = SortArray([1, 2, 3, 6, 9], 8)
    print(obj.solution_two())
    print(obj.solution_one())
