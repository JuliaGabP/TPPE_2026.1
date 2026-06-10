import pytest

from src.registro_autor import RegistroAutor
from src.curador_dados import CuradorDeDados, AutorInvalido
from src.deduplicador import DeduplicadorNomes


@pytest.mark.caso_4
@pytest.mark.parametrize(
    "nome_completo, nome_abreviado",
    [
        ("Vanilda Cristina Junior", "VC Junior"),
        ("Sérgio Henrique Guaraldi", "SH Guaraldi"),
        ("Ana Mattos Seabra", "AM Seabra"),
        ("Ana de Mattos Seabra", "AM Seabra"),
    ],
)
def test_caso4_corresponde_iniciais_agrupadas_mais_sobrenome(
    nome_completo,
    nome_abreviado
):
    caso4 = CuradorDeDados()

    assert caso4.corresponde_caso4(nome_completo, nome_abreviado)


@pytest.mark.caso_4
@pytest.mark.parametrize(
    "nome_completo, nome_abreviado",
    [
        ("Vanilda Cristina Junior", "VH Junior"),
        ("Sérgio Henrique Guaraldi", "SG Guaraldi"),
        ("Ana Mattos Seabra", "AS Seabra"),
    ],
)
def test_caso4_nao_corresponde_autores_diferentes(
    nome_completo,
    nome_abreviado
):
    caso4 = CuradorDeDados()

    assert not caso4.corresponde_caso4(nome_completo, nome_abreviado)


@pytest.mark.caso_4
def test_caso4_deduplica_vanilda_cristina_junior():
    registros = [
        RegistroAutor(763027, "Vanilda Cristina Junior"),
        RegistroAutor(763027, "VC Junior"),
    ]

    deduplicador = DeduplicadorNomes()

    resultado = deduplicador.deduplicar_caso4(registros)

    assert resultado == [
        RegistroAutor(763027, "Vanilda Cristina Junior"),
        RegistroAutor(763027, "Vanilda Cristina Junior"),
    ]


@pytest.mark.caso_4
def test_caso4_deduplica_sergio_henrique_guaraldi():
    registros = [
        RegistroAutor(243350, "Sérgio Henrique Guaraldi"),
        RegistroAutor(954057, "SH Guaraldi"),
    ]

    deduplicador = DeduplicadorNomes()

    resultado = deduplicador.deduplicar_caso4(registros)

    assert resultado == [
        RegistroAutor(243350, "Sérgio Henrique Guaraldi"),
        RegistroAutor(954057, "Sérgio Henrique Guaraldi"),
    ]


@pytest.mark.caso_4
def test_caso4_lanca_excecao_quando_nome_completo_vazio():
    caso4 = CuradorDeDados()

    with pytest.raises(AutorInvalido):
        caso4.corresponde_caso4("", "VC Junior")


@pytest.mark.caso_4
def test_caso4_lanca_excecao_quando_nome_abreviado_vazio():
    caso4 = CuradorDeDados()

    with pytest.raises(AutorInvalido):
        caso4.corresponde_caso4("Vanilda Cristina Junior", "")
