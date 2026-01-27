from pydantic import BaseModel


class PurchaseOrderItemBase(BaseModel):
    quantity: int
    delivery_received: bool


class PurchaseOrderItemCreate(PurchaseOrderItemBase):
    item_id: int
    purchase_order_id: int


class PurchaseOrderItemUpdate(PurchaseOrderItemBase):
    pass


class PurchaseOrderItemResponse(PurchaseOrderItemBase):
    id: int 
    item_id: int
    purchase_order_id: int

    class Config:
        from_attributes = True