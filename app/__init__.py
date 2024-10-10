from app import routes
from app.config.api import server, app

app.include_router(routes.vehicle_router)
