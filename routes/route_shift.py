from fastapi import APIRouter

router_shifts = APIRouter()

@router_shifts.get("/")
def shift():
    return {"message": "shift"}