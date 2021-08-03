#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
【1， 2， 4， 5， 6】
结果 【1， 6， 2， 5， 4】
"""

from .demo import *


def reverse_N(head):
    while head.next.next:
        head = head.next

    last = head
    tmp = last.next
    last.next = None
    return tmp


class Solution:
    def reorderList(self, head):
        # write code here
        if head is None:
            return None

        bak = head
        while not (head.next is None or head.next.next is None):
            print_link_table(head)
            last = reverse_N(head)
            print('last ', last.val, 'cur next ', head.next.val)
            last.next = head.next
            print(last.next.val)
            head.next = last
            head = last.next

        print_link_table(bak)
        return bak


if __name__ == '__main__':
    head_node = create_node([1, 2])
    Solution().reorderList(head_node)
