import requests as r
from bs4 import BeautifulSoup as bs



def make_soup(url):
    """[summary]


    Args:
        url ([type]): Pass an argument like URL type

    Returns:
        [class 'bs4.BeautifulSoup']:   This function returns a BeautifulSoup object know as soup from the famus 
        library for scraping

    """
    try:
        response = r.get(url)
    except Exception :
        print("Something happends.. ")
    else:
        html = response.text
        soup =  bs(html, 'lxml')
    return soup




if __name__ == "__main__":
    make_soup()