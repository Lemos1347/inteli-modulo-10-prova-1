from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Orders


class OrdersRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        return

    async def create(self, user_name: str, user_email: str, description: str) -> Orders:
        order = Orders(
            user_name=user_name, user_email=user_email, description=description
        )

        self.session.add(order)

        await self.session.flush()

        return order

    async def get_by_id(self, order_id: str) -> Orders | None:
        statement = select(Orders).filter_by(order_id=order_id)

        result = await self.session.execute(statement)

        return result.scalars().first()

    async def get_all(self) -> Sequence[Orders]:
        statement = select(Orders)

        result = await self.session.execute(statement)

        return result.scalars().all()

    async def modify_order(self, order_id: str, new_description: str) -> Orders:
        order = await self.get_by_id(order_id)

        if order is None:
            raise RuntimeError("Dont exist an order with this id")

        order.description = new_description

        return order

    async def delete_order(self, order_id: str) -> Orders:
        order = await self.get_by_id(order_id)

        if order is None:
            raise RuntimeError("Order with this id doesn't exists")

        await self.session.delete(order)

        return order
