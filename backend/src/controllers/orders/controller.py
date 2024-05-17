from typing import List

from fastapi import APIRouter, Depends, HTTPException
from src.schema.dtos import (
    OrderCreationInputDTO,
    OrderDeletionOutputDTO,
    OrderOutputDTO,
    OrderUpdatesInputDTO,
)
from src.services import OrdersService, get_orders_service

router = APIRouter()


@router.post("/novo", response_model=OrderOutputDTO)
async def create_order_route(
    body: OrderCreationInputDTO,
    order_service: OrdersService = Depends(get_orders_service),
):
    try:
        return await order_service.create_order(body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/pedidos", response_model=List[OrderOutputDTO])
async def get_all_order_route(
    order_service: OrdersService = Depends(get_orders_service),
):
    try:
        return await order_service.get_all_orders()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/pedidos/{id}", response_model=OrderOutputDTO)
async def get_order_route(
    id: str, order_service: OrdersService = Depends(get_orders_service)
):
    try:
        return await order_service.get_order_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/pedidos/{id}", response_model=OrderOutputDTO)
async def update_order_route(
    id: str,
    updates: OrderUpdatesInputDTO,
    order_service: OrdersService = Depends(get_orders_service),
):
    try:
        return await order_service.modify_order(id, updates)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/pedidos/{id}", response_model=OrderDeletionOutputDTO)
async def delete_order_route(
    id: str,
    order_service: OrdersService = Depends(get_orders_service),
):
    try:
        return await order_service.delete_order(id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
