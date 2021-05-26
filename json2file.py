#!/usr/bin/python

import json

jsonvar = json.dumps(['Ubicacion', {'ciudad': 'madrid'}])
fo = open("files/fichero.json", "w")
fo.write(jsonvar)
fo.close()
