from dataclasses import dataclass

@dataclass
class Article:
    title:str
    content:str
    author:str


@dataclass(init=False)
class PythonArticle(Article):
    language:str
    author:str
    price:int = 30

    def __init__(self,title,price):
        self.title = title
        self.price = price
        self.language = "Python 3"
        self.author = "Marcin Albiniak"
        self.content = "Opis wybranych zastosowań języka Python"

    def rabat(self):
        print(f"publikacja: {self.title}, autor: {self.author}, cena: {self.price:.2f} zł, "
              f"cena po rabacie: {0.86*self.price:.2f} zł")


pa = PythonArticle("Algorytmy DL w Pythonie",88)
print(pa)
pa.rabat()


