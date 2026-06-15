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
        deduplicacao = DeduplicacaoCaso4(
            registros=registros,
            curador=self.curador
        )

        return deduplicacao.executar()


class DeduplicacaoCaso4:
    def __init__(
        self,
        registros: list[RegistroAutor],
        curador: CuradorDeDados
    ):
        self.registros = registros
        self.curador = curador
        self.resultado = registros.copy()

    def executar(self) -> list[RegistroAutor]:
        for registro_completo in self.registros:
            self._deduplicar_registro(registro_completo)

        return self.resultado

    def _deduplicar_registro(self, registro_completo: RegistroAutor) -> None:
        for indice, registro_candidato in enumerate(self.resultado):
            if self._deve_ignorar(registro_completo, registro_candidato):
                continue

            if self._sao_equivalentes(registro_completo, registro_candidato):
                self._substituir_por_nome_completo(
                    indice,
                    registro_completo,
                    registro_candidato
                )

    def _deve_ignorar(
        self,
        registro_completo: RegistroAutor,
        registro_candidato: RegistroAutor
    ) -> bool:
        return registro_completo == registro_candidato

    def _sao_equivalentes(
        self,
        registro_completo: RegistroAutor,
        registro_candidato: RegistroAutor
    ) -> bool:
        return self.curador.corresponde_caso4(
            registro_completo.nome,
            registro_candidato.nome
        )

    def _substituir_por_nome_completo(
        self,
        indice: int,
        registro_completo: RegistroAutor,
        registro_candidato: RegistroAutor
    ) -> None:
        self.resultado[indice] = RegistroAutor(
            id_autor=registro_candidato.id_autor,
            nome=registro_completo.nome
        )
