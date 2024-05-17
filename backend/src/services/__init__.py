from fastapi import Depends
from src.configs.db_config.config import get_db_session
from src.repository import OrdersRepository

from .orders_service import OrdersService


async def get_orders_service(session=Depends(get_db_session)) -> OrdersService:
    return OrdersService(OrdersRepository(session))
