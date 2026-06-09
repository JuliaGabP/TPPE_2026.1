import re
import unicodedata


class AutorInvalido(ValueError):
    pass


class Caso4:
    def corresponde(self, nome_completo: str, nome_abreviado: str) -> bool:
        if not nome_completo or not nome_abreviado:
            raise AutorInvalido("Nome do autor não pode ser vazio.")

        tokens_nome_completo = self._normalizar_tokens(nome_completo)
        tokens_nome_abreviado = self._normalizar_tokens(nome_abreviado)

        if len(tokens_nome_completo) < 2 or len(tokens_nome_abreviado) != 2:
            return False

        iniciais_agrupadas = tokens_nome_abreviado[0]
        sobrenome_abreviado = tokens_nome_abreviado[1]

        sobrenome_completo = tokens_nome_completo[-1]
        iniciais_nome_completo = self._extrair_iniciais_agrupadas(
            tokens_nome_completo
        )

        return (
            iniciais_nome_completo == iniciais_agrupadas
            and sobrenome_completo == sobrenome_abreviado
        )

    def _normalizar_tokens(self, nome: str) -> list[str]:
        nome = nome.strip().upper()
        nome = self._remover_acentos(nome)
        nome = nome.replace(",", " ")
        nome = nome.replace(".", " ")

        tokens = re.split(r"\s+", nome)
        return [token for token in tokens if token]

    def _remover_acentos(self, texto: str) -> str:
        texto_normalizado = unicodedata.normalize("NFD", texto)

        return "".join(
            caractere
            for caractere in texto_normalizado
            if unicodedata.category(caractere) != "Mn"
        )

    def _extrair_iniciais_agrupadas(self, tokens: list[str]) -> str:
        nome_sem_ultimo_sobrenome = tokens[:-1]

        return "".join(
            token[0]
            for token in nome_sem_ultimo_sobrenome
        )
