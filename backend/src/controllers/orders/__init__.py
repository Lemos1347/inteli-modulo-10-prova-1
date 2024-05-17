from fastapi import APIRouter

from .controller import router

OrdersRouter = APIRouter()

OrdersRouter.include_router(router, tags=["Users"])
