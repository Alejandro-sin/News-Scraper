'''

1. Me falta entender bien como exportar los modulos de mi propio archivo.

'''

from bs4 import bs
import requests as r


url = "https://www.wikipedia.org/"

def make_soup(url):
    try:
        response =  r.get(url)
    except Exception as e:
        print("There's nothung here")
    else:
        html_text = response.text()
        soup = bs(html_text, "html.parser")
    return soup.prettify()


make_soup(url)


    
