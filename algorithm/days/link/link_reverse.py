#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
【1， 2， 4， 5， 6】
结果 【1， 6， 2， 5， 4】
"""

from algorithm.days.link.demo import *


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


"""第二种方法"""


def reverse(head):
    if head is None:
        return None

    if head.next is None:
        return head

    last = reverse(head.next)

    head.next.next = head
    head.next = None
    return last


def get_length(head):
    cur = head
    length = 0
    while cur:
        cur = cur.next
        length += 1

    print('link node length %d' % length)
    return length


def reorder_list(head):
    from copy import deepcopy
    bak = deepcopy(head)
    t_head = reverse(bak)

    print(' ------------------ ')
    print_link_table(t_head)
    print_link_table(head)
    print(' ------------------ ')

    length = get_length(head)

    new_head = ListNode(-1)
    tail = new_head

    index = 0
    while head.val != t_head.val and index < (length // 2):
        print(head.val, t_head.val)
        node = ListNode(head.val)
        tail.next = node
        tail = node

        node = ListNode(t_head.val)
        tail.next = node
        tail = node

        head = head.next
        t_head = t_head.next

        index += 1

    if length % 2:
        node = ListNode(head.val)
        tail.next = node

    return new_head.next


if __name__ == '__main__':
    head_node = create_node([1, 2, 4, 3])
    # last = reverse(head_node)
    last = reorder_list(head_node)
    print_link_table(last)
