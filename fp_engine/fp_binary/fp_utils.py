#! /usr/bin/python


import numpy as np

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>


def fp_round(x):
    tmp = map(round, x)
    return np.array(list(tmp))


def is_integer(x):
    for i in x:
        if int(i) != i:
            return False
    return True


def is_feasible(x, A, b):
    for poly, n in zip(A, b):
        if poly.dot(x) > n:
            return False
    return True
