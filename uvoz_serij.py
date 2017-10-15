import re
import requests
import os

f = open('serije.html', 'r', encoding = 'utf8')
vsebina_strani = f.read()
#print(vsebina_strani)


vzorec_serije = re.compile('<a href="http:\/\/www.imdb.com\/title\/tt'
                               '(?P<id>\d+)'
                                '(.*?)>'
                               '(?P<ime>.*?)'
                                '<\/a>'
                            )
flags = re.DOTALL #pika so vsi znaki, tudi znak za novo vrstico

# with open('serije.html', 'r') as f:
 #   vsebina_strani = f.read()
  #  print (f)

stevilo_najdenih = 0
for ujemanje in vzorec_serije.finditer(vsebina_strani):
    podatki = ujemanje.groupdict() #z groupdict nam da niz, vrne skupaj z imeni značk
    stevilo_najdenih += 1
    stran_z_detajli = requests.get('http://www.imdb.com/title/tt{}/?ref_=adv_li_tt'.format(podatki['id']))
    print(podatki)
print(stevilo_najdenih)

