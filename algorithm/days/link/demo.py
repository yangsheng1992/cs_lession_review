#!/usr/bin/python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x, _next=None):
        self.val = x
        self.next = _next


def print_link_table(head):
    while head is not None:
        print(head.val, end='')
        head = head.next

    print('\n')


def create_node(list_):
    pre = None
    while list_:
        val = list_.pop()
        node = ListNode(val)
        node.next = pre
        pre = node

    print_link_table(pre)
    return pre
