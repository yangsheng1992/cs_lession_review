#!/usr/bin/python
# -*- coding: utf-8 -*-

import celery


@celery.task
def sum_(*iterables):
    return sum(iterables)


@celery.task
def mul(a, b):
    return a * b
