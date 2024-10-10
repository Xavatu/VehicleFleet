from app import cruds
from app.config.db import get_session
from app.schemas import vehicle_fabric
from fabric.reference_routes.router_fabric import generate_routes_pack, Method

vehicle_router = generate_routes_pack(
    router_prefix="/vehicles",
    common_name="vehicle",
    crud=cruds.VehicleCrud(),
    fabric=vehicle_fabric,
    get_session=get_session,
    excluded_methods=[Method.put, Method.patch],
)
