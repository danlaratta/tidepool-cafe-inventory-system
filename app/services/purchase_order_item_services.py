
from app.crud.purchase_order_item_crud import PurchaseOrderItemCrud
from app.crud.purchase_order_crud import PurchaseOrderCrud
from app.crud.item_crud import ItemCrud
from app.models.purchase_order_item import PurchaseOrderItem
from app.models.purchase_order import PurchaseOrder
from app.models.item import Item


class PurchaseOrderItemService:
    def __init__(self, order_item_crud: PurchaseOrderItemCrud, item_crud: ItemCrud, order_crud: PurchaseOrderCrud) -> None:
        self.order_item_crud = order_item_crud
        self.item_crud = item_crud
        self.order_crud = order_crud


    # Create purchase order item
    async def create_purchase_order_item(self, quantity: int, delivery_received: bool, item_id: int, purchase_order_id: int) -> PurchaseOrderItem:
        # Get item and purchase order
        item: Item = await self.item_crud.get_item(item_id)
        purchase_order: PurchaseOrder = await self.order_crud.get_purchase_order(purchase_order_id)

        # Create order item
        order_item: PurchaseOrderItem = PurchaseOrderItem(
            quantity = quantity,
            delivery_received = delivery_received,
            item_id = item.id,
            purchase_order_id = purchase_order.id, 
        )

        return await self.order_item_crud.create_order_item(order_item)


    # Get purchase order item    
    async def get_purchase_order_item(self, order_item_id: int) -> PurchaseOrderItem:
        order_item: PurchaseOrderItem = await self.order_item_crud.get_order_item(order_item_id)
        return order_item


    # Delete purchase order item
    async def delete_purchase_order_item(self, order_item_id: int) -> None:
        order_item: PurchaseOrderItem = await self.order_item_crud.get_order_item(order_item_id)
        await self.order_item_crud.delete_order_item(order_item)
        




