#"""
#9Nov2018 Tarea JSON de cerouno
#Ada Martinez
#"""
#Impresion de titulos de una cadena json de web

import requests
import json
url='https://jsonplaceholder.typicode.com/posts/'
myrequest = requests.get(url)
print(type(myrequest))
ddic = json.loads(myrequest.text)
for row in ddic:
    print('Titulo:' + row['title'])