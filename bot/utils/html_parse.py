import requests
from bs4 import BeautifulSoup


def get_h1_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h1 = soup.find('h1')
    if h1:
        return h1.text
    else:
        return False
