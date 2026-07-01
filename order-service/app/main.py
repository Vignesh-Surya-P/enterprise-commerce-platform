from fastapi import FastAPI

from app.api.orders import router as order_router

app = FastAPI(
    title="Enterprise Order Service",
    description="Order Service for Enterprise Multi-Vendor Commerce Integration Platform",
    version="1.0.0"
)

app.include_router(order_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Enterprise Order Service!"
    }