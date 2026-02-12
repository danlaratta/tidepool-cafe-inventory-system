from app.crud.item_crud import ItemCrud
from app.crud.supplier_crud import SupplierCrud
from app.enums.item_category import ItemCategory
from app.enums.quantity_unit import QuantityUnit
from app.models.item import Item 
from app.models.supplier import Supplier


class ItemService:
    def __init__(self, item_crud: ItemCrud, supplier_crud: SupplierCrud) -> None:
        self.item_crud = item_crud
        self.supplier_crud = supplier_crud


    # Create new item
    async def create_item(self, name: str, category: ItemCategory, threshold: int, reitem_amount: int, unit: QuantityUnit, perishable: bool, supplier_id: int) -> Item:
        # Get the supplier
        supplier: Supplier = await self.supplier_crud.get_supplier(supplier_id)

        # Create item
        item: Item = Item(
            name = name, 
            category = category,
            reitem_threshold = threshold,
            reitem_amount = reitem_amount,
            quantity_unit = unit,
            perishable = perishable,
            supplier_id = supplier.id,
        )

        return await self.item_crud.create_item(item)


    # Get item
    async def get_item(self, item_id: int) -> Item:
        item: Item = await self.item_crud.get_item(item_id)
        return item
    

    # Update item
    async def update_item(self, item_id: int, threshold: int, reitem_amount: int ) -> Item:
        # Get item to update
        item: Item = await self.item_crud.get_item(item_id)

        # Validate
        if threshold < 0:
            raise ValueError('Reitem threshold must be a postivie number')
        
        if reitem_amount < 0:
            raise ValueError('Reitem amount must be a postivie number')
        
        # Update 
        item.reitem_threshold = threshold
        item.reitem_amount = reitem_amount

        return await self.item_crud.update_item(item)


    # Delete item
    async def delete_item(self, item_id: int) -> None:
        # Get item to delete 
        item: Item = await self.item_crud.get_item(item_id)
        await self.item_crud.delete_item(item)


