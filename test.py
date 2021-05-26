#!/usr/bin/python

import unittest


class myTest(unittest.TestCase):

    def testNumber(self):
        num = 2 + 2 + 5
        self.assertEqual(num, 9)
