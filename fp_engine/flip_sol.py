#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from secrets import randbelow

def fp_error(x, rx):
    tmp = (abs(i - j) for i, j in zip(x, rx))
    out = {e: i for i, e in enumerate(tmp)}
    return out

def flip_solution(x, rx):
    err = fp_error(x, rx)
    sort = sorted(err.keys())

    end = len(x)
    begin = randbelow(end - 1) + 1 
    for k in sort[begin:end]:
        i = err[k]
        rx[i] = (rx[i] + 1) % 2

    return rx