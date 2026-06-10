import pytest
from src.curador_dados import CuradorDeDados

class TestCaso1:
    def setup_method(self):
        self.curador = CuradorDeDados()

    @pytest.mark.caso_1
    @pytest.mark.parametrize("variacoes, esperado", [
        (["Monica Hirata Sant`anna", "Mônica Hirata Sant’anna"], "Mônica Hirata Sant'anna"),
        (["Sergio Henrique Guaraldi", "Sérgio Henrique Guaraldi"], "Sérgio Henrique Guaraldi"),
        (["Veronica de Oliveira Moreira", "Verônica de Oliveira Moreira"], "Verônica de Oliveira Moreira")])
    def test_ResolverGrafia(self, variacoes, esperado):
        assert self.curador.resolveCaso1Grafia(variacoes) == esperado

    @pytest.mark.caso_1
    def test_ExcecaoListaVazia(self):
        with pytest.raises(ValueError, match="A lista de nomes não pode estar vazia."):
            self.curador.resolveCaso1Grafia([])