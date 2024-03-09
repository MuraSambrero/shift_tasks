from fastapi import APIRouter
from .route_shift import router_shifts

router = APIRouter()

@router.get("/")
def index():
    return {"message": "Hello World"}

router.include_router(router_shifts, prefix="/shifts", tags=["shifts"])