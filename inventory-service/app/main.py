from fastapi import FastAPI

from app.api.inventory import router as inventory_router

app = FastAPI(
    title="Inventory Service",
    description="Inventory Management Microservice",
    version="1.0.0"
)

app.include_router(inventory_router)


@app.get("/")
def root():
    return {
        "message": "Inventory Service is running!"
    }