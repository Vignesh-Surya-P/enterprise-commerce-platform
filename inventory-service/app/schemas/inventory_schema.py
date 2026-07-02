from pydantic import BaseModel


class InventoryResponse(BaseModel):
    productId: str
    availableQuantity: int
    status: str