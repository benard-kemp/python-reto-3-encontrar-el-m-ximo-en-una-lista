import pytest
from reto_03_encontrar_maximo import encontrar_maximo


def test_lista_normal():
    assert encontrar_maximo([1, 3, 2]) == 3


def test_numeros_negativos():
    assert encontrar_maximo([-5, -1, -10]) == -1


def test_lista_con_un_elemento():
    assert encontrar_maximo([7]) == 7


def test_lista_vacia():
    assert encontrar_maximo([]) is None


def test_none_devuelve_none():
    assert encontrar_maximo(None) is None


def test_tipo_incorrecto_lanza_typeerror():
    with pytest.raises(TypeError):
        encontrar_maximo("123")
