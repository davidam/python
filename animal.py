#!/usr/bin/python

class animal(object):
    def vivo(self, vivo):
        vivo = true
        return vivo


class gato(animal):
    def ronronear(self, sonido):
        sonido="rrrr"
        return sonido
    def maullar(sonido):
        sonido="miauuu"
        return sonido
    def grunir(sonido):
        sonido="gggrrrr"
        return sonido


g = gato()

sonido=""
print(g.ronronear(sonido))
print(g.maullar())
print(g.grunir())
