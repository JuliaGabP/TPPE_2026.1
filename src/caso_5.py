from typing import TypedDict
from src.registro_autor import RegistroAutor


class Caso5:
    
    def resolver_menor_id_por_nome(self, autores: list[RegistroAutor]) -> list[RegistroAutor]:
        if not autores:
            raise ValueError("A lista não pode estar vazia.")
        menores_ids = {}
        
        for autor in autores:
            nome_atual = autor["nome"]
            id_atual = autor["id"]
            
            if nome_atual not in menores_ids or id_atual < menores_ids[nome_atual]:
                menores_ids[nome_atual] = id_atual
                
        for autor in autores:
            autor["id"] = menores_ids[autor["nome"]]

        return autores
