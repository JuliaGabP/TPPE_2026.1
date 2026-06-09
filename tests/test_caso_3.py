import pytest
from src.caso_3 import CuradorCaso3

class TestCaso3:
    def setup_method(self):
        self.curador = CuradorCaso3()

    @pytest.mark.caso_3
    @pytest.mark.parametrize("variacoes, esperado", [
        (["Luiz Oliveira Souza", "Luiz de Oliveira de Souza", "Luiz de O. de Souza"], "Luiz de Oliveira de Souza"),
        (["Ana de Mattos Seabra", "Ana Mattos Seabra"], "Ana de Mattos Seabra")])
    def test_resolver_particulas_e_pontos(self, variacoes, esperado):
        assert self.curador.resolver_caso3(variacoes) == esperado

    @pytest.mark.caso_3
    def test_excecao_lista_vazia(self):
        with pytest.raises(ValueError, match="A lista não pode estar vazia."):
            self.curador.resolver_caso3([])