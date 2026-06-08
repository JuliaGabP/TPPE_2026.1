import pytest
from src.caso_1 import resolveCaso1Grafia

@pytest.mark.caso1
def test_ResolverGrafiacomApostrofo():
    variacoes = ["Monica Hirata Sant`anna", "Mônica Hirata Sant’anna"]
    esperado = "Mônica Hirata Sant'anna"
    assert resolveCaso1Grafia(variacoes) == esperado

@pytest.mark.caso1
def test_ResolverGrafiacomAcento():
    variacoes = ["Sergio Henrique Guaraldi", "Sérgio Henrique Guaraldi"]
    esperado = "Sérgio Henrique Guaraldi"
    assert resolveCaso1Grafia(variacoes) == esperado 