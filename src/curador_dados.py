import re
import unicodedata


class AutorInvalido(ValueError):
    pass


class CuradorDeDados:
    CONEXOES = {"DE", "DA", "DO", "DAS", "DOS"}

    def corresponde_caso2(self, nome_completo: str, nome_abreviado: str) -> bool:
        self._validar_nomes(nome_completo, nome_abreviado)

        tokens_nome_completo = self._normalizar_tokens(nome_completo)
        tokens_nome_abreviado = self._normalizar_tokens(nome_abreviado)

        if self._nomes_invalidos_para_caso2(tokens_nome_completo, tokens_nome_abreviado):
            return False

        sobrenome_completo = self._obter_sobrenome(tokens_nome_completo)
        iniciais_abreviado = self._obter_iniciais_abreviadas_caso2(
            tokens_nome_abreviado,
            sobrenome_completo
        )

        if iniciais_abreviado is None:
            return False

        iniciais_completo = self._extrair_iniciais_nome_completo(
            tokens_nome_completo
        )

        return iniciais_completo == iniciais_abreviado

    def corresponde_caso4(self, nome_completo: str, nome_abreviado: str) -> bool:
        self._validar_nomes(nome_completo, nome_abreviado)

        tokens_nome_completo = self._normalizar_tokens(nome_completo)
        tokens_nome_abreviado = self._normalizar_tokens(nome_abreviado)

        if len(tokens_nome_completo) < 2 or len(tokens_nome_abreviado) != 2:
            return False

        iniciais_agrupadas = tokens_nome_abreviado[0]
        sobrenome_abreviado = tokens_nome_abreviado[1]

        sobrenome_completo = self._obter_sobrenome(tokens_nome_completo)
        iniciais_nome_completo = self._extrair_iniciais_agrupadas_caso4(
            tokens_nome_completo
        )

        return (
            iniciais_nome_completo == iniciais_agrupadas
            and sobrenome_completo == sobrenome_abreviado
        )

    def resolveCaso1Grafia(self, nomes: list) -> str:
        if not nomes:
            raise ValueError("A lista de nomes não pode estar vazia.")

        nomes_corrigidos = [
            re.sub(r"[`’‘´]", "'", nome)
            for nome in nomes
        ]

        for nome in nomes_corrigidos:
            if nome != self._remover_acentos(nome):
                return nome

        return nomes_corrigidos[-1]

    def resolver_caso3(self, nomes: list) -> str:
        if not nomes:
            raise ValueError("A lista não pode estar vazia.")

        return max(nomes, key=self._calcular_completude_caso3)

    def resolver_menor_id_por_nome(self, autores: list[dict]) -> list[dict]:
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

    def _validar_nomes(self, nome_completo: str, nome_abreviado: str) -> None:
        if not nome_completo or not nome_abreviado:
            raise AutorInvalido("Nome do autor não pode ser vazio.")

    def _nomes_invalidos_para_caso2(
        self,
        tokens_nome_completo: list[str],
        tokens_nome_abreviado: list[str]
    ) -> bool:
        return len(tokens_nome_completo) < 2 or len(tokens_nome_abreviado) < 2

    def _obter_sobrenome(self, tokens: list[str]) -> str:
        return tokens[-1]

    def _obter_iniciais_abreviadas_caso2(
        self,
        tokens_nome_abreviado: list[str],
        sobrenome_completo: str
    ) -> list[str] | None:
        if tokens_nome_abreviado[-1] == sobrenome_completo:
            tokens_iniciais = tokens_nome_abreviado[:-1]
        elif tokens_nome_abreviado[0] == sobrenome_completo:
            tokens_iniciais = tokens_nome_abreviado[1:]
        else:
            return None

        return self._extrair_iniciais(tokens_iniciais)

    def _extrair_iniciais_nome_completo(self, tokens: list[str]) -> list[str]:
        nome_sem_sobrenome = tokens[:-1]
        return self._extrair_iniciais(nome_sem_sobrenome)

    def _extrair_iniciais(self, tokens: list[str]) -> list[str]:
        return [
            token[0]
            for token in tokens
            if token not in self.CONEXOES
        ]

    def _extrair_iniciais_agrupadas_caso4(self, tokens: list[str]) -> str:
        nome_sem_ultimo_sobrenome = tokens[:-1]

        return "".join(
            token[0]
            for token in nome_sem_ultimo_sobrenome
            if token not in self.CONEXOES
        )

    def _calcular_completude_caso3(self, nome: str) -> int:
        pontuacao = len(nome)

        if "." in nome:
            pontuacao -= 10

        particulas = {"de", "da", "do", "das", "dos"}
        palavras = nome.lower().split()

        for palavra in palavras:
            if palavra in particulas:
                pontuacao += 5

        return pontuacao

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
