# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rVv8niWnDK53b-B1ayiKHDQN4GTeOtSf
"""

from bs4 import BeautifulSoup
import requests
import json


dove_cercare = "lecco"
regione_ricerca = "lombardia"
comune_ricerca = "" #insert a city if you want to search within a city. void for searchin in region.
if not comune_ricerca:
  res = requests.get("https://www.subito.it/annunci-"+regione_ricerca+"/vendita/usato/"+dove_cercare+"/?q=gravel")
else:
  res = requests.get("https://www.subito.it/annunci-"+regione_ricerca+"/vendita/usato/"+dove_cercare+"/"+comune_ricerca+"/?q=gravel")

soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())

script = soup.find_all("script")
for s in script:
  if "__NEXT_DATA__" in str(s):
    #print(s)
    values = str(s)   
    
a = str(values)
fine = a.find("__NEXT_LOADED_PAGES_")
a=(a[24:fine-1])
js = json.loads(a)


print ("RICERCA: " + js["props"]["state"]["search"]["query"])
risultati = js["props"]["state"]["items"]["list"]
print ("Numero risultato: " + str(len(risultati)) + "\n")

res = risultati[0]["item"]
for res in risultati:
  print("---\n")
  body = res["item"]["body"]
  data = res["item"]["date"]
  prezzo = res["item"]["features"]["/price"]["values"][0]["value"]
  citta = res["item"]["geo"]["city"]["value"]
  url = res["item"]["urls"]["default"]
  img = res["item"]["images"][0]["scale"][4]["secureuri"]
  print(data +" "+citta +"\n")
  print(str(body))
  print(prezzo)
  print("url: " + url + "\n")
