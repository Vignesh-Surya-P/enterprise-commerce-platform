from uuid import uuid4

from app.schemas.order_schema import OrderRequest, OrderResponse


def create_order(order: OrderRequest) -> OrderResponse:
    """
    Business logic for creating an order.
    """

    order_id = f"ORD-{uuid4().hex[:8].upper()}"

    return OrderResponse(
        orderId=order_id,
        status="CREATED",
        message="Order created successfully"
    )