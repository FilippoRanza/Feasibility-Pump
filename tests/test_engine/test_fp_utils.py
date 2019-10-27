#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import unittest
import numpy as np
from fp_engine.fp_binary.fp_utils import is_integer, is_feasible


class TestUtils(unittest.TestCase):
    
    def test_integer(self):
        int_array = np.array([0.0, 1.0, 2.0, 5.0])
        self.assertTrue(is_integer(int_array))

        float_array = np.array([0.0, 1.0, 2.5, 5.0])
        self.assertFalse(is_integer(float_array))


    def test_feasible(self):
        consts = np.array([[2, -6, 3, -4, -1, 2]]) 
        value = np.array([-2]) 

        feasible = np.array([0, 1, 1, 0, 0, 0])
        self.assertTrue(is_feasible(feasible, consts, value))

        infeasible = np.zeros(6)
        self.assertFalse(is_feasible(infeasible, consts, value))
        


if __name__ == '__main__':
    unittest.main()
