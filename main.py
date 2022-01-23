import requests
from bs4 import BeautifulSoup

from src.listarMusicas import *
from src.pegarCifra import *
from src.salvarCifra import *

urlArtista = input('Cole aqui a url referente ao artista: ')

endPoints = ListaMusicas(urlArtista).href_musicas()
nomesMusicas = ListaMusicas(urlArtista).nome_musicas()
print('Numero de musicas: ', len(nomesMusicas))

for i in range(len(endPoints)):
    urlCifra = 'https://www.cifraclub.com.br' + endPoints[i]
    artista = ListaMusicas(urlArtista).artista()

    cifra = PegarCifra(urlCifra).pegar_cifra(nomesMusicas[i])

    Salvar().salvar_cifra(cifra, nomesMusicas[i], artista)
    
