# import libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests_cache
from pprint import pprint

requests_cache.install_cache('demo_cache')

# On demande à l'utilisateur de rentrer sa ville

ville = input("Quel est votre ville ").strip()

# url dynamique vers notre page web


def get_url_page(ville):
    page = 'https://www.google.com/search?q=meteo' + ville
    page = requests.get(page).text
    # On parse le html en utilisant beautiful soup et on le stocke dans la variable 'soup'
    return BeautifulSoup(page, 'html.parser')


print(get_url_page(ville))
