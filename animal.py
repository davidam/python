#!/usr/bin/python

class Animal(object):
    def __init__(self):
        self.estoyVivo = True

    def vivo():
        return self.estoyVivo 


class Gato(Animal):
    def __init__(self):
        sonido = ""

    def ronronear(self):
        sonido = "rrrr"
        return sonido

    def maullar(self):
        sonido = "miauuu"
        return sonido

    def grunir(self):
        sonido = "gggrrrr"
        return sonido


g = Gato()
print(g.ronronear())
print(g.maullar())
print(g.grunir())
print(g.vivo())
