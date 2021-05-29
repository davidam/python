#!/usr/bin/python

import yaml

datos_yaml = '[{"DNS": "myHome.com", "IP": "192.168.1.100", "PUERTO": 80}, {"DNS": "mySSLHome.com", "IP": "192.168.1.100", "PUERTO": 443},{"DNS": "myProxyHome.com", "IP": "192.168.1.100", "PUERTO": 8080}]'

yaml_content = yaml.load(datos_yaml, Loader=yaml.FullLoader)

with open(r'files/conf_red.yaml', 'w') as file:
    documents = yaml.dump(yaml_content, file)
