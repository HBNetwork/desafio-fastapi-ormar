from fastapi import APIRouter

from api.controllers.usuarios_controller import user_router

root_router = APIRouter()

root_router.include_router(user_router, prefix='/usuarios', tags=['Usuarios'])
