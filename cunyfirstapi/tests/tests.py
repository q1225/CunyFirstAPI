###***********************************###
'''
CUNYFirstAPI
File: tests.py
Author: Ehud Adler
Core Maintainers: Ehud Adler, Akiva Sherman, 
Yehuda Moskovits
Copyright: Copyright 2019, Ehud Adler
License: MIT
'''
###***********************************###
import unittest

class TestTest(unittest.TestCase):
    def test(self):
        self.assertEqual(True, True)

def run_test():
    unittest.main()

def main():
    run_test()

if __name__ == '__main__':
    main()