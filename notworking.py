# import libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests_cache
from pprint import pprint

requests_cache.install_cache('demo_cache')

# On demande à l'utilisateur de rentrer sa ville

#ville = input("Quel est votre ville ").strip()

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
acceptLanguage = " fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5"


def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = userAgent
    session.headers['Accept-Language'] = acceptLanguage
    session.headers['Content-Language'] = acceptLanguage
    html = session.get(url)
    # create a new soup
    soup = BeautifulSoup(html.text, "html.parser")

    # stockage du résultat dans un dictionnaire
    result = {}
    # recuperation de la region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # temperature actuelle
    result['temp'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # jour et heure actuelle
    result['timestamp'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # météo
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
