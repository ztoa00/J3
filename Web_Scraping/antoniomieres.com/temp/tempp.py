import json
import urllib.request


url1 = "https://xintel.com.ar/api/?cache=08072020&json=fichas.propiedades&amaira=false&suc=ATM&global=LU3AIKPR4F6ZSUY8GQODKWRO8&emprendimiento=True&oppel=&esweb=&apiK=4m17zq256jvsm24wOnqbev43y&id=5921&_=1594194841261"
url2 = "https://xintel.com.ar/api/?cache=08072020&json=fichas.propiedades&amaira=false&suc=AT2&global=LU3AIKPR4F6ZSUY8GQODKWRO8&emprendimiento=True&oppel=&esweb=&apiK=4m17zq256jvsm24wOnqbev43y&id=5057&_=1594195092584"


response = urllib.request.urlopen(url2)

j = json.load(response)
"""
with open('j.json', 'w') as outfile:
    json.dump(j, outfile, sort_keys=True, indent=4)
"""


print(j['resultado']['ficha'][0]['in_tip'])
print(j['resultado']['ficha'][0]['in_loc'])
print(j['resultado']['ficha'][0]['in_bar'])
print(j['resultado']['ficha'][0]['in_cal'])
print(j['resultado']['ficha'][0]['precio'])
print(j['resultado']['superficie']['dato'][3])
