#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from .arg_min import base_sol, build_constr, arg_min

from .fp_utils import is_integer, is_feasible, fp_round
from .flip_sol import flip_solution


def need_update(x, rx):
    for i, j in zip(x, rx):
        if round(i) != j:
            return True
    return False


def update_round(sol, int_sol):
    if need_update(sol, int_sol):
        out = fp_round(sol)
    else:
        out = flip_solution(sol, int_sol)
    return out


def feasibility_pump(c, A, b):
    rx = base_sol(c, A, b)
    constr = build_constr(A, b)

    if is_feasible(rx, A, b):
        return rx, True

    for _ in range(len(c) * 10):

        tmp = arg_min(rx, constr)
        if is_integer(tmp):
            out = tmp, True
            break

        rx = update_round(tmp, rx)

        if is_feasible(rx, A, b):
            out = rx, True
            break

    else:
        out = None, False

    return out
