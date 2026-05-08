from fastapi import WebSocket
from typing import List


class ConnectionManager:
    def __init__(self):
        # List thiet bi dang ket noi (High level)
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast_update(self, message: dict):
        """Cap nhat thong tin cho cac DASHBOARD dang open"""
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                # Xoa ket noi bi loi hoac da close
                self.disconnect(connection)


manager = ConnectionManager()
