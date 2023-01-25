from fastapi import APIRouter

from api.controllers import usuarios_controller as usuarios

router = APIRouter()

router.include_router(usuarios.router, prefix='/usuarios', tags=['Usuarios'])
