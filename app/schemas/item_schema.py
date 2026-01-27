from pydantic import BaseModel
from app.enums.item_category import ItemCategory
from app.enums.quantity_unit import QuantityUnit


class ItemBase(BaseModel):
    name: str 
    category: ItemCategory
    reorder_threshold: int 
    reorder_amount: int 
    quantity_unit: QuantityUnit
    perishable: bool 


class ItemCreate(ItemBase):
    supplier_id: int


class ItemUpdate(BaseModel):
    reorder_threshold: int 
    reorder_amount: int 


class ItemResponse(ItemBase):
    id: int 
    supplier_id: int

    class Config:
        from_attributes = True