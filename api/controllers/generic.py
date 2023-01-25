from functools import wraps

import ormar
from fastapi import HTTPException
from pydantic import BaseModel


def delete_controller(modelo: ormar.Model):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(id: int):
            entidade = await modelo.objects.get(id=id)
            return await entidade.delete()
        return wrapper
    return inner


def entidade_nao_encontrada(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ormar.exceptions.NoMatch:
            raise HTTPException(status_code=404, detail="Entidade não encontrada")
    return inner


def get_all_controller(modelo: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper():
            return await modelo.objects.all()
        return wrapper
    return inner


def get_controller(modelo: ormar.Model, select_related=[]):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(id: int):
            consulta = modelo.objects
            if len(select_related):
                consulta = consulta.select_related(select_related)
            entidade = await consulta.get(id=id)
            return entidade
        return wrapper
    return inner


def patch_controller(modelo: ormar.Model):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(propriedades_atualizacao: BaseModel, id: int):
            entidade_salva = await modelo.objects.get(id=id)
            propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
            await entidade_salva.update(**propriedades_atualizadas)
            return entidade_salva
        return wrapper
    return inner


def post_controller (func):
    @wraps(func)
    async def wrapper(entidade: ormar.Model):
        await entidade.save()
        return entidade
    return wrapper
