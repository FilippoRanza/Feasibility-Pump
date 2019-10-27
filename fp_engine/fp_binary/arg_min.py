#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import numpy as np
from scipy import optimize

from .fp_utils import fp_round


def fp_make_delta(int_sol):
    zeros = [i for i, j in enumerate(int_sol) if j == 0]
    ones = [i for i, j in enumerate(int_sol) if j == 1]
    amount = len(ones)

    def __out__(x):
        return x[zeros].sum() + amount - x[ones].sum()

    return __out__


def build_constr(A, b):
    out = [optimize.LinearConstraint(poly, -np.inf, n) for poly, n in zip(A, b)]
    return out


def base_sol(c, A, b):
    res = optimize.linprog(c, A_ub=A, b_ub=b)
    x = fp_round(res.x)
    return x


def arg_min(rx, constr):

    hess = np.zeros((len(rx), len(rx)))
    tmp = optimize.minimize(
        fp_make_delta(rx),
        rx,
        method="trust-constr",
        constraints=constr,
        bounds=optimize.Bounds(0, 1),
        hess=lambda x: hess,
    )
    return tmp.x
