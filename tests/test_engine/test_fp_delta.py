#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import unittest
import numpy as np
from fp_engine.fp_binary.fp_utils import fp_round
from fp_engine.fp_binary.arg_min import fp_make_delta


class Round(unittest.TestCase):
    def test_round(self):
        sol = np.array([0.5, 0.75, 0.2])
        int_sol = fp_round(sol)
        self.assertTrue(np.array_equal(int_sol, np.array([0, 1, 0])))

    def test_delta(self):
        sol = np.array([0.5, 0.75, 0.2])
        int_sol = fp_round(sol)
        func = fp_make_delta(int_sol)
        delta = func(sol)
        self.assertEqual(0.95, delta)

if __name__ == '__main__':
    unittest.main()
