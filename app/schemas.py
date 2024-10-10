from pydantic import BaseModel, Field

from app import models
from fabric.common.schema import copy_schema
from fabric.common.sqlalchemy_to_pydantic import get_model_schema
from fabric.reference_routes.route_schema import PydanticRouteModelsFabric


class VehicleIdentity(BaseModel):
    id: int = Field()


VehicleBase = get_model_schema(models.Vehicle)
VehicleQuery = copy_schema(
    VehicleBase, name="VehicleQuery", exclude=VehicleIdentity.model_fields
)
VehicleCreate = copy_schema(
    VehicleBase, name="VehicleCreate", exclude=VehicleIdentity.model_fields
)
vehicle_fabric = PydanticRouteModelsFabric(
    VehicleBase, VehicleIdentity, query_class=VehicleQuery, create_class=VehicleCreate
)
