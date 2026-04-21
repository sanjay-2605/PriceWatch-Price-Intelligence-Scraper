import requests
from bs4 import BeautifulSoup
from .utils import get_headers, random_delay

def scrape_amazon(url):
    random_delay()
    res = requests.get(url, headers=get_headers())
    soup = BeautifulSoup(res.text, "html.parser")

    try:
        price = soup.select_one(".a-price-whole").text
        return float(price.replace(",", ""))
    except:
        return None
