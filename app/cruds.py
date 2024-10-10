from app import models, schemas
from fabric.common.crud import CRUDBase


class VehicleCrud(CRUDBase[models.Vehicle, schemas.VehicleBase]):
    def __init__(self):
        super().__init__(models.Vehicle)
