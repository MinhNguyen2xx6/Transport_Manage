from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.db.database import engine, Base

from app.models.trip import Trip, TripItem

from app.websockets.manager import manager
import app.models as models
from app.api.v1.endpoints import trips

print("------------------------------------------")
print(f"🚀 PROJECT: {settings.PROJECT_NAME}")
print(f"🔗 DATABASE URI ĐANG DÙNG: {settings.SQLALCHEMY_DATABASE_URI}")
print("------------------------------------------")

# Auto create table for dev mode
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Cau hinh CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "project": settings.PROJECT_NAME,
        "status": "online",
        "message": "HE THONG DA SAN SANG",
    }


# Endpoint WebSocket cho Dashboard for realtime
@app.websocket("/ws/updates")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Giu ket noi open va nhan tin hieu ping tu client
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)


app.include_router(trips.router, prefix="/api/v1/trips", tags=["Quan ly lenh dieu xe"])
