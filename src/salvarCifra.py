import os

class Salvar:
    def __init__(self):
        self.caminho = os.getcwd()
        self.arquivo = ''
        self.cifra = ''

    def salvar_cifra(self, cifra, nome_musica, nome_artista):
        ARTISTAS_DIR = os.path.join(self.caminho, 'Artistas')
        ARTISTA_DIR = os.path.join(ARTISTAS_DIR, nome_artista)

        if not os.path.exists(ARTISTAS_DIR):
            os.mkdir(ARTISTAS_DIR)
        if not os.path.exists(ARTISTA_DIR):
            os.mkdir(ARTISTA_DIR)

        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        for char in invalid_chars:
            nome_musica = nome_musica.replace(char, '_')

        self.cifra = cifra
        self.arquivo = os.path.join(ARTISTA_DIR, nome_musica + '.txt')

        with open(self.arquivo, 'w', encoding='utf8') as f:
            f.write(self.cifra)
        