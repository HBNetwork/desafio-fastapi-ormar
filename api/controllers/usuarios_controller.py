from fastapi import APIRouter

from api.controllers.generic import (
    delete_controller, get_all_controller, get_controller,
    patch_controller, post_controller,
)
from api.models.requests.patch_usuario import UsuarioUpdate
from api.models.usuario import Usuario

user_router = APIRouter()


@user_router.post("/")
@post_controller
async def add_item(entidade: Usuario):
    pass


@user_router.get("/")
@get_all_controller(Usuario)
async def list_item():
    pass


@user_router.get("/{id}")
@get_controller(Usuario)
async def get_usuario(id: int):
    pass


@user_router.patch("/{id}")
@patch_controller(Usuario)
async def patch_usuario(propriedades_atualizacao: UsuarioUpdate, id: int):
    pass


@user_router.delete("/{id}")
@delete_controller(Usuario)
async def delete_usuario(id: int):
    pass
