from pydantic import BaseModel, EmailStr
from typing import List


class OrderItem(BaseModel):
    productId: str
    quantity: int


class OrderRequest(BaseModel):
    customerName: str
    email: EmailStr
    items: List[OrderItem]


class OrderResponse(BaseModel):
    orderId: str
    status: str
    message: str