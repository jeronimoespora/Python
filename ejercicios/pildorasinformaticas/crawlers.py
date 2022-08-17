from bs4 import BeautifulSoup

import requests


class PostCrawled:
    def __init__(self, titulo, emoticon, contenido, imagen):

        self.titulo = titulo
        self.emoticon = emoticon
        self.contenido = contenido
        self.imagen = imagen


class PostExtractor:
    def extraeInfo(self):

        miDoc = requests.get("http://python.beispiel.programmierenlernen.io/index.php")

        docFinal = BeautifulSoup(miDoc.text, "html.parser")

        posts = []

        for card in docFinal.select(".card"):
            titulo = card.select(".card-title span")[1].text
            emoticon = card.select_one(".emoji").text
            contenido = card.select_one(".card-text").text
            imagen = card.select_one("img").attrs["src"]

            crawled = PostCrawled(titulo, emoticon, contenido, imagen)
            posts.append(crawled)

        return posts


unPost = PostExtractor()

listaPosts = unPost.extraeInfo()


for elPost in listaPosts:

    print(elPost.emoticon)
    print(elPost.titulo)
    print(elPost.contenido)
    print(elPost.imagen)
    print()

# print(listaPosts)
