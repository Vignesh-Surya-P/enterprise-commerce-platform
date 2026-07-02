from fastapi import APIRouter

from app.schemas.inventory_schema import InventoryResponse
from app.services.inventory_service import get_inventory

router = APIRouter(
    prefix="/api/v1/inventory",
    tags=["Inventory"]
)


@router.get(
    "/{product_id}",
    response_model=InventoryResponse
)
def check_inventory(product_id: str):
    return get_inventory(product_id)