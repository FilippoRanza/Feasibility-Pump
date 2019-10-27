#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import unittest
from tempfile import TemporaryDirectory
from os.path import join
import numpy as np
from fp_engine.fp_parser.json_parser import parse_data, load_json_instance


class TestJsonLoader(unittest.TestCase):
    def test_parse_data(self):
        instance = {
            "min": [1, 1],
            "constrs": [
                {"eq": [1, 1], "ge": 1},
                {"eq": [5, 10], "ge": 5},
                {"eq": [11, 5], "le": 11},
                {"eq": [11, 2], "le": 11},
            ],
        }

        c, A, b = parse_data(instance)

        valid_c = np.array([1, 1])
        valid_A = np.array([[-1, -1], [-5, -10], [11, 5], [11, 2]])
        valid_b = np.array([-1, -5, 11, 11])

        self.assertTrue(np.array_equal(c, valid_c))
        self.assertTrue(np.array_equal(A, valid_A))
        self.assertTrue(np.array_equal(b, valid_b))

    def test_json_loader(self):
        instance = """
        {
            "min" : [1, 1],
            "constrs":[
                {"eq": [1, 1], "ge": 1},
                {"eq": [5, 10], "ge": 5},
                {"eq": [11, 5], "le": 11},
                {"eq": [11, 2], "le": 11}
            ]
        }
        """

        with TemporaryDirectory() as temp_dir:
            path = join(temp_dir, "instance.json")
            with open(path, "w") as out:
                out.write(instance)

            c, A, b = load_json_instance(path)

            valid_c = np.array([1, 1])
            valid_A = np.array([[-1, -1], [-5, -10], [11, 5], [11, 2]])
            valid_b = np.array([-1, -5, 11, 11])

            self.assertTrue(np.array_equal(c, valid_c))
            self.assertTrue(np.array_equal(A, valid_A))
            self.assertTrue(np.array_equal(b, valid_b))


if __name__ == "__main__":
    unittest.main()
