#!/usr/bin/python

class Animal():
    def __init__(self):
        self.isVivo = True

    def vivo(self):
        print("Está vivo")
        return self.isVivo

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
print(g.isVivo())
