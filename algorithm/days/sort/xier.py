#!/usr/bin/python
# -*- coding: utf-8 -*-
"""希尔排序"""


"""
按照下标增量进行分组
对每组使用插入排序
随着增量减少，每组包含的关键字越来越多，增量减到1，整个序列被分为1组，算法终止
"""


def insert_sort(arr, length, start, gap):
    i = j = 0
    value = 0

    for i in range(start, length-start, gap):
        value = arr[i + gap]
        for j in range(i, start, -gap):
            if value < arr[j]:
                arr[j+gap] = arr[j]
            else:
                break

        arr[j+gap] = value




def shell_sort(arr):
    length = len(arr)

    gap = length // 2
    start = 0
    count = 0

    while gap > 0:
        start = 0

        while count < length:
            insert_sort(arr, length, start, gap)

            start += 1
            count += 1

        gap //= 2

    print(arr)

if __name__ == '__main__':
    shell_sort([8, 23, 64, 12, 0, 5, 6])