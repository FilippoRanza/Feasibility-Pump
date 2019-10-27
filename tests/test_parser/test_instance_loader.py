#! /usr/bin/python


import unittest
from fp_engine.fp_parser.instance_loader import get_extension


class TestHelpers(unittest.TestCase):
    def test_get_extension(self):
        results = [('test.txt', 'txt'),  ('name.tar.bz', 'tar.bz'), ('name.', ''), ('name', None)]
        for name, ext in results:
            self.assertEqual(ext, get_extension(name))
            


if __name__ == '__main__':
    unittest.main()

