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

# specify the url
urlpage = "http://api.openweathermap.org/data/2.5/weather?q=" + ville + \
    "&appid=18510638b7f670070f0c8aff37d87f2b&units=metric&lang=fr"

# query the website and return the html to the variable 'page'
page = requests.get(urlpage).text
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

print(soup)


weather = soup["weather"]

print(weather)
