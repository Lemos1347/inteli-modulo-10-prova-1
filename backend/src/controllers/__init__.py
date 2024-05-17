from fastapi import APIRouter

from .orders import OrdersRouter

EndPointsRouter = APIRouter()

EndPointsRouter.include_router(OrdersRouter)
