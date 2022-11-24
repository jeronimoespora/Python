from bs4 import BeautifulSoup

import requests

miDoc=requests.get("http://python.beispiel.programmierenlernen.io/index.php")

docFinal=BeautifulSoup(miDoc.text, "html.parser")

iconos=docFinal.select(".emoji")

print(iconos[0].text)
