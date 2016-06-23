# -*- coding:utf-8 -*-

'''
Json bilgisi
{
 "maps":[
         {"id":"blabla","kategori":"0"},
         {"id":"blabla","kategori":"0"}
        ],
"masks":
         {"id":"valore"},
"om_points":"value",
"parameters":
         {"id":"valore"}
}
'''

#json parse etmek icin eklenmesi gereken kutuphane
import json
#ekrana tum veriyi patlatmak icin gerekli
from pprint import pprint
#url den veri cekebilmek icin
import urllib2

#okunacak dosya
with open('data.json') as data_file:
    data = json.load(data_file)

#hepsini yazdır
print "Hepsini yazdirma:"
pprint(data)

#icerisindeki tek bir dataya ulasmak icin
print "\nTek bir veriye erisme islemi: " + data["maps"][0]["id"]
print data["parameters"]["id"]


### Siteden veri çekmek için yöntem ###
j = urllib2.urlopen('url_buraya')

j_obj = json.load(j)

pprint(j_obj)

### Var olan bir json cekmek icin baska yontem ###
### bu yontem icin python 3 gerekli ###

import json
import urllib.request
req = urllib.request.Request('url_buraya')
with urllib.request.urlopen(req) as response:
    result = json.loads(response.readall().decode('utf-8'))

### degisken icerisindeki json okuma ###
input = """
[
  { "id" : "001", 
    "x" : "2", 
    "name" : "Chuck" 
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]"""

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']

