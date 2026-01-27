from pydantic import BaseModel, model_validator
from datetime import date
from app.enums.purchase_order_status import PurchaseOrderStatus


class PurchaseOrderBase(BaseModel):
    status: PurchaseOrderStatus
    created_at: date
    updated_at: date | None
    delivery_date: date | None

    @model_validator(mode='after')
    def validate_updated_at(self):
        if self.updated_at:
            if self.updated_at < self.created_at:
                raise ValueError('updated_at cannot be before created_at')
        return self
    
    @model_validator(mode='after')
    def validate_delivery_date(self):
        if self.delivery_date:
            if self.delivery_date < self.created_at:
                raise ValueError('delivery_date cannot be before created_at')
        return self


class PurchaseOrderCreate(PurchaseOrderBase):
    supplier_id: int


class PurchaseOrderUpdate(BaseModel):
    status: PurchaseOrderStatus
    updated_at: date | None
    delivery_date: date | None


class PurchaseOrderResponse(PurchaseOrderBase):
    id: int 
    supplier_id: int

    class Config:
        from_attributes = True