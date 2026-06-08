import unicodedata
import re

def tirar_acentos(texto: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def resolveCaso1Grafia(nomes: list) -> str:
    nomeCorreto = [re.sub(r"[`’‘´]", "'", nome) for nome in nomes]
    for nome in nomeCorreto:
        if nome != tirar_acentos(nome):
            return nome
    return nomeCorreto[-1]