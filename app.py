from fastapi import FastAPI
from routes.route_index import router

app = FastAPI()

app.include_router(router=router, prefix="/api/v1")