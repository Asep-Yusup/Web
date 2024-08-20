import requests
from bs4 import BeautifulSoup


class sca:
    
    def scraping(self):
        link = input("Masukkan Link : ")
        html = requests.get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))