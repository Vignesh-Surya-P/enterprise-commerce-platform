from fastapi import APIRouter

from app.schemas.order_schema import OrderRequest, OrderResponse
from app.services.order_service import create_order

router = APIRouter(
    prefix="/api/v1/orders",
    tags=["Orders"]
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=201
)
def create_new_order(order: OrderRequest):
    """
    Create a new customer order.
    """
    return create_order(order)