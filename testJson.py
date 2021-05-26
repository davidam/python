#!/usr/bin/python

import unittest
import json


class myTestJson(unittest.TestCase):

    def testJson(self):
        f = open("files/fichero.json")
        datos = f.read()
        myjson = json.loads(datos)
        print(myjson)
        self.assertEqual(myjson[1], {'ciudad': 'madrid'})
        f.close()
