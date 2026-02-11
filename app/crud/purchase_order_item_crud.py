from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.exceptions.database_exception import DatabaseException
from app.models.purchase_order_item import PurchaseOrderItem

class PurchaseOrderItemCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create PurchaseOrderItem 
    async def create_order_item(self, order_item: PurchaseOrderItem) -> PurchaseOrderItem:
        self.db_session.add(order_item)
        await self.db_session.flush()
        return order_item


    # Get PurchaseOrderItem 
    async def get_order_item(self, order_item_id: int) -> PurchaseOrderItem:
        result = await self.db_session.execute(select(PurchaseOrderItem).where(PurchaseOrderItem.id == order_item_id))
        order_item: PurchaseOrderItem | None = result.scalar_one_or_none()

        if order_item is None:
            raise DatabaseException(f'No purchase order item found with id: {order_item_id}')
        return order_item


    # Delete PurchaseOrderItem 
    async def delete_order_item(self, order_item: PurchaseOrderItem) -> None:
        await self.db_session.delete(order_item)