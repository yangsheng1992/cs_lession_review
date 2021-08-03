#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
本程序主要解决的是区间问题。区间问题主要包括以下几种:
1. 一个会议室怎么尽可能多的安排会议
2. 较短的视频拼接为较长的视频
3. 若干区间，某些区间可能被其他的覆盖了，找出并删除覆盖区间
4. 若干区间，将有重叠的区间合并
5. 区间交集，例子就是：计算冲突时段
6. 使会议室的闲置时间最少
7. 若干会议 申请会议室
"""
import statistics


class Task:
    def __init__(self):
        pass

    @staticmethod
    def sort_by_index(x, index):
        return x[index]


# 给若干会议 怎么申请会议室
class ApplyMeetingRoom:
    def __init__(self, meets):
        self.meets = meets

    def solution_one(self):
        meets = self.meets.copy()
        meets = sorted(meets, key=lambda x: Task.sort_by_index(x, 0))

        print(meets)
        end = 0
        count = 0

        for i in range(len(meets)):
            if meets[i][0] < meets[end][1]:
                count += 1
            else:
                end += 1

        print(count)

    def solution_two(self):
        meets = self.meets.copy()

        starts = []
        ends = []

        for i in meets:
            starts.append(i[0])
            ends.append(i[1])

        starts.sort()
        ends.sort()

        print(starts)
        print(ends)

        n = len(meets)
        i = 0
        j = 0
        count = 0
        res = 0
        while (i < n) and (j < n):
            if starts[i] < ends[j]:
                i += 1
                count += 1
            else:
                count -= 1
                j += 1

            res = max(count, res)

        print(res)

    def run(self):
        self.solution_one()
        self.solution_two()


# Interval Scheduling（区间调度问题）。给你很多形如[start,end]的闭区间，请你设计一个算法，
# 算出这些区间中最多有几个互不相交的区间。

class IntervalNotConflict:
    def __init__(self, intvs):
        self.intervals = intvs

    def solution_one(self):
        intvs = self.intervals.copy()
        intvs = sorted(intvs, key=lambda x: Task.sort_by_index(x, 1))

        print(intvs)
        end = 0
        count = 1

        n = len(intvs)

        for i in range(1, n):
            if intvs[i][0] < intvs[end][1]:
                continue
            else:
                end += i
                count += 1

        print(count)
        return count

    def solution_two(self):
        """leetcode 435 找需要移除区间的最小数量"""
        count = len(self.intervals) - self.solution_one()
        print(count)
        return count

    def solution_three(self):
        """第 452 题，用最少的箭头射爆气球："""
        intvs = self.intervals.copy()
        intvs = sorted(intvs, key=lambda x: Task.sort_by_index(x, 1))
        # 处理边界
        count = 1
        x_end = intvs[0][1]
        for interval in intvs:
            start = interval[0]
            if start > x_end:
                x_end = interval[1]
                count += 1

        print(count)
        return count

    def run(self):
        self.solution_one()
        self.solution_two()
        self.solution_three()


if __name__ == '__main__':
    # ApplyMeetingRoom([[1, 3], [2, 5], [3, 6]]).run()
    IntervalNotConflict(intvs=[[1, 3], [2, 4], [3, 6]]).run()
    IntervalNotConflict(intvs=[[10, 16], [2, 8], [1, 6], [7, 12]]).solution_three()
