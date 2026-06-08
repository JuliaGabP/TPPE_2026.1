import re
import unicodedata


class AutorInvalido(ValueError):
    pass


class Caso2:
    CONEXOES = {"DE", "DA", "DO", "DAS", "DOS"}

    def corresponde(self, nome_completo: str, nome_abreviado: str) -> bool:
        if not nome_completo or not nome_abreviado:
            raise AutorInvalido("Nome do autor não pode ser vazio.")

        tokens_nome_completo = self._normalizar_tokens(nome_completo)
        tokens_nome_abreviado = self._normalizar_tokens(nome_abreviado)

        if len(tokens_nome_completo) < 2 or len(tokens_nome_abreviado) < 2:
            return False

        sobrenome_completo = tokens_nome_completo[-1]
        sobrenome_abreviado = tokens_nome_abreviado[0]

        iniciais_nome_completo = self._extrair_iniciais_nome_completo(
            tokens_nome_completo
        )
        iniciais_nome_abreviado = self._extrair_iniciais_nome_abreviado(
            tokens_nome_abreviado
        )

        return (
            sobrenome_completo == sobrenome_abreviado
            and iniciais_nome_completo == iniciais_nome_abreviado
        )

    def _normalizar_tokens(self, nome: str) -> list[str]:
        nome = nome.strip().upper()
        nome = self._remover_acentos(nome)
        nome = nome.replace(",", " ")
        nome = nome.replace(".", " ")
        nome = nome.replace("`", "'")
        nome = nome.replace("’", "'")

        tokens = re.split(r"\s+", nome)
        return [token for token in tokens if token]

    def _remover_acentos(self, texto: str) -> str:
        texto_normalizado = unicodedata.normalize("NFD", texto)

        return "".join(
            caractere
            for caractere in texto_normalizado
            if unicodedata.category(caractere) != "Mn"
        )

    def _extrair_iniciais_nome_completo(
        self,
        tokens: list[str]
    ) -> list[str]:
        nome_sem_sobrenome = tokens[:-1]

        return [
            token[0]
            for token in nome_sem_sobrenome
            if token not in self.CONEXOES
        ]

    def _extrair_iniciais_nome_abreviado(
        self,
        tokens: list[str]
    ) -> list[str]:
        iniciais = tokens[1:]

        return [
            token[0]
            for token in iniciais
            if token not in self.CONEXOES
        ]
