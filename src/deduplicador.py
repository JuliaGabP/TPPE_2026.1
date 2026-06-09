from src.registro_autor import RegistroAutor
from src.caso_2 import Caso2
from src.caso_4 import Caso4


class DeduplicadorNomes:
    def __init__(self):
        self.caso2 = Caso2()
        self.caso4 = Caso4()

    def deduplicar_caso2(
        self,
        registros: list[RegistroAutor]
    ) -> list[RegistroAutor]:
        resultado = registros.copy()

        for registro_completo in registros:
            for indice, registro_candidato in enumerate(resultado):
                if registro_completo == registro_candidato:
                    continue

                if self.caso2.corresponde(
                    registro_completo.nome,
                    registro_candidato.nome
                ):
                    resultado[indice] = RegistroAutor(
                        id_autor=registro_candidato.id_autor,
                        nome=registro_completo.nome
                    )

        return resultado
        
    def deduplicar_caso4(
        self,
        registros: list[RegistroAutor]
    ) -> list[RegistroAutor]:
        resultado = registros.copy()

        for registro_completo in registros:
            for indice, registro_candidato in enumerate(resultado):
                if registro_completo == registro_candidato:
                    continue

                if self.caso4.corresponde(
                    registro_completo.nome,
                    registro_candidato.nome
                ):
                    resultado[indice] = RegistroAutor(
                        id_autor=registro_candidato.id_autor,
                        nome=registro_completo.nome
                    )

        return resultado
