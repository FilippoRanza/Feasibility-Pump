#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import unittest
import numpy as np
from scipy import optimize
from fp_engine.fp_binary.fp_binary import need_update, update_round, feasibility_pump


class TestUpdate(unittest.TestCase):
    def test_need_update(self):
        sol = np.array([0.5, 0.75, 0.2])
        
        int_sol = np.array([0, 1, 0])
        self.assertFalse(need_update(sol, int_sol))

        update_sol = np.array([0, 1, 1])
        self.assertTrue(need_update(sol, update_sol))

    def test_update_result(self):
        sol = np.array([0.5, 0.75, 0.2])
        old_sol = np.array([0, 1, 1])
        new_sol = np.array([0, 1, 0])
        
        # old_sol and new_sol will be modified in place
        # round given solution
        int_sol = update_round(sol, old_sol)
        self.assertTrue(np.array_equal(new_sol, int_sol))

        # flip some bits in give solution
        rnd_sol = update_round(sol, new_sol)
        self.assertFalse(np.array_equal(int_sol, rnd_sol))
        

class TestFeasibilityPump(unittest.TestCase):

    def test_feasible_problem(self):
        """
        this problem is feasible as LP or
        binary MIP
        """
        c = np.array([1, 1])                                                                                                                                                                 
        A = np.array([[-1, -1], [-5, -10], [11, 5], [11, 2]])                                                                                                                                  
        b = np.array([-1, -5, 11, 11])   

        lp_sol = optimize.linprog(c, A, b)
        self.assertTrue(lp_sol.success)

        _, stat = feasibility_pump(c, A, b)
        self.assertTrue(stat)

    def test_unfeasilbe_problem(self):
        """
        this problem is feasible as LP but
        not as a binary MIP
        """
        c = np.array([1, 1])                                                                                                                                                                 
        A = np.array([[-2, -0.5], [-4, -10], [11, 5], [11, 2]])                                                                                                                                  
        b = np.array([-1, -5, 11, 11]) 

        lp_sol = optimize.linprog(c, A, b)
        self.assertTrue(lp_sol.success)

        sol, stat = feasibility_pump(c, A, b)
        self.assertFalse(stat)
        self.assertIsNone(sol)

if __name__ == '__main__':
    unittest.main()
