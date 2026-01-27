from pydantic import BaseModel, model_validator
from datetime import date
from app.enums.log_type import InventoryLogType


class InventoryLogBase(BaseModel):
    quantity_change_amount: int
    log_type: InventoryLogType
    created_at: date
    updated_at: date

    @model_validator(mode='after')
    def validate_dates(self):
        if self.updated_at < self.created_at:
            raise ValueError('updated_at cannot be before created_at')
        return self


class InventoryLogCreate(InventoryLogBase):
    item_id: int
    inventory_id: int


class InventoryLogUpdate(BaseModel):
    quantity_change_amount: int
    log_type: InventoryLogType
    updated_at: date


class InventoryLogResponse(InventoryLogBase):
    id: int 
    item_id: int
    inventory_id: int

    class Config:
        from_attributes = True