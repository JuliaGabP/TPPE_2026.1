class CuradorCaso3:
    def _calcular_completude(self, nome: str) -> int:
        pontuacao = len(nome)
        if "." in nome:
            pontuacao -= 10
        particulas = {"de", "da", "do", "das", "dos"}
        palavras = nome.lower().split()
        for p in palavras:
            if p in particulas:
                pontuacao += 5
        return pontuacao

    def resolver_caso3(self, nomes: list) -> str:
        if not nomes:
            raise ValueError("A lista não pode estar vazia.")
        return max(nomes, key=self._calcular_completude)