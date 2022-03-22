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
urlpage = 'https://www.google.com/search?q=meteo+{ville}'

# query the website and return the html to the variable 'page'
page = requests.get(urlpage).text
# On parse le html en utilisant beautiful soup et on le stocke dans la variable 'soup'
soup = BeautifulSoup(page, 'html.parser')
