#!/usr/bin/python
# -*- coding: utf-8 -*-

from demo import *


# 在O（N）时间内删除单链表节点
def delete_indict_node(head, indict_node):
    bak = head
    while head.next != indict_node:
        head = head.next

    head.next = indict_node.next
    return bak


# 在O（1）时间内删除单链表节点
def delete_indict_node_priority(head, indict_node):
    if indict_node.next is None:
        return delete_indict_node(head, indict_node)

    if head == indict_node:
        next_node = head.next
        head.next = None
        return next_node

    next_node = indict_node.next
    # indict_node = next_node
    indict_node.val = next_node.val
    indict_node.next = next_node.next
    return head


# 删除倒数第N个节点
def removeNthFromEnd(head, n):
    if head.next is None:
        return None

    fast = head
    low = head

    while fast.next is not None and n:
        fast = fast.next
        n -= 1

    if n == 1:
        return low.next

    while fast.next:
        fast = fast.next
        low = low.next

    low.next = low.next.next
    return head


if __name__ == '__main__':
    node4 = ListNode(1)
    node3 = ListNode(2, node4)
    node2 = ListNode(3, node3)
    node1 = ListNode(4, node2)

    # print_link_table(node1)
    # # head_node = delete_indict_node(node1, node3)
    # head_node = delete_indict_node_priority(node1, node3)
    # print_link_table(head_node)

    print("+++++++++++++++++++++++")
    print_link_table(node1)
    head = removeNthFromEnd(node1, 4)
    print_link_table(head)


