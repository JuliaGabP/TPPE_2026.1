import pytest
from src.curador_dados import CuradorDeDados

class TestCaso5:
    def setup_method(self):
        self.curador = CuradorDeDados()

    @pytest.mark.caso_5
    @pytest.mark.parametrize("dados_entrada, esperado", [
        (
            [
                {"nome": "Raphael Goncalves Viana", "id": 433094},
                {"nome": "Raphael Goncalves Viana", "id": 31298},
                {"nome": "Raphael Goncalves Viana", "id": 549243},
                {"nome": "Yuri Vieira Faria", "id": 713897}
            ],
            [
                {"nome": "Raphael Goncalves Viana", "id": 31298},
                {"nome": "Raphael Goncalves Viana", "id": 31298},
                {"nome": "Raphael Goncalves Viana", "id": 31298},
                {"nome": "Yuri Vieira Faria", "id": 713897}
            ]
        ),
        (
            [
                {"nome": "Lilian Luíza Viana Vieira", "id": 899639},
                {"nome": "Lilian Luíza Viana Vieira", "id": 243351},
                {"nome": "Lilian Luíza Viana Vieira", "id": 663795},
                {"nome": "Lilian Luíza Viana Vieira", "id": 663795}
            ],
            [
                {"nome": "Lilian Luíza Viana Vieira", "id": 243351},
                {"nome": "Lilian Luíza Viana Vieira", "id": 243351},
                {"nome": "Lilian Luíza Viana Vieira", "id": 243351},
                {"nome": "Lilian Luíza Viana Vieira", "id": 243351}
            ]
        )
    ])
    def test_resolver_menor_id_por_nome(self, dados_entrada, esperado):
        resultado = self.curador.resolver_menor_id_por_nome(dados_entrada)
        assert resultado == esperado

    @pytest.mark.caso_5
    def test_excecao_lista_vazia(self):
        with pytest.raises(ValueError, match="A lista não pode estar vazia."):
            self.curador.resolver_menor_id_por_nome([])