from app.schemas.inventory_schema import InventoryResponse


def get_inventory(product_id: str) -> InventoryResponse:
    """
    Temporary business logic.
    Later this will read from PostgreSQL.
    """

    return InventoryResponse(
        productId=product_id,
        availableQuantity=50,
        status="IN_STOCK"
    )