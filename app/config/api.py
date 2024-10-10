import os

import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from app.config.db import async_engine

host = os.getenv("API_HOST", "localhost")
port = os.getenv("API_PORT", "8000")
port = int(port)

app = FastAPI(title="VehicleFleet")
config = uvicorn.Config(app, host=host, port=port)
server = uvicorn.Server(config)
admin = Admin(app, async_engine)
