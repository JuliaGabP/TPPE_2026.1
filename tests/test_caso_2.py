import pytest

from src.registro_autor import RegistroAutor
from src.caso_2 import Caso2, AutorInvalido
from src.deduplicador import DeduplicadorNomes


@pytest.mark.caso_2
@pytest.mark.parametrize(
    "nome_completo, nome_abreviado",
    [
        ("Ana de Mattos Seabra", "Seabra A. M."),
        ("Ana de Mattos Seabra", "Seabra A M"),
        ("Cassius de Souza", "Souza C."),
        ("Verônica de Oliveira Moreira", "Moreira V O"),
        ("Verônica de Oliveira Moreira", "Moreira V. de O."),
        ("Luiz de Oliveira de Souza", "Souza L. O."),
        ("Mônica Hirata Sant'anna", "Sant'anna M. H."),
    ],
)
def test_caso2_corresponde_sobrenome_mais_iniciais(
    nome_completo,
    nome_abreviado
):
    caso2 = Caso2()

    assert caso2.corresponde(nome_completo, nome_abreviado)


@pytest.mark.caso_2
@pytest.mark.parametrize(
    "nome_completo, nome_abreviado",
    [
        ("Ana de Mattos Seabra", "Souza A M"),
        ("Cassius de Souza", "Seabra C"),
        ("Verônica de Oliveira Moreira", "Moreira V A"),
        ("Luiz de Oliveira de Souza", "Souza L X"),
    ],
)
def test_caso2_nao_corresponde_autores_diferentes(
    nome_completo,
    nome_abreviado
):
    caso2 = Caso2()

    assert not caso2.corresponde(nome_completo, nome_abreviado)


@pytest.mark.caso_2
def test_caso2_deduplica_nome_de_registro_autor():
    registros = [
        RegistroAutor(28372, "Ana de Mattos Seabra"),
        RegistroAutor(582585, "Seabra A. M."),
    ]

    deduplicador = DeduplicadorNomes()

    resultado = deduplicador.deduplicar_caso2(registros)

    assert resultado == [
        RegistroAutor(28372, "Ana de Mattos Seabra"),
        RegistroAutor(582585, "Ana de Mattos Seabra"),
    ]


@pytest.mark.caso_2
def test_caso2_deduplica_cassius_de_souza():
    registros = [
        RegistroAutor(28371, "Cassius de Souza"),
        RegistroAutor(746936, "Souza C."),
    ]

    deduplicador = DeduplicadorNomes()

    resultado = deduplicador.deduplicar_caso2(registros)

    assert resultado == [
        RegistroAutor(28371, "Cassius de Souza"),
        RegistroAutor(746936, "Cassius de Souza"),
    ]


@pytest.mark.caso_2
def test_caso2_lanca_excecao_quando_nome_completo_vazio():
    caso2 = Caso2()

    with pytest.raises(AutorInvalido):
        caso2.corresponde("", "Seabra A. M.")


@pytest.mark.caso_2
def test_caso2_lanca_excecao_quando_nome_abreviado_vazio():
    caso2 = Caso2()

    with pytest.raises(AutorInvalido):
        caso2.corresponde("Ana de Mattos Seabra", "")
