from pydantic import BaseModel, Field, model_validator
from datetime import datetime, date, timezone


class DeliveryBase(BaseModel):
    quantity_in_delivery: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    received_at: date = Field(default_factory=lambda: datetime.now(timezone.utc).date())
    expires_at: date

    @model_validator(mode='after')
    def validate_dates(self):
        if self.expires_at < self.received_at:
            raise ValueError('expires_at cannot be before received_at')
        return self


class DeliveryCreate(DeliveryBase):
    item_id: int 
    purchase_order_item_id: int


class DeliveryUpdate(BaseModel):
    quantity_in_stock: int
    expires_at: date


class DeliveryResponse(DeliveryBase):
    id: int 
    item_id: int 
    purchase_order_item_id: int

    class Config:
        from_attributes = True