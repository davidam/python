#!/usr/bin/python

f = open("files/gpl-3.0.txt", "r")
f2 = open("files/lineas1-15.txt", "w")
f3 = open("files/lineas16-20.txt", "w")

contLineas = 0

for linea in f:
    if contLineas < 15:
        f2.write(linea)
    elif contLineas < 20:
        f3.write(linea)
    contLineas = contLineas + 1


f.close()
f2.close()
f3.close()
