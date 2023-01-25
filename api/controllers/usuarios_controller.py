from fastapi import APIRouter
import ormar
from api.controllers.utils.delete_controller import delete_controller
from api.controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from api.controllers.utils.get_all_controller import get_all_controller
from api.controllers.utils.get_controller import get_controller
from api.controllers.utils.patch_controller import patch_controller
from api.controllers.utils.post_controller import post_controller
from api.models.usuario import Usuario
from api.models.requests.patch_usuario import UsuarioUpdate

router = APIRouter()

@router.post("/")
@post_controller
async def add_item(entidade: Usuario):
    pass

@router.get("/")
@get_all_controller(Usuario)
async def list_item():
    pass

@router.get("/{id}")
@get_controller(Usuario)
async def get_usuario(id: int):
    pass

@router.patch("/{id}")
@patch_controller(Usuario)
async def patch_usuario(propriedades_atualizacao: UsuarioUpdate, id: int):
    pass

@router.delete("/{id}")
@delete_controller(Usuario)
async def delete_usuario(id: int):
    pass
