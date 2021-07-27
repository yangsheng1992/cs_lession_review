#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The
definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is
to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B.
You need to find out the celebrity (or verify there is not one) by asking as few questions as possible
(in the asymptotic sense).

You are given a helper function bool knows(a, b)which tells you whether A knows B.
Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party.
 Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1
"""


def knows(a, b) -> bool:
    return True if tables[a][b] else False


def find_celebrity(n: int) -> int:
    if n <= 0:
        return -1

    if n == 1:
        return 0

    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    for i in range(n):
        if i == candidate:
            continue

        if not knows(i, candidate):
            return -1

        if knows(candidate, i):
            return -1

    return candidate


def find_celebrity_2(n):
    if n == 1:
        return 0

    candidate = 0
    for other in range(1, n):
        if knows(candidate, other) or not knows(other, candidate):
            candidate = other
        else:
            pass

    for other in range(n):
        if other == candidate:
            continue

        if knows(candidate, other) or not knows(other, candidate):
            return -1

    return candidate


if __name__ == '__main__':
    tables = [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    tables = [
        [1, 1, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]
    print(find_celebrity(3))
    assert find_celebrity_2(3) == 1

    tables = [
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1]
    ]
    print(find_celebrity(3))
    assert find_celebrity_2(3) == 2