#!/usr/bin/python
# -*- coding: utf-8 -*-


from demo import *


def merge(head1, head2):
    list_ = []
    while head1 and head2:
        if head1.val <= head2.val:
            list_.append(head1.val)
            head1 = head1.next
        else:
            list_.append(head2.val)
            head2 = head2.next

    while head1:
        list_.append(head1.val)
        head1 = head1.next

    while head2:
        list_.append(head2.val)
        head2 = head2.next

    print(list_)


def merge_method_two(head1, head2):
    p = ListNode(None)
    tail = p

    while head1 and head2:
        if head1.val <= head2.val:
            node = ListNode(head1.val)
            tail.next = node
            tail = node
            head1 = head1.next
        else:
            node = ListNode(head2.val)
            tail.next = node
            tail = node
            head2 = head2.next

    while head1:
        node = ListNode(head1.val)
        tail.next = node
        tail = node
        head1 = head1.next

    while head2:
        node = ListNode(head2.val)
        tail.next = node
        tail = node
        head2 = head2.next

    return p.next


if __name__ == '__main__':
    head1 = create_node([1, 3, 5])
    head2 = create_node([2, 4, 6])

    head3 = merge_method_two(head1, head2)
    print_link_table(head3)