#!/usr/bin/python

from lxml import html
import requests

url = 'https://www.eldiario.es'
page = requests.get(url)
if page.status_code == 200:
    tree = html.fromstring(page.content)
    listaRef = tree.xpath('//@href')
    for ref in listaRef:
        if ref.find("/socios") != -1 and ref.startswith("https"):
            print("la url de socios es: " + ref)
else:
    print("Error al acceder a la pagina")
