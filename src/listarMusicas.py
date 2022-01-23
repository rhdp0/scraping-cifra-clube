import requests
from bs4 import BeautifulSoup

class ListaMusicas:
    def __init__(self, url):
        self.url = url
        self.musicas = []
        self.href = []
        self.nome_artista = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

    def nome_musicas(self):

        site = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        musicas = soup.find_all('a', class_='art_music-link')
        musica = musicas[0].get_text().strip()

        for musica in musicas:
            self.musicas.append(musica.get_text().strip())
            self.href.append(musica.get('href'))
                
        return self.musicas
    
    def href_musicas(self):

        site = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        musicas = soup.find_all('a', class_='art_music-link')
        musica = musicas[0].get_text().strip()

        for musica in musicas:
            self.href.append(musica.get('href'))
                
        return self.href
    
    def artista(self):

        site = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(site.content, 'html.parser')

        artista = soup.find_all('span', class_='t1')[0].get_text().strip()

        self.nome_artista = artista
                
        return self.nome_artista