#!/usr/bin/python

import yaml

yaml_file = open("files/conf_red.yaml", 'r')
yaml_content_list = yaml.load(yaml_file, Loader=yaml.FullLoader)

for dato_dict in yaml_content_list:
    DNS=dato_dict['DNS']
    IP=dato_dict['IP']
    PUERTO=dato_dict['PUERTO']
    print("El DNS: " + DNS + " se conecta por " + IP + ":" + str(PUERTO))
