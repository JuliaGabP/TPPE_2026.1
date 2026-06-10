import re
import unicodedata
from src.registro_autor import RegistroAutor

class AutorInvalido(ValueError):
    pass
class CuradorDeDados:
    CONEXOES = {"DE", "DA", "DO", "DAS", "DOS"}
    def _remover_acentos(self, texto: str) -> str:
        texto_normalizado = unicodedata.normalize("NFD", texto)
        return "".join(
            caractere for caractere in texto_normalizado
            if unicodedata.category(caractere) != "Mn")
    def _normalizar_tokens(self, nome: str) -> list[str]:
        nome = nome.strip().upper()
        nome = self._remover_acentos(nome)
        nome = nome.replace(",", " ")
        nome = nome.replace(".", " ")
        nome = nome.replace("`", "'")
        nome = nome.replace("’", "'")
        tokens = re.split(r"\s+", nome)
        return [token for token in tokens if token]

    #Caso 1: Diferenças de Grafia
    def resolveCaso1Grafia(self, nomes: list) -> str:
        if not nomes:
            raise ValueError("A lista de nomes não pode estar vazia.")
        nomeCorreto = [re.sub(r"[`’‘´]", "'", nome) for nome in nomes]
        for nome in nomeCorreto:
            if nome != self._remover_acentos(nome):
                return nome
        return nomeCorreto[-1]

    #Caso 2: Sobrenome + Iniciais
    def corresponde_caso2(self, nome_completo: str, nome_abreviado: str) -> bool:
        if not nome_completo or not nome_abreviado:
            raise AutorInvalido("Nome do autor não pode ser vazio.")
        tokens_nome_completo = self._normalizar_tokens(nome_completo)
        tokens_nome_abreviado = self._normalizar_tokens(nome_abreviado)

        if len(tokens_nome_completo) < 2 or len(tokens_nome_abreviado) < 2:
            return False

        sobrenome_completo = tokens_nome_completo[-1]
        
        if tokens_nome_abreviado[-1] == sobrenome_completo:
            iniciais_abreviado_tokens = tokens_nome_abreviado[:-1]
        elif tokens_nome_abreviado[0] == sobrenome_completo:
            iniciais_abreviado_tokens = tokens_nome_abreviado[1:]
        else:
            return False

        iniciais_nome_completo = self._extrair_iniciais_nome_completo_c2(tokens_nome_completo)
        iniciais_nome_abreviado = [t[0] for t in iniciais_abreviado_tokens if t not in self.CONEXOES]

        return iniciais_nome_completo == iniciais_nome_abreviado

    def _extrair_iniciais_nome_completo_c2(self, tokens: list[str]) -> list[str]:
        nome_sem_sobrenome = tokens[:-1]
        return [token[0] for token in nome_sem_sobrenome if token not in self.CONEXOES]

    def _extrair_iniciais_nome_abreviado_c2(self, tokens: list[str]) -> list[str]:
        iniciais = tokens[1:]
        return [token[0] for token in iniciais if token not in self.CONEXOES]

    #Caso 3: Partículas "de" e Pontos Opcionais
    def resolver_caso3(self, nomes: list) -> str:
        if not nomes:
            raise ValueError("A lista não pode estar vazia.")
        return max(nomes, key=self._calcular_completude_c3)

    def _calcular_completude_c3(self, nome: str) -> int:
        pontuacao = len(nome)
        if "." in nome:
            pontuacao -= 10
        particulas = {"de", "da", "do", "das", "dos"}
        palavras = nome.lower().split()
        for p in palavras:
            if p in particulas:
                pontuacao += 5
        return pontuacao

    #Caso 4: Iniciais Agrupadas + Sobrenome
    def corresponde_caso4(self, nome_completo: str, nome_abreviado: str) -> bool:
        if not nome_completo or not nome_abreviado:
            raise AutorInvalido("Nome do autor não pode ser vazio.")
        tokens_nome_completo = self._normalizar_tokens(nome_completo)
        tokens_nome_abreviado = self._normalizar_tokens(nome_abreviado)

        if len(tokens_nome_completo) < 2 or len(tokens_nome_abreviado) != 2:
            return False
        
        iniciais_agrupadas = tokens_nome_abreviado[0]
        sobrenome_abreviado = tokens_nome_abreviado[1]
        sobrenome_completo = tokens_nome_completo[-1]
        iniciais_nome_completo = self._extrair_iniciais_agrupadas_c4(tokens_nome_completo)
        return(
            iniciais_nome_completo == iniciais_agrupadas
            and sobrenome_completo == sobrenome_abreviado)

    def _extrair_iniciais_agrupadas_c4(self, tokens: list[str]) -> str:
        nome_sem_ultimo_sobrenome = tokens[:-1]
        return "".join(token[0] for token in nome_sem_ultimo_sobrenome if token not in self.CONEXOES)

    #Caso 5: IDs Diferentes
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
