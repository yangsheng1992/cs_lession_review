#!/usr/bin/python
# -*- coding: utf-8 -*-


from demo import *


def single_reverse_method_one(head):
    pre = None

    print_link_table(head)
    while head:
        cur = head.next
        head.next = pre

        pre = head
        head = cur

    print_link_table(pre)


def single_reverse_method_two(head):
    if head is None:
        return
    if head.next is None:
        return head

    last = single_reverse_method_two(head.next)
    head.next.next = head
    head.next = None
    return last


def reverse_k_group(head, k):
    pass


def reverse_between_n_m(head, n, m):
    pre = None
    diff = m - n + 1

    while n:
        pre = head
        head = head.next
        n -= 1

    tail = head
    diff_bak = diff
    while diff_bak:
        tail = tail.next
        diff_bak -= 1

    bak = tail
    while head and diff:
        next_ = head.next
        head.next = bak
        bak = head
        head = next_

        diff -= 1

    print_link_table(bak)
    pre.next = bak
    return pre


global successor


def reverse_n(head, n):
    if head is None:
        return

    if n == 1:
        global successor
        successor = head.next
        return head

    last = reverse_n(head.next, n - 1)
    head.next.next = head
    head.next = successor
    return last


def reverse_between_n_m_method_two(head, m, n):

    if m == 1:
        return reverse_n(head, n)

    head.next = reverse_between_n_m(head.next, m - 1, n - 1)
    return head


if __name__ == '__main__':
    root = create_node([1, 2, 3, 4])
    single_reverse_method_one(root)
    print('++++++++++++++++++++++++++++')
    root = create_node([1, 2, 3, 4])
    last_node = single_reverse_method_two(root)
    print_link_table(last_node)
    print('++++++++++++++++++++++++++++')

    root = create_node([1, 2, 3, 4, 5])
    head = reverse_between_n_m(root, 1, 3)
    print('reverse between ', )
    print_link_table(head)

    print('++++++++++++++++++++++++++++')

    root = create_node([1, 2, 3, 4, 5])
    head = reverse_between_n_m_method_two(root, 1, 3)
    print('reverse between ', )
    print_link_table(head)
