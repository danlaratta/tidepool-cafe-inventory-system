from pydantic import BaseModel
from datetime import datetime
from app.enums.purchase_order_status import PurchaseOrderStatus


class PurchaseOrderBase(BaseModel):
    status: PurchaseOrderStatus
    updated_at: datetime | None
    delivery_date: datetime | None


class PurchaseOrderCreate(PurchaseOrderBase):
    supplier_id: int


class PurchaseOrderUpdate(BaseModel):
    status: PurchaseOrderStatus
    delivery_date: datetime | None


class PurchaseOrderResponse(PurchaseOrderBase):
    id: int 
    supplier_id: int

    class Config:
        from_attributes = True