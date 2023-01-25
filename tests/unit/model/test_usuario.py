from api.models.usuario import Usuario
from tests.utils.usuarios import create_usuario_valido


def test_cria_usuario_valido() -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)
