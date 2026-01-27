from pydantic import BaseModel, model_validator
from datetime import date


class InventoryBase(BaseModel):
    quantity_in_stock: int
    received_at: date
    expires_at: date

    @model_validator(mode='after')
    def validate_dates(self):
        if self.expires_at < self.received_at:
            raise ValueError('expires_at cannot be before received_at')
        return self


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(InventoryBase):
    pass


class InventoryResponse(InventoryBase):
	id: int 

	class Config:
		from_attributes = True