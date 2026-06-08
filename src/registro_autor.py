from dataclasses import dataclass

@dataclass(frozen=True)
class RegistroAutor:
    id_autor: int
    nome: str