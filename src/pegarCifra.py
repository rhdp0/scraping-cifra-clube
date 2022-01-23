import requests
from bs4 import BeautifulSoup

class PegarCifra:
    def __init__(self, url):
        self.url = url
        self.cifra = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

    def pegar_cifra(self, nome_musica):
        site = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        try:
            cifras = soup.find_all('pre')
            self.cifra = cifras[0].get_text()
            print('Cifra salva com sucesso! ==> ' + nome_musica)
        except:
            print('Erro ao pegar a cifra: ' + nome_musica)

        return self.cifra