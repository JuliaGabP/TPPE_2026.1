import unicodedata
import re

class CuradorDeDados:
    def tirar_acentos(self, texto: str) -> str:
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    
    def resolveCaso1Grafia(self, nomes: list) -> str:
        if not nomes:
            raise ValueError("A lista de nomes não pode estar vazia.")
        nomeCorreto = [re.sub(r"[`’‘´]", "'", nome) for nome in nomes]
        for nome in nomeCorreto:
            if nome != self.tirar_acentos(nome):
                return nome
        return nomeCorreto[-1]