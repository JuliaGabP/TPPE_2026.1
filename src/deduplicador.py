from src.registro_autor import RegistroAutor
from src.curador_dados import CuradorDeDados


class DeduplicadorNomes:
    def __init__(self):
        self.curador = CuradorDeDados()

    def deduplicar_caso2(
        self,
        registros: list[RegistroAutor]
    ) -> list[RegistroAutor]:
        resultado = registros.copy()

        for registro_completo in registros:
            for indice, registro_candidato in enumerate(resultado):
                if registro_completo == registro_candidato:
                    continue

                if self.curador.corresponde_caso2(
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

                if self.curador.corresponde_caso4(
                    registro_completo.nome,
                    registro_candidato.nome
                ):
                    resultado[indice] = RegistroAutor(
                        id_autor=registro_candidato.id_autor,
                        nome=registro_completo.nome
                    )

        return resultado
