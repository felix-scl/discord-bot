import requests
from bs4 import BeautifulSoup


def get_h1_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        h1 = soup.find('h1')
        if h1:
            return h1.text
        else:
            return False
    except requests.exceptions.RequestException as e:
        return f'An error has occurred while fetching the challenge name: {str(e)}'
