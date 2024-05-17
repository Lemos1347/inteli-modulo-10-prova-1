from typing import Sequence

from src.models import Orders
from src.repository import OrdersRepository
from src.schema.dtos import OrderCreationInputDTO, OrderUpdatesInputDTO, OrderDeletionOutputDTO


class OrdersService:
    def __init__(self, orders_repository: OrdersRepository) -> None:
        self.orders_repository = orders_repository

    async def create_order(self, order_info: OrderCreationInputDTO) -> Orders:
        return await self.orders_repository.create(
            user_name=order_info.user_name,
            user_email=order_info.user_email,
            description=order_info.description,
        )

    async def get_all_orders(self) -> Sequence[Orders]:
        return await self.orders_repository.get_all()

    async def get_order_by_id(self, order_id: str) -> Orders:
        order = await self.orders_repository.get_by_id(order_id)

        if order is None:
            raise RuntimeError("Could not find order with this id")

        return order

    async def modify_order(
        self, order_id: str, updates: OrderUpdatesInputDTO
    ) -> Orders:
        return await self.orders_repository.modify_order(order_id, updates.description)


    async def delete_order(self, order_id: str) -> OrderDeletionOutputDTO:
        deleted_order = await self.orders_repository.delete_order(order_id)

        if deleted_order is None:
            raise RuntimeError("Unable to delete order")

        return OrderDeletionOutputDTO(message=f"Order {order_id} deleted with success")
